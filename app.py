import streamlit as st
import ollama
import easyocr
from PIL import Image
import numpy as np
import io
from datetime import datetime
import cv2

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

TONE: Professional, technical, suitable for a CRA assessor with engineering knowledge but not domain expert in your specific technology.

---

REFERENCE EXAMPLES (Few-Shot Training)

These examples demonstrate the pattern and structure for SR&ED-qualifying work narratives:

EXAMPLE 1: Agri-Tech Automation
Uncertainty: Could a novel humidity control mechanism stabilize rapidly changing greenhouse environments?
Work: Developed and trialed several control algorithms, modified hardware configurations, logged results under variable conditions, reviewed failure modes systematically.
Advancement: Clarified the instability factors affecting greenhouse automation, contributing new knowledge to agri-tech climate control through sensor response time analysis and algorithm tuning parameters.

EXAMPLE 2: Food Processing R&D
Uncertainty: Would natural preservative alternatives maintain shelf life and safety under real-world pH variation?
Work: Formulated experimental batches, varied pH conditions to simulate storage scenarios, tracked spoilage indicators, performed stability tests.
Advancement: Negative results revealed critical failure factors—specifically, pH sensitivity was higher than expected. These conclusions informed future development and advanced understanding of natural preservative chemistry.

EXAMPLE 3: Manufacturing Alloy Development
Uncertainty: Could new alloy compositions increase tool durability beyond commercial standards under elevated temperatures?
Work: Designed multiple prototype compositions with varying nickel percentages, manufactured test samples, tested at progressively escalating temperatures to identify failure points.
Advancement: Discovered a technical limit to temperature resistance and documented the precise role of nickel percentage. This clarified the composition-durability relationship, advancing sector knowledge.

EXAMPLE 4: Software Algorithm Optimization
Uncertainty: Could novel algorithms optimize large dataset sorting without common performance bottlenecks?
Work: Formulated efficiency hypothesis, coded and compared multiple algorithm variants, used 8M+ record benchmarking dataset, logged both successes and edge-case failures.
Advancement: Identified the true bottleneck (memory access patterns vs. computational complexity) and published a new algorithm approach addressing this limitation."""
    
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

def format_narrative_output(raw_output: str) -> tuple[str, str, str]:
    """
    Splits the raw narrative into thinking process and formatted output.
    Returns: (thinking_process, formatted_narrative, full_output_for_download)
    """
    # Split by the first occurrence of "## Line 242" to separate thinking from output
    lines = raw_output.split("\n")
    thinking_lines = []
    narrative_lines = []
    in_narrative = False
    
    for line in lines:
        if "## Line 242" in line:
            in_narrative = True
        
        if in_narrative:
            narrative_lines.append(line)
        else:
            thinking_lines.append(line)
    
    thinking_text = "\n".join(thinking_lines).strip()
    narrative_text = "\n".join(narrative_lines).strip()
    
    # Enhance formatting: add bullets and structure
    formatted_narrative = enhance_narrative_formatting(narrative_text)
    
    # Full output includes both thinking and narrative for download
    full_output = f"=== AI THINKING PROCESS ===\n\n{thinking_text}\n\n=== TECHNICAL NARRATIVE FOR T661 FORM ===\n\n{formatted_narrative}"
    
    return thinking_text, formatted_narrative, full_output

def enhance_narrative_formatting(narrative: str) -> str:
    """
    Enhances narrative formatting with bullets, bold text, and clearer section separation.
    """
    formatted = narrative.replace("**", "**")  # Preserve bold
    # Add more visual separation
    formatted = formatted.replace("## Line 242", "\n---\n## 📋 Line 242: Technological Uncertainty\n---")
    formatted = formatted.replace("## Line 244", "\n---\n## 📋 Line 244: Systematic Investigation\n---")
    formatted = formatted.replace("## Line 246", "\n---\n## 📋 Line 246: Technological Advancement\n---")
    
    return formatted

def process_multiple_inputs(source_texts: list[str], mode: str) -> str:
    """
    Process multiple input texts based on user preference.
    mode: "combined" or "separate"
    """
    if mode == "combined":
        # Merge all texts into one context
        combined_text = "\n\n---\n\n".join(source_texts)
        return generate_narrative_local(combined_text)
    else:
        # Generate separate narratives and combine them
        narratives = []
        for i, text in enumerate(source_texts, 1):
            st.write(f"Processing input {i}/{ len(source_texts)}...")
            narrative = generate_narrative_local(text)
            narratives.append(f"### Narrative {i}\n\n{narrative}")
        return "\n\n---\n\n".join(narratives)

# --- SESSION STATE INITIALIZATION ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- UI & APPLICATION LOGIC ---

st.set_page_config(layout="wide", page_title="SR&ED GPT", page_icon="🍁")
st.title("🍁 SR&ED GPT")
st.subheader("Your AI Co-pilot for Canadian R&D Tax Credits")

# Load the OCR reader at the start
reader = load_ocr_reader()

# --- SIDEBAR: SESSION HISTORY ---
with st.sidebar:
    st.header("📚 Session History")
    if st.session_state.history:
        st.write(f"**Generated Narratives:** {len(st.session_state.history)}")
        for i, item in enumerate(st.session_state.history, 1):
            with st.expander(f"📄 Result {i} - {item['timestamp']}"):
                st.text_area("View narrative", value=item['output'], height=200, disabled=True)
                st.download_button(
                    label=f"Download Result {i}",
                    data=item['output'],
                    file_name=f"sred_narrative_{i}_{item['timestamp'].replace(':', '-')}.txt",
                    key=f"download_{i}"
                )
    else:
        st.info("💡 Generated narratives will appear here during your session.")

# --- MAIN CONTENT ---
col1, col2 = st.columns(2)

with col1:
    st.header("1. Provide Your Technical Data")
    
    # Using tabs for different input methods
    input_tab1, input_tab2 = st.tabs(["📄 Paste Text", "📸 Upload Image(s)"])

    with input_tab1:
        user_input_text = st.text_area(
            "Paste git logs, Jira tickets, or technical notes here:", 
            height=300,
            placeholder="Example:\nfeat(parser): Implement recursive descent parser\nfix(lexer): Handle escaped characters\n..."
        )
    
    with input_tab2:
        st.write("**Upload one or more images:**")
        uploaded_files = st.file_uploader(
            "Select image(s) to upload", 
            type=['png', 'jpg', 'jpeg'],
            accept_multiple_files=True,
            help="Upload images of git logs, architecture diagrams, or project tickets"
        )
        
        # Processing preference for multiple images
        if uploaded_files and len(uploaded_files) > 1:
            st.write("**How should multiple images be processed?**")
            process_mode = st.radio(
                "Processing mode:",
                ["combined", "separate"],
                format_func=lambda x: "Combined Context (one narrative)" if x == "combined" else "Separate Narratives (one per image)",
                key="process_mode"
            )
        else:
            process_mode = "combined"

    if st.button("🚀 Generate SR&ED Narrative", type="primary", use_container_width=True):
        source_texts = []
        
        # Collect text input
        if user_input_text:
            source_texts.append(user_input_text)
        
        # Collect image inputs
        if uploaded_files:
            with st.spinner("📖 Reading images with EasyOCR..."):
                for uploaded_file in uploaded_files:
                    try:
                        # Load image with PIL and convert to RGB first
                        image = Image.open(uploaded_file).convert('RGB')
                        # Convert PIL Image to numpy array (RGB format)
                        image_rgb = np.array(image, dtype=np.uint8)
                        # Convert RGB to BGR for OpenCV/EasyOCR compatibility
                        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
                        # Ensure the array is contiguous in memory
                        image_bgr = np.ascontiguousarray(image_bgr)
                        # Pass BGR image to EasyOCR
                        results = reader.readtext(image_bgr)
                        extracted = "\n".join([result[1] for result in results])
                        source_texts.append(extracted)
                        
                        # Show extracted text in an expander
                        with st.expander(f"📝 Extracted Text from {uploaded_file.name}"):
                            st.text(extracted)
                    except Exception as e:
                        st.error(f"❌ Error processing {uploaded_file.name}: {str(e)}")
                        continue
        
        if not source_texts:
            st.warning("⚠️ Please paste text or upload image(s) first.")
        else:
            with col2:
                st.header("2. AI-Generated SR&ED Narrative")
                with st.spinner("🤖 Consulting the AI expert... (this may take 30-60 seconds per input)"):
                    # Process inputs based on mode
                    if len(source_texts) > 1:
                        narrative_output = process_multiple_inputs(source_texts, process_mode)
                    else:
                        narrative_output = generate_narrative_local(source_texts[0])
                    
                    if narrative_output:
                        # Split into thinking and narrative
                        thinking_process, formatted_narrative, full_output_for_download = format_narrative_output(narrative_output)
                        
                        # Display thinking process in collapsible expander
                        with st.expander("🤔 View AI's Thinking Process"):
                            st.markdown(thinking_process)
                        
                        # Display formatted narrative prominently (always visible, not in expander)
                        st.markdown("---")
                        st.subheader("📋 Technical Narrative for T661 Form")
                        st.markdown(formatted_narrative)
                        
                        # Download button with full output (thinking + narrative)
                        st.download_button(
                            label="💾 Download Narrative",
                            data=full_output_for_download,
                            file_name=f"sred_narrative_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain"
                        )
                        
                        # Add to session history
                        st.session_state.history.append({
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'output': formatted_narrative,
                            'input_count': len(source_texts)
                        })
                        st.success("✅ Narrative added to session history!")
                    else:
                        st.error("Failed to generate narrative. Check Ollama connection.")

with col2:
    if 'narrative_output' not in locals():
        st.header("2. AI-Generated Narrative")
        st.info("""
            **How to Use:**
            1. **Paste Text** or **Upload Image(s)** of your technical work.
            2. For multiple images, choose how they should be processed.
            3. Click the **Generate** button.
            4. The AI will analyze the data and draft a technical narrative based on official SR&ED guidelines.
            
            **What the AI Does:**
            - Extracts technical information from your input
            - Identifies potential technological uncertainties
            - Structures the narrative according to T661 form requirements (Lines 242, 244, 246)
            - Generates professional, CRA-compliant language
            - Provides formatted output ready for CRA submission
            
            **Features:**
            - 🤔 View AI's thinking process (hidden by default for cleaner UI)
            - 📝 Formatted narrative with clear sections
            - 📚 Session history sidebar for quick access to past generations
            - 💾 Download narratives for offline editing
            
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
