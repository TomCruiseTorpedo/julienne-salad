# SR&ED Research & Prompting Guide

## Core SR&ED Concepts (from CRA Guide T4088)

- **Line 242: Technological Uncertainty:** The "whether" or "how" to achieve a technical goal could not be known or determined based on standard practice or publicly available knowledge. This is the core technical problem or challenge.
- **Line 244: Work Performed:** The systematic investigation or search that was carried out by experiment or analysis. This includes the hypotheses tested, experiments conducted, data collected, and results analyzed.
- **Line 246: Technological Advancement:** The new knowledge gained that advanced the understanding of the underlying technology. It is an advancement in the technology itself, not just an advancement of the product.

## Example Raw Input (For Demo Asset Creation)

### Git Log Example
- `feat(parser): Implement recursive descent parser for new syntax`
- `fix(lexer): Correctly handle escaped characters in strings`
- `perf(parser): Memoize parsing results to improve performance by 40%`
- `refactor(core): Abstract tokenization logic into separate module`
- `feat(ast): Add support for abstract syntax tree node generation`

### Architecture Diagram Text Example
- `Boxes: User Auth Service, API Gateway, PostgreSQL DB, Redis Cache`
- `Arrows: Show request flow from Gateway to Auth Service`
- `Notes: "Uncertainty: How to scale Redis?" and "Experiment: Try sharding the user table."`

### Jira Ticket Example
- `Title: Implement real-time collaboration feature`
- `Description: The current architecture uses stateless REST APIs. To support real-time multi-user editing, we need to investigate a persistent connection-based paradigm like WebSockets. The primary technological uncertainty is how to maintain state and resolve edit conflicts at scale without introducing significant server load or latency.`

## Master Prompt Ideas

### System Prompt (for Modelfile)
You are an expert Canadian SR&ED consultant. You analyze technical data and convert it into formal, structured narratives suitable for government tax credit applications. You are precise, professional, and knowledgeable about the SR&ED program's requirements for demonstrating technological uncertainty and advancement.

### User Prompt (for app.py)
Based on the official Canadian SR&ED guidelines, analyze the following extracted technical data. Draft a compelling technical narrative for the "Technological Advancement" section of a T661 form. Structure your response clearly. Convert the technical jargon into a story of systematic investigation and overcoming technological uncertainty.

---RAW PROJECT DATA---
{extracted_text}

## Poor Man's RAG - Hardcoded CRA Guidelines

For the MVP, use this hardcoded context directly in prompts:

```python
cra_guidelines = """
Key principles for SR&ED technical narratives:
1. Technological Uncertainty: The "whether" or "how" to achieve a technical goal could not be known based on standard practice. Describe the technical problem.
2. Systematic Investigation: Detail the approach taken, including hypotheses, experiments, and analysis of results. Show a logical, planned process.
3. Technological Advancement: Explain how the work advanced the underlying technology. What new knowledge was gained? How is it a technological improvement, not just a product improvement?
"""
```

## Future Enhancement: Real RAG with ChromaDB

For v2.0, consider implementing proper RAG:
- Vector database: ChromaDB (lightweight, local-first)
- Embed T4088 guide sections as chunks
- Query relevant sections based on input context
- More dynamic, context-aware guidance retrieval
