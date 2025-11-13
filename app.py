import streamlit as st
import ollama
import easyocr
from PIL import Image
import numpy as np
import io

# --- MODEL LOADING (CACHED) ---

@st.cache_resource
def load_ocr_reader():
    """Loads the EasyOCR reader object once and caches it."""
    print("Loading EasyOCR reader...")
    reader = easyocr.Reader(['en'])
    print("Reader loaded.")
    return reader

def generate_narrative_local(extracted_text: str) -> str:
    """
    Generates the SR&ED narrative using the local Ollama model.
    Uses knowledge base-informed prompting with process entity models and Q&A patterns.
    """
    # Knowledge Base-Informed Prompting (Enhanced from user-provided corpus)
    knowledge_base_context = """
=== SR&ED KNOWLEDGE BASE CONTEXT ===

CORE SR&ED CONCEPTS (The 5 Questions):
1. Was there a scientific or technological uncertainty? (Not business uncertainty - must be technical)
2. Did it involve formulating hypotheses? (Specific, testable technical statements, not business goals)
3. Was the approach systematic? (Testing, analysis, experiments, not routine work)
4. Was the goal technological advancement? (Advancing the field, not just the product)
5. Were records/documentation kept? (Contemporaneous evidence is critical)

KEY DISTINCTIONS TO GET RIGHT:
- Business Goal ("We will make the software faster") ≠ SR&ED Hypothesis ("Algorithm X will reduce latency by overcoming the bottleneck")
- Business Project (overall commercial goal) ≠ SR&ED Project (focused sub-project addressing specific technical uncertainty)
- Routine engineering (standard practice, ineligible) ≠ Experimental development (novel approach, eligible)
- Product advancement (user-facing improvements) ≠ Technological advancement (new knowledge, underlying tech)
- Failed project (ineligible if no real experimentation) ≠ Failed experiment (eligible - proves a hypothesis wrong)

PROCESS MODEL - The Narrative Must Show:
PHASE 1 (Pre-Claim): Identify the Technological Uncertainty → Formulate SR&ED Hypothesis → Establish Documentation
PHASE 2 (Preparation): Gather Evidence → Separate SR&ED work from routine work → Write narratives for Lines 242, 244, 246
PHASE 3 (Filing/Review): Submit T661 form → Defend with Contemporaneous Documentation

THE THREE NARRATIVE SECTIONS (T661 Form Lines 242, 244, 246):

LINE 242 - TECHNOLOGICAL UNCERTAINTY:
- What specific technical problem could NOT be resolved using standard practice or publicly known solutions?
- Why was this problem non-obvious or novel? (Prove it wasn't routine)
- What was the "whether" or "how" that wasn't known?
- AVOID: Vague claims. BE SPECIFIC about what made this technically uncertain.

LINE 244 - SYSTEMATIC INVESTIGATION (The Proof of Process):
- What hypothesis did you formulate to test? (Specific, testable statement)
- What experiments, tests, or analyses did you conduct?
- What data did you collect? What tools, methods did you use?
- Show a logical progression: Hypothesis → Test → Result → Conclusion
- Include failed attempts - these are evidence of systematic investigation
- AVOID: High-level summaries. BE CONCRETE about the investigation process.

LINE 246 - TECHNOLOGICAL ADVANCEMENT (The Knowledge Gained):
- What new knowledge or capability did you gain? (Not commercial success - knowledge itself)
- How does this advance the underlying technology or field?
- What was learned that changes how you or others would solve similar problems?
- This can be negative learning too ("Approach X doesn't work" is advancement)
- AVOID: Confusing product benefits with technological advancement.

ENTITY MODEL - Key Relationships:
Project is DEFINED BY Technological Uncertainty
Project is TESTED VIA SR&ED Hypothesis
Project is PROVEN BY Contemporaneous_Documentation (commits, tickets, lab notes, timesheets)
Contemporaneous Documentation = Jira tickets, code commits, dated timesheets, meeting minutes, email threads, photos
CRITICAL: Use existing tools (Jira, GitHub, Trello) with SR&ED tags as your evidence source

COMMON PITFALLS TO AVOID:
- Claiming "routine debugging" as SR&ED work
- Vague language without specific technical details
- Confusing business goals with technological uncertainty
- Failing to show WHY existing solutions wouldn't work
- Using future tense instead of describing actual completed work
- Not separating SR&ED work from routine work
"""
    
    system_prompt = """You are an expert Canadian SR&ED consultant. Your role is to analyze technical work and generate compelling, CRA-compliant narratives for the T661 form.

CRITICAL PRINCIPLES:
1. SPECIFICITY: Always use concrete technical details (algorithm names, data structures, performance metrics, specific challenges)
2. LINKING: Clearly connect technological uncertainty → systematic investigation → advancement (the three-part story)
3. DISTINCTION: Actively separate SR&ED work from routine work; explain WHY the work was experimental/novel
4. EVIDENCE: Reference documented activities (commits, tickets, tests, experiments) as proof of systematic investigation
5. HONESTY: Failed experiments and negative results are valid SR&ED - show the investigation process, not just success

TONE: Professional, technical, suitable for a CRA assessor with engineering knowledge but not domain expert in your specific technology."""
    
    user_prompt = f"""{knowledge_base_context}

---EXTRACTED TECHNICAL DATA TO ANALYZE---
{extracted_text}

---YOUR TASK---
Analyze the above technical data and generate a compelling technical narrative for a Canadian SR&ED claim.

Structure your response with THREE clearly labeled sections (one for each form field):

## Line 242: Technological Uncertainty
Describe the specific technical problem or challenge that could NOT be resolved using standard practice or publicly known solutions. Explain WHY this was uncertain/non-obvious. Be specific about what made this work experimental.

## Line 244: Systematic Investigation
Detail the methodical approach used to test the hypothesis. Describe:
- The specific hypothesis you were testing
- Experiments or tests conducted
- Data collected and analyzed
- Tools and methods used
- Logical progression from hypothesis → test → result
- Include any failed attempts or negative results (these prove systematic investigation)

## Line 246: Technological Advancement
Explain the new knowledge or capability gained. Describe:
- What did you learn that advances the underlying technology/field?
- How does this change how the problem would be solved in the future?
- What new understanding was gained (even if negative/failure results)?
- Why is this advancement in TECHNOLOGY, not just in the product?

QUALITY GUIDELINES:
- Use specific technical terms, algorithm names, metrics (not generic language)
- Show WHY existing solutions/APIs/frameworks wouldn't work
- Explicitly separate SR&ED work from routine work
- Use active voice describing completed work (not future tense)
- Reference specific dates, tools, people when helpful
- Keep narrative cohesive: the three sections should tell ONE continuous story"""
    
    try:
        response = ollama.chat(
            model='sred-expert',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ],
            options={'temperature': 0.5}
        )
        return response['message']['content']
    except Exception as e:
        st.error(f"Error communicating with Ollama. Is the 'sred-expert' model running? Details: {e}")
        return ""

# --- UI & APPLICATION LOGIC ---

st.set_page_config(layout="wide", page_title="SR&ED GPT", page_icon="🍁")
st.title("🍁 SR&ED GPT")
st.subheader("Your AI Co-pilot for Canadian R&D Tax Credits")

# Load the OCR reader at the start
reader = load_ocr_reader()

col1, col2 = st.columns(2)

with col1:
    st.header("1. Provide Your Technical Data")
    
    # Using tabs for different input methods
    input_tab1, input_tab2 = st.tabs(["📄 Paste Text", "📸 Upload Image"])

    with input_tab1:
        user_input_text = st.text_area(
            "Paste git logs, Jira tickets, or technical notes here:", 
            height=300,
            placeholder="Example:\nfeat(parser): Implement recursive descent parser\nfix(lexer): Handle escaped characters\n..."
        )
    
    with input_tab2:
        uploaded_file = st.file_uploader(
            "Upload a screenshot, diagram, or document", 
            type=['png', 'jpg', 'jpeg'],
            help="Upload images of git logs, architecture diagrams, or project tickets"
        )

    if st.button("🚀 Generate SR&ED Narrative", type="primary", use_container_width=True):
        source_text = ""
        
        if user_input_text:
            source_text = user_input_text
        elif uploaded_file is not None:
            with st.spinner("📖 Reading image with EasyOCR..."):
                image = Image.open(uploaded_file).convert('RGB')
                image_np = np.array(image)
                results = reader.readtext(image_np)
                source_text = "\n".join([result[1] for result in results])
                
                # Show extracted text in an expander
                with st.expander("📝 Extracted Text from Image"):
                    st.text(source_text)
        else:
            st.warning("⚠️ Please paste text or upload an image first.")

        if source_text:
            with col2:
                st.header("2. AI-Generated SR&ED Narrative")
                with st.spinner("🤖 Consulting the AI expert... (this may take 30-60 seconds)"):
                    narrative_output = generate_narrative_local(source_text)
                    
                    if narrative_output:
                        st.markdown(narrative_output)
                        
                        # Add a download button for the generated narrative
                        st.download_button(
                            label="💾 Download Narrative",
                            data=narrative_output,
                            file_name="sred_narrative.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error("Failed to generate narrative. Check Ollama connection.")

with col2:
    if 'narrative_output' not in locals():
        st.header("2. AI-Generated Narrative")
        st.info("""
            **How to Use:**
            1.  **Paste Text** or **Upload an Image** of your technical work.
            2.  Click the **Generate** button.
            3.  The AI will analyze the data and draft a technical narrative based on official SR&ED guidelines.
            
            **What the AI Does:**
            - Extracts technical information from your input
            - Identifies potential technological uncertainties
            - Structures the narrative according to T661 form requirements (Lines 242, 244, 246)
            - Generates professional, CRA-compliant language
            
            **Disclaimer:** This is an AI-powered tool for generating drafts. Always review and edit the output with a qualified SR&ED consultant before submission to the CRA.
        """)
        
        st.markdown("---")
        
        st.markdown("""
            ### 📚 SR&ED Eligibility Quick Check
            
            Your work likely qualifies for SR&ED if:
            - ✅ There was **technological uncertainty** that couldn't be resolved through standard practice
            - ✅ You performed **systematic investigation** (experiments, testing, analysis)
            - ✅ The work resulted in **technological advancement** (new knowledge gained)
            
            **Not SR&ED:**
            - ❌ Routine engineering or debugging
            - ❌ Business or market uncertainty alone
            - ❌ Product improvements without underlying tech advancement
        """)
