# SR&ED GPT Project Memory Bank

## Project Brief

**Name:** SR&ED GPT - Canadian R&D Tax Credit Copilot MVP

**Vision:** A specialized AI co-pilot that ingests a company's technical artifacts (code commits, project tickets, chats) and transforms them into compliant, high-quality technical narratives for the Canadian SR&ED tax incentive program.

**Core Value Proposition:** Demystifies and dramatically accelerates the SR&ED application process, converting hundreds of hours of high-cost engineering and administrative time into a few hours of review, maximizing claims and freeing up teams to focus on actual innovation.

**Status:** MVP (Initialization Phase)

---

## Tech Stack & Architecture

### Core Technologies
- **LLM Engine:** DeepSeek R1 Distill Qwen 1.5B Q6 K L
- **LLM Runtime:** Ollama (local inference)
- **OCR Engine:** Easy OCR (document processing)
- **Language:** Python 3.12.11
- **Deployment:** Local/standalone (no cloud dependencies)

### System Design Goals
1. **Local-First:** All processing on user's machine (no external APIs)
2. **Privacy:** No sensitive data leaves user's environment
3. **Efficiency:** Minimal resource requirements (1.5B model)
4. **Compliance:** Output narratives meet CRA SR&ED requirements

### Planned Architecture Layers
```
User Interface Layer
    ↓
Artifact Ingestion (commits, tickets, chats)
    ↓
Text Extraction & Preprocessing (Easy OCR)
    ↓
Context Summarization & Analysis
    ↓
DeepSeek R1 LLM (Ollama)
    ↓
Narrative Generation (SR&ED compliant)
    ↓
Output & Review Layer
```

---

## Project Context & Domain Knowledge

### SR&ED Program Overview
- **SR&ED:** Scientific Research and Experimental Development
- **Authority:** Canadian Revenue Agency (CRA)
- **Purpose:** Tax incentive for companies conducting eligible R&D
- **Challenge:** Documentation requirements are extensive and often misunderstood

### Key SR&ED Eligibility Criteria
- Work must be scientific or technological in nature
- Must involve systematic investigation with uncertainty
- Must involve creating new knowledge or capability
- Commerical viability uncertain at project start
- Work undertaken in Canada

### Narrative Requirements
- Technical detail demonstrating R&D nature of work
- Evidence of problem-solving approach
- Documentation of challenges overcome
- Clear timeline and resource allocation
- Compliance with CRA standards

### Input Artifacts
- Git commit history and messages
- Project management tickets/issues
- Team chat logs and discussions
- Design documents and specifications
- Technical incident reports

---

## Development Standards

### Python Environment
- **Version:** Python 3.12.11 (enforced globally via asdf)
- **Isolation:** venv per project
- **Dependencies:** Locked in requirements.txt
- **Style:** PEP 8 with Black formatter (target line length: 100)

### Git Workflow
- **Main branch:** Always production-ready
- **Feature branches:** feature/*, bugfix/*, docs/*
- **Commit format:** `type(scope): description`
- **Commit types:** feat, fix, docs, refactor, test, chore

### Documentation
- Docstrings: Google/NumPy style
- Complex logic: Inline comments
- Architectural decisions: Update memory.md
- README: Keep current with latest features

---

## Project Status & Timeline

### Current Phase: Initialization ✓
- [x] Repository created
- [x] .gitignore configured
- [x] README placeholder created
- [x] .clinerules established
- [x] Memory bank initialized
- [ ] Initial git commit
- [ ] First push to GitHub

### Next Phases (TBD)
- [ ] Phase 1: Core architecture & Ollama integration
- [ ] Phase 2: Document parsing & OCR pipeline
- [ ] Phase 3: Artifact ingestion layer
- [ ] Phase 4: Narrative generation engine
- [ ] Phase 5: SR&ED compliance validation
- [ ] Phase 6: UI/UX layer
- [ ] Phase 7: Testing & optimization
- [ ] Phase 8: MVP launch

---

## Cline Integration

### Available Tools
- **Preferred:** read_file, write_to_file, replace_in_file, execute_command, search_files
- **Available:** browser_action, MCP tools (as needed)
- **Enabled:** All tools (no restrictions)

### Key Commands
```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Ollama setup
ollama pull deepseek-r1:1.5b-q6_k_l

# Testing
python -m pytest

# Git operations
git status
git add .
git commit -m "message"
git push origin branch-name
```

### Memory Bank References
- **Global Context:** `/Users/jj/.cline/memory.md`
- **Global Rules:** `/Users/jj/.clinerules/`
- **Project Rules:** `.clinerules` (this directory)
- **GitHub Account:** TomCruiseTorpedo

---

## Important Notes

### Global Memory Bank Sync
This project references the global memory bank at `/Users/jj/.cline/memory.md`. Key information maintained globally:
- System configuration (Python 3.12.11, Node 22.21.1)
- Development environment setup
- Safety protocols and context management
- Version manager configurations (asdf, NVM)

### Context Management
- Monitor context usage during development
- At 75%+ context: use /smol or create /newtask
- Default model: Claude 4.5 Sonnet (required for SR&ED complexity)
- Escalate from Haiku if context >60%

### Safety Reminders
- No credentials in code (use .env)
- All inference local only (Ollama)
- Sanitize external data before processing
- Reference global rules before each session

---

## Session Checklist

Before starting work:
1. [ ] Verify Python 3.12.11 active: `python --version`
2. [ ] Check git status: `git status`
3. [ ] Review latest commits: `git log --oneline -5`
4. [ ] Confirm Ollama available (if needed): `ollama list`
5. [ ] Check context usage: Monitor progress bar

---

## Last Updated
2025-11-10, 2:56 PM - Initial project setup and memory bank creation

**Next Update:** When architecture decisions finalized or after Phase 1 completion
