# SR&ED GPT - Automated Narrative Generation for Canadian R&D Tax Claims

Struggling to articulate the technological uncertainty, systematic investigation, and advancement in your R&D work for Canada's Scientific Research and Experimental Development (SR&ED) program? SR&ED GPT is a locally-hosted AI assistant that generates high-quality, CRA-compliant narratives directly from your project documentation and code.

**This is a hackathon MVP** built to solve a real pain point: translating technical work into the specific language and structure required by CRA's T661 form (Lines 242, 244, and 246). While not a substitute for professional claim preparation, it dramatically reduces the time spent on first drafts and ensures consistency in SR&ED terminology.

## 🎯 Key Features

### v1.1 Enhancements
- **Multiple Image Upload**: Submit project documentation, screenshots, and code snippets all at once. Choose between combined narratives (synthesized context) or separate narratives for each image.
- **Session History**: All inputs, outputs, and formatting preferences persist within your session. No need to re-enter context across multiple queries.
- **Advanced Output Formatting**: Outputs include the AI's thinking process (hidden by default) and a polished, CRA-ready narrative with explicit section mapping to T661 form lines.

### Core Capabilities
- **Local LLM Integration**: Runs entirely on your machine using Ollama + DeepSeek R1 Distill Qwen (1.5B parameters). No cloud dependencies, no data sent elsewhere.
- **OCR Support**: Extract text from documentation images automatically using EasyOCR.
- **SR&ED-Specific Reasoning**: Embedded knowledge base patterns for technological uncertainty assessment, systematic investigation documentation, and advancement claims.
- **Streamlined UI**: Simple, intuitive Streamlit interface with copy-to-clipboard formatting for CRA submission.

## 🏗️ How It Works

### Architecture Overview

```
User Input (Text/Images)
    ↓
[Streamlit UI] ← Session State Management
    ↓
[Text Extraction] ← EasyOCR for images
    ↓
[Context Assembly] ← Multi-input processing
    ↓
[Ollama/DeepSeek] ← Local LLM inference
    ↓
[Output Formatting] ← Thinking + Narrative separation
    ↓
CRA-Ready Narrative Output
```

### Processing Pipeline

1. **Input Ingestion**: Users provide text descriptions and/or project documentation images
2. **Image Processing**: Images are processed with EasyOCR to extract text content
3. **Context Aggregation**: Multiple inputs (text + extracted text) are intelligently combined based on user preference
4. **LLM Inference**: Local DeepSeek model generates narratives with explicit reasoning about SR&ED criteria (uncertainty, investigation, advancement)
5. **Output Formatting**: Results are split into:
   - **Thinking Process**: Raw reasoning (useful for understanding the AI's assessment)
   - **Polished Narrative**: CRA-submission-ready text with T661 form section mapping

### SR&ED Knowledge Integration

The system uses embedded prompt patterns that:
- Guide the AI to identify technological uncertainty vs. normal engineering
- Document systematic investigation methodologies
- Articulate technological advancement relative to industry standards
- Map narrative content to specific CRA T661 form lines (242, 244, 246)

This is **not** a vector database or retrieval system—it's knowledge-as-prompts, ensuring deterministic and transparent reasoning.

## 🚀 Quick Start

### Prerequisites
- **Python 3.12.11** (required)
- **Ollama** installed and running locally ([Get Ollama](https://ollama.ai))
- **DeepSeek R1 Distill Qwen model** loaded (`ollama pull deepseek-r1:1.5b`)
- **GPU recommended** (for faster inference, though CPU works fine for MVP)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TomCruiseTorpedo/julienne-salad.git
   cd julienne-salad
   ```

2. Create a virtual environment:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure Ollama is running:
   ```bash
   ollama serve
   ```
   (In another terminal, pull the model if needed: `ollama pull deepseek-r1:1.5b`)

5. Launch the app:
   ```bash
   streamlit run app.py
   ```

6. Open your browser to `http://localhost:8501`

## 📖 Usage Guide

### Single-Input Workflow
Best for: Quick narrative generation from a single project description or document

1. Enter your project context in the text area (or paste code snippets, project summaries, etc.)
2. Click **"Generate SR&ED Narrative"**
3. Review the output (thinking + polished narrative)
4. Copy the narrative for submission

### Multi-Image Workflow (v1.1)
Best for: Complex projects documented across multiple sources (design docs, code screenshots, test reports)

1. Upload multiple images using the file uploader
2. Optionally add supplementary text context
3. Select preference:
   - **Combined**: Single unified narrative synthesizing all inputs (recommended for large contexts)
   - **Separate**: Individual narratives for each image (useful for modular projects)
4. Click **"Generate SR&ED Narrative"**
5. Review outputs and copy as needed

### Session History
All inputs, outputs, and user preferences are saved within your session:
- Switch between different projects without losing history
- Refine narratives iteratively based on feedback
- Session clears when you restart the app

## 📋 Understanding the Output

### T661 Form Mapping

The AI's output is structured to address three critical CRA requirements:

**Line 242 - Technological Uncertainty**
- Identifies gaps in knowledge or technical challenges that weren't readily deducible
- Explains why the problem wasn't a routine engineering task

**Line 244 - Work Performed**
- Documents the systematic investigation: hypotheses tested, methodologies used, experiments conducted
- Shows the breadth and depth of R&D activity

**Line 246 - Technological Advancement**
- Articulates what new technology or capability was achieved
- Connects to industry context and improvement over prior art

### Output Structure

Each narrative output includes:

1. **Thinking Process**: Raw reasoning from the AI model (hidden by default)
   - Use this to understand assessment logic and catch errors
   - Reference when preparing claim details with tax professionals

2. **Polished Narrative**: CRA-submission-ready text
   - Clear, concise language aligned with SR&ED terminology
   - Implicit section mapping to Lines 242/244/246
   - Ready to copy-paste into CRA forms or claim documents

## ⚙️ Advanced Features

### Customization via Prompts
The system uses role-based prompting (expert tax advisor + technical architect). Modify `app.py` to adjust:
- Formality level
- Technical depth
- SR&ED terminology emphasis
- Claim conservatism

### Local LLM Benefits
- **Privacy**: No data leaves your machine
- **Control**: Adjust model parameters, inference settings
- **Cost**: No API fees for unlimited queries
- **Offline**: Works without internet after initial model download

### Performance Tuning
- **CPU Mode**: 2-5 minutes per narrative (1.5B model)
- **GPU Mode**: 30-60 seconds per narrative (recommended)
- Adjust Ollama settings for your hardware in `~/.ollama/ollamarc`

## 🐛 Troubleshooting

### "Connection refused" / Ollama not found
**Problem**: Streamlit can't reach Ollama server
- Verify Ollama is running: `ollama list` in another terminal
- Check Ollama is on default port 11434
- Solution: Restart Ollama with `ollama serve`

### "Model not found" / sred-expert model missing
**Problem**: DeepSeek model not loaded locally
- Pull the model: `ollama pull deepseek-r1:1.5b`
- Verify it's available: `ollama list`
- Solution: The app will auto-pull if configured, or manually pull before starting

### OCR errors or empty text extraction
**Problem**: Images not processing correctly
- Verify image quality (clear, high contrast text)
- Check image format (JPEG, PNG, BMP supported)
- Logs show extraction details for debugging
- Solution: Pre-process poor-quality images or provide text manually

### Slow inference / hanging on generation
**Problem**: App stalled during narrative generation
- Check system resources (CPU/memory) with Activity Monitor
- For CPU-only systems, expect 2-5 min per narrative
- Verify model loaded: `ollama list`
- Solution: Consider GPU acceleration if available, or increase system resources

### Python version mismatch
**Problem**: "Python 3.12.11 required" error
- Verify Python version: `python --version`
- Check virtual environment activation
- Solution: Install Python 3.12.11 or update dependencies for compatible version

### Memory issues with large images
**Problem**: App crashes with large uploaded files
- Resize images before upload (recommend < 5MB)
- Limit to 3-5 images per session
- Solution: Process in batches if working with many documents

## 🔧 Development

### Project Structure
```
julienne-salad/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── Modelfile             # Ollama custom model configuration
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── .gitignore            # Excludes private docs, cache, LLM models
```

### Dependencies
- **streamlit**: UI framework
- **ollama**: Local LLM interface
- **easyocr**: Image-to-text extraction
- **pillow**: Image processing
- **numpy**: Numerical operations

See `requirements.txt` for full dependency list and versions.

### Contributing
This is a hackathon MVP. Future enhancements welcome:
- Vector database integration for larger knowledge bases
- Multi-model support (Llama 2, Mistral, etc.)
- Batch processing for multiple projects
- Export to CRA-standard formats
- Fine-tuned models for SR&ED claims
- Web deployment with sandboxed execution

### Running Tests (Future)
Comprehensive test suite planned for production version. Currently, manual testing recommended with real SR&ED claim scenarios.

## 🗺️ Roadmap

**v1.2 (Planned)**
- [ ] CRA T661 form auto-fill integration
- [ ] Export to Word/PDF with proper formatting
- [ ] Multi-language support (French translations for Quebec)
- [ ] Claim history persistence to local database

**v2.0 (Future)**
- [ ] Vector database for embedded knowledge base (RAG)
- [ ] Fine-tuned model specifically for SR&ED claims
- [ ] CRA technical guide references inline
- [ ] Collaborative claims (team inputs, version control)
- [ ] Professional claim review integration

## 📄 License

This project is provided as-is under the Apache License 2.0. See LICENSE file for details.

## ⚠️ Disclaimer

**SR&ED GPT is not a substitute for professional tax or legal advice.** 

This tool is designed to:
- ✅ Accelerate first-draft narrative generation
- ✅ Ensure consistent SR&ED terminology
- ✅ Reduce time spent on documentation

It is **not** designed to:
- ❌ Replace tax professionals or accountants
- ❌ Guarantee CRA approval (claims require qualification review)
- ❌ Provide legal advice
- ❌ Substitute for proper project record-keeping

**Always have generated narratives reviewed by a qualified tax professional or SR&ED claim preparer before submission to CRA.** The CRA reviews claims rigorously, and professional guidance significantly increases approval likelihood.

---

**Built with ❤️ as a hackathon MVP | Questions?** Open an issue on GitHub or reach out to the development team.
