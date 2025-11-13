# SR&ED GPT - Canadian R&D Tax Credit Copilot MVP

## Overview

A specialized AI co-pilot that ingests a company's technical artifacts (code commits, project tickets, chats) and transforms them into compliant, high-quality technical narratives for the Canadian SR&ED tax incentive program.

**Core Value Proposition:** Demystifies and dramatically accelerates the SR&ED application process, converting hundreds of hours of high-cost engineering and administrative time into a few hours of review, maximizing claims and freeing up teams to focus on actual innovation.

---

## Tech Stack

- **Application Framework:** Streamlit (Python web UI)
- **LLM Engine:** DeepSeek R1 Distill Qwen 1.5B Q6 K L (GGUF format)
- **LLM Runtime:** Ollama (local model serving)
- **OCR Library:** EasyOCR (text extraction from images)
- **Language:** Python 3.12.11
- **Architecture:** Local-first, stateless, privacy-focused

---

## Features

- 📄 **Dual Input Methods:** Paste text directly or upload images (screenshots, diagrams, tickets)
- 🔍 **OCR Integration:** Automatically extracts text from technical documents using EasyOCR
- 🤖 **AI-Powered Analysis:** Uses locally-run DeepSeek R1 model via Ollama for narrative generation
- 📋 **T661 Form Alignment:** Structures output according to CRA form requirements (Lines 242, 244, 246)
- 🔒 **Privacy-First:** All processing happens locally - no data leaves your machine
- 💾 **Export Ready:** Download generated narratives for review and submission
- ⚡ **Cached Performance:** EasyOCR loads once and stays in memory for fast processing

---

## Setup Instructions

### Prerequisites

- **Python 3.12.11** (verify with `python --version`)
- **Ollama** installed via Homebrew: `brew install ollama`
- **DeepSeek R1 Model File:** DeepSeek-R1-Distill-Qwen-1.5B-Q6_K_L.gguf (GGUF format)

### Step 1: Clone the Repository

```bash
git clone https://github.com/TomCruiseTorpedo/julienne-salad.git
cd julienne-salad
```

### Step 2: Create Python Virtual Environment

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** EasyOCR will automatically install PyTorch. First run may take several minutes to download OCR models (~100MB).

### Step 4: Create Custom Ollama Model

The `Modelfile` in this repository configures the DeepSeek R1 model specifically for SR&ED narrative generation.

```bash
# Create the custom 'sred-expert' model
ollama create sred-expert -f ./Modelfile
```

**Verify the model was created:**
```bash
ollama list
# Should show 'sred-expert' in the list
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## Usage

### Quick Start

1. **Start the app:** `streamlit run app.py`
2. **Choose input method:**
   - **Paste Text:** Enter git logs, Jira tickets, or technical notes directly
   - **Upload Image:** Upload screenshots of commits, diagrams, or project tickets
3. **Generate Narrative:** Click "🚀 Generate SR&ED Narrative"
4. **Review Output:** AI-generated narrative appears with structured sections
5. **Download:** Use "💾 Download Narrative" button to save for review

### Input Examples

**Git Log (Paste Text):**
```
feat(parser): Implement recursive descent parser for new syntax
fix(lexer): Correctly handle escaped characters in strings
perf(parser): Memoize parsing results to improve performance by 40%
```

**Architecture Diagram (Upload Image):**
- Screenshot showing system components
- Include annotations about technical challenges
- Notes on uncertainties or experiments

**Jira Ticket (Upload Image or Paste):**
- Technical investigation stories
- Research spikes with clear uncertainty
- Experiment descriptions and results

### Understanding the Output

The AI generates three key sections aligned with T661 form requirements:

**Line 242: Technological Uncertainty**
- Describes what couldn't be solved with standard practice
- Identifies the core technical challenge

**Line 244: Work Performed**
- Details the systematic investigation
- Lists experiments, tests, and analysis conducted

**Line 246: Technological Advancement**
- Explains new knowledge gained
- Shows how underlying technology was advanced

---

## Project Structure

```
julienne-salad/
├── app.py                    # Main Streamlit application
├── Modelfile                 # Ollama model configuration
├── requirements.txt          # Python dependencies
├── research/                 # SR&ED research materials
│   ├── source_material.md    # Prompting guide and examples
│   ├── official_references.md # CRA T4088 & T661 documentation
│   └── example_narratives.md # High-quality example collection
└── demo_assets/              # Demo presentation materials
    └── README.md             # Specifications for hero assets
```

---

## Architecture Notes

### "Poor Man's RAG" Approach

For the MVP, we use hardcoded CRA guidelines directly in the prompt rather than a vector database. This keeps the architecture simple while providing context-aware generation.

**Future Enhancement:** Implement proper RAG with ChromaDB for dynamic retrieval of T4088 guide sections.

### SR&ED Eligibility Criteria

Your work qualifies for SR&ED if it meets three criteria:

1. **Technological Advancement:** Sought to achieve scientific/technological advancement
2. **Technological Uncertainty:** Had uncertainty that couldn't be resolved through routine engineering
3. **Systematic Investigation:** Followed a methodical process of experimentation and analysis

**Common Pitfalls:**
- ❌ Routine debugging or standard engineering
- ❌ Business uncertainty without technical challenge
- ❌ Product improvements without underlying tech advancement

---

## Troubleshooting

### "Error communicating with Ollama"

**Solution:** Ensure Ollama service is running and the model is created:
```bash
# Check if Ollama is running
ollama list

# If 'sred-expert' is missing, create it
ollama create sred-expert -f ./Modelfile

# Test the model directly
ollama run sred-expert "Test prompt"
```

### EasyOCR Installation Issues

**Solution:** If PyTorch installation fails, try installing it separately first:
```bash
pip install torch torchvision
pip install -r requirements.txt
```

### Streamlit Won't Start

**Solution:** Verify Python version and virtual environment:
```bash
python --version  # Should be 3.12.11
which python      # Should point to venv/bin/python
```

---

## Development

### Running Tests

```bash
# Placeholder for future test suite
pytest
```

### Contributing

This is an MVP project. Contributions welcome after initial development phase.

---

## License

Apache License 2.0 - See LICENSE file for details.

---

## Disclaimer

This tool generates **draft narratives only**. Always review and edit the output with a qualified SR&ED consultant before submission to the Canada Revenue Agency. The authors are not responsible for the accuracy or acceptance of claims generated by this tool.

---

## License

Apache License 2.0 - See LICENSE file for details.
