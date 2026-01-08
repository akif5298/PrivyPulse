# PrivyPulse

## Project Overview
PrivyPulse is a privacy-first, adaptive AI platform designed to demonstrate modern AI system design at an industry level. The system combines a multi-agent workflow architecture, real-time adaptive behavior, and privacy-preserving machine learning to solve complex information tasks without ever collecting or centralizing raw user data.

The project is developed in clearly defined phases, progressing from vision and scope definition to a fully working, deployable system.

---

## Problem
Most AI systems today are:
- Monolithic, relying on a single model to handle many tasks
- Static, with little ability to adapt to real user behavior after deployment
- Dependent on centralized user data collection, creating privacy and security risks

These limitations result in tools that are generic, inflexible, and unsuitable for privacy-sensitive or user-centric applications.

---

## Solution
PrivyPulse addresses these issues by:
- Using a **multi-agent architecture**, where specialized agents collaborate on different parts of a task
- Continuously adapting outputs and interface behavior based on observed user interactions
- Leveraging **privacy-preserving learning techniques** (e.g., federated learning) so that raw user data never leaves its local environment

The result is an AI system that is collaborative, adaptive, and privacy-first by design.

---

## MVP Use Case (Locked)
**Privacy-Preserving Market Research Assistant**

The MVP demonstrates how PrivyPulse can:
- Accept market or trend-related questions
- Decompose tasks across multiple AI agents
- Generate structured insights collaboratively
- Adapt recommendations based on user interaction
- Improve learning outcomes without storing personal data

This use case remains fixed throughout development.

---

## Core Demo Flow (Locked)
1. User submits a research question
2. A coordinator agent decomposes the task
3. Specialized agents perform data retrieval, analysis, and synthesis
4. A validation step ensures output quality
5. Results are presented to the user
6. User interactions are logged
7. The system adapts future behavior based on interaction patterns
8. A visual explanation highlights privacy-preserving learning

---

## Development Roadmap

### Phase 0: Vision Lock & Scope Definition
**Goal:** Eliminate ambiguity and prevent scope creep.

Deliverables:
- Defined problem and solution
- Locked MVP use case
- Fixed demo flow
- Feature inclusion and exclusion list
- Clear success criteria

No production code is written during this phase.

---

### Phase 1: System Skeleton
**Goal:** Establish an end-to-end working pipeline.

Focus:
- Basic frontend (single input, single output)
- Backend API with placeholder responses
- Initial agent orchestrator with mocked agents

Outcome:
- A query can flow through the system end-to-end.

---

### Phase 2: Multi-Agent Architecture
**Goal:** Implement real multi-agent collaboration.

Focus:
- Coordinator agent
- Specialized agents (data, analysis, synthesis, validation)
- Agent communication and orchestration
- Error handling and task coordination

Outcome:
- Agents collaborate to produce real outputs.

---

### Phase 3: Adaptive Learning Loop
**Goal:** Enable the system to learn from user behavior.

Focus:
- Interaction logging (clicks, time spent, navigation)
- Periodic retraining or adjustment logic
- Adaptive UI or output ranking

Outcome:
- System behavior changes based on real usage patterns.

---

### Phase 4: Privacy-Preserving Learning
**Goal:** Demonstrate privacy-first intelligence.

Focus:
- Federated learning (simulated or real)
- Secure aggregation of model updates
- Comparison of centralized vs federated learning outcomes
- Clear privacy explanation

Outcome:
- Learning occurs without collecting raw user data.

---

### Phase 5: Metrics & Monitoring
**Goal:** Make the system production-aware.

Focus:
- Performance metrics (latency, throughput)
- Agent health and reliability
- Learning effectiveness and engagement metrics
- Visualization dashboards

Outcome:
- System behavior and performance are measurable and transparent.

---

### Phase 6: Deployment & Polish
**Goal:** Prepare the project for real-world demonstration.

Focus:
- Containerization (Docker)
- Cloud deployment (AWS/GCP)
- Documentation and diagrams
- Demo-ready UI and workflows

Outcome:
- The system is deployable, stable, and demo-ready.

---

### Phase 7: Presentation & Employer Readiness
**Goal:** Clearly communicate technical depth and impact.

Deliverables:
- Architecture diagrams
- Demo video
- Case study-style explanation
- Resume and portfolio-ready project description

Outcome:
- The project can be confidently presented to employers and technical reviewers.

---

## MVP Feature Scope

### Included
- Multi-agent orchestration
- Adaptive behavior from user interaction
- Privacy-preserving learning
- System metrics and monitoring
- Clear privacy explanations

### Explicitly Excluded
- User authentication or accounts
- Payments or monetization
- Mobile applications
- Non-essential UI animations
- Additional product verticals

---

## Success Criteria
The MVP is considered successful if:
- A non-technical user can understand the system within 60 seconds
- The system demonstrates visible adaptation over time
- Privacy-preserving learning is clearly communicated
- The workflow runs end-to-end without manual intervention
- The project can be confidently demoed live

---

## Guiding Principles
- Privacy-first by design
- Clear separation of responsibilities
- Adaptation driven by real user behavior
- Engineering decisions justified by measurable outcomes

All future development phases must align with this document.

---

## Quick Start Guide

### Start the Servers

**Terminal 1: Backend Server**
```bash
cd backend
pip install -r requirements.txt  # If not already installed
python -m uvicorn app.main:app --reload --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Terminal 2: Frontend Server**
```bash
cd frontend
npm install  # If not already installed
npm run dev
```

You should see:
```
- ready started server on 0.0.0.0:3000
```

### Test in Browser

1. Open http://localhost:3000 in your browser
2. Try these example queries:

**Trend Analysis:**
- "What are the trends in artificial intelligence market?"
- "What are the current trends in cloud computing?"

**Comparison:**
- "Compare AWS vs Azure cloud services"
- "Compare SaaS vs PaaS market growth"

**Explanation:**
- "Explain the growth of electric vehicle market"
- "Describe the cybersecurity market landscape"

**General Research:**
- "Market research on renewable energy"
- "Analysis of fintech industry"

### What to Look For

✅ **Response Structure:**
- Formatted output with sections (Summary, Findings, Implications, Recommendations)
- Monospace font for readability

✅ **Execution Details:**
- All 4 agents listed: DataAgent, AnalysisAgent, SynthesisAgent, ValidatorAgent
- Task focus displayed (trend_analysis, comparison, explanation, etc.)
- Validation status (✓ Passed or ⚠ Needs improvement)
- Data sources used

✅ **Features:**
- Loading state while processing
- Error handling if backend is down
- Enter key to submit
- Disabled button when query is empty

### Troubleshooting

**Backend not connecting:**
- Make sure backend is running on port 8000
- Check http://localhost:8000/ in browser (should show `{"status":"ok"}`)

**Frontend not loading:**
- Make sure frontend is running on port 3000
- Check browser console for errors

**No response:**
- Check backend terminal for error messages
- Verify all dependencies are installed
- Try the health check endpoint: http://localhost:8000/

### API Testing (Alternative)

You can also test directly via API:

```bash
curl -X POST http://localhost:8000/query/ \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the trends in AI market?"}'
```