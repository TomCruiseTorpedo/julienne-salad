# Demo Assets - Hero Files for Presentation

## Purpose
These are the specific image files used during the final demo presentation. They should be clean, impressive, and designed to make the SR&ED GPT app shine.

## Required Assets

### 1. git_log.png
**Purpose:** Screenshot of a git log showing technical commits

**Content Specifications:**
- Display 5-7 commit messages showing clear technical progression
- Include commit types: feat, fix, perf, refactor
- Show technical depth (e.g., parser implementation, AST generation, performance optimization)

**Example Commits to Include:**
```
feat(parser): Implement recursive descent parser for new syntax
fix(lexer): Correctly handle escaped characters in strings
perf(parser): Memoize parsing results to improve performance by 40%
refactor(core): Abstract tokenization logic into separate module
feat(ast): Add support for abstract syntax tree node generation
```

**Technical Details:**
- Format: PNG
- Recommended size: 1920x1080 or similar (high resolution for presentation)
- Background: Dark theme preferred (looks professional)
- Font: Monospace (typical terminal font)
- Include: Commit hashes, author (can be anonymized), timestamps

**How to Create:**
1. Use `git log --oneline --graph --decorate` in a real or mock repo
2. Take a high-quality screenshot
3. Crop to focus on the commit messages
4. Optional: Use tools like Carbon (carbon.now.sh) for styled code screenshots

---

### 2. architecture_diagram.png
**Purpose:** Technical architecture diagram showing system components

**Content Specifications:**
- Display microservices or system components
- Show connections/data flow between components
- Include annotations about technical challenges or uncertainties

**Example Components:**
```
Boxes: 
- User Auth Service
- API Gateway
- PostgreSQL DB
- Redis Cache
- Background Job Queue

Arrows: 
- Request flow from Gateway → Auth Service
- Data flow from Auth → DB
- Cache lookups between Gateway ↔ Redis

Annotations:
- "Uncertainty: How to scale Redis for 100k concurrent users?"
- "Experiment: Tried sharding the user table by region"
- "Challenge: State management across distributed sessions"
```

**Technical Details:**
- Format: PNG
- Recommended size: 1920x1080 or similar
- Style: Clean, professional (tools like draw.io, Lucidchart, Excalidraw)
- Colors: Use consistent color scheme
- Labels: Clear component names and relationships

**How to Create:**
1. Use diagramming tool (draw.io, Lucidchart, Excalidraw, or even PowerPoint)
2. Focus on showing technological complexity
3. Add brief annotations that hint at SR&ED-eligible challenges
4. Export as high-resolution PNG

---

### 3. jira_ticket.png
**Purpose:** Screenshot of a project management ticket showing technical investigation

**Content Specifications:**
- Display a realistic technical ticket with clear uncertainty
- Show description field with detailed technical context
- Include labels, priority, assignee fields

**Example Ticket Content:**
```
Title: Implement real-time collaboration feature

Priority: High
Type: Technical Investigation
Labels: research, websockets, scalability

Description:
The current architecture uses stateless REST APIs. To support real-time 
multi-user editing, we need to investigate a persistent connection-based 
paradigm like WebSockets.

Technological Uncertainty:
- How to maintain state and resolve edit conflicts at scale?
- What approach minimizes server load while maintaining low latency?
- How to handle connection drops and reconnection gracefully?

Proposed Investigation:
1. Benchmark WebSocket vs Server-Sent Events vs Long Polling
2. Prototype operational transformation algorithm
3. Load test with 1000 concurrent editing sessions
4. Analyze memory/CPU usage patterns

Acceptance Criteria:
- ≤100ms latency for edit propagation
- Handle 500+ concurrent connections per server instance
- Graceful degradation under high load
```

**Technical Details:**
- Format: PNG
- Recommended size: 1920x1080 or similar
- Background: Use actual Jira UI or mockup that looks like Jira/Linear/GitHub Issues
- Font: Standard UI font (readable at presentation scale)
- Include: Typical ticket metadata (ID, status, assignee, dates)

**How to Create:**
1. Use a real project management tool (Jira, Linear, Trello) or create mockup
2. Write a ticket that clearly demonstrates SR&ED eligibility
3. Take screenshot of the full ticket view
4. Crop and optimize for presentation

---

## Asset Quality Checklist

Before using assets in demo:
- [ ] High resolution (minimum 1080p)
- [ ] Clear, readable text (no blurry fonts)
- [ ] Professional appearance (no obvious mockup artifacts)
- [ ] Content demonstrates clear technological uncertainty
- [ ] Technical depth is appropriate (not too simple, not too obscure)
- [ ] Assets tell a cohesive story together

## Usage in Demo

**Demo Flow:**
1. **Upload git_log.png** → Show OCR extracting commit messages
2. **Generate narrative** → Display AI-generated SR&ED narrative
3. **Upload architecture_diagram.png** → Show handling of diagram annotations
4. **Generate narrative** → Show different type of technical uncertainty
5. **Upload jira_ticket.png** → Show comprehensive ticket analysis
6. **Generate final narrative** → Demonstrate quality and structure of output

## Notes

- Assets should be **visually impressive** but not overly complex
- Focus on **SR&ED-eligible content** (uncertainty, investigation, advancement)
- Ensure **consistency** across assets (similar technical domain if possible)
- Keep file sizes reasonable (< 5MB each for quick loading)
- Test OCR with each asset before demo day to ensure clean text extraction

## Asset Location

Place all three PNG files in this directory:
```
demo_assets/
├── README.md (this file)
├── git_log.png
├── architecture_diagram.png
└── jira_ticket.png
