# PrivyPulse Backend

FastAPI backend implementing the multi-agent architecture for PrivyPulse.

## Setup

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python -m uvicorn app.main:app --reload --port 8000
```

## Project Structure

```
backend/
├── app/
│   ├── agents/          # Multi-agent system
│   │   ├── coordinator.py      # Orchestrates agent workflow
│   │   ├── data_agent.py       # Fetches and aggregates data
│   │   ├── analysis_agent.py  # Analyzes data and extracts insights
│   │   ├── synthesis_agent.py # Synthesizes insights into summaries
│   │   └── validator_agent.py # Validates output quality
│   ├── api/             # API endpoints
│   │   └── query.py     # Query endpoint
│   ├── schemas/         # Pydantic models
│   │   └── query.py     # Request/response schemas
│   └── main.py          # FastAPI application
├── tests/               # Test suite
└── requirements.txt     # Python dependencies
```

## Testing

### Quick Start Testing

#### 1. Manual End-to-End Testing (UI)

**Start the servers:**
```bash
# Terminal 1: Backend
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm install
npm run dev
```

**Test queries to try:**
- "What are the current trends in artificial intelligence market?"
- "Compare cloud computing services AWS vs Azure"
- "Explain the growth of electric vehicle market"
- "What is the market size for cybersecurity solutions?"

**What to verify:**
- ✅ Response appears with structured format
- ✅ All 4 agents are listed in "Agents used"
- ✅ Validation status is shown
- ✅ Task focus is displayed
- ✅ Response contains sections (Summary, Findings, Implications, Recommendations)

#### 2. API Testing (curl/Postman)

**Health check:**
```bash
curl http://localhost:8000/
```

**Test query endpoint:**
```bash
curl -X POST http://localhost:8000/query/ \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the trends in renewable energy market?"}'
```

**Expected response structure:**
```json
{
  "response": "...",
  "agents_used": ["DataAgent", "AnalysisAgent", "SynthesisAgent", "ValidatorAgent"],
  "task_plan": {
    "focus": "trend_analysis",
    "priority": "normal"
  },
  "metadata": {
    "data_sources": ["web_search"],
    "validation_passed": true,
    "validation_notes": [...]
  }
}
```

#### 3. Unit Testing Individual Agents

Run the test suite:
```bash
cd backend
python -m pytest tests/ -v
```

**What each test verifies:**
- **DataAgent**: Fetches data, handles errors, retries
- **AnalysisAgent**: Extracts metrics, identifies trends, structures analysis
- **SynthesisAgent**: Creates summaries, extracts findings, generates recommendations
- **ValidatorAgent**: Validates completeness, checks quality, enhances content

#### 4. Integration Testing

Test the full workflow:
```bash
cd backend
python -m pytest tests/test_integration.py -v
```

**What it verifies:**
- Coordinator orchestrates all agents correctly
- Data flows properly between agents
- Error handling works end-to-end
- Response structure is correct

### Test Scenarios

#### Scenario 1: Successful Query Flow
**Query:** "What are the market trends for cloud computing?"
**Expected:**
- All 4 agents execute successfully
- Response contains structured insights
- Validation passes
- Task focus is "trend_analysis"

#### Scenario 2: Comparison Query
**Query:** "Compare SaaS vs PaaS market growth"
**Expected:**
- Task focus is "comparison"
- Analysis includes comparative insights
- Synthesis highlights differences

#### Scenario 3: Error Handling
**Query:** "" (empty query)
**Expected:**
- Graceful error message
- Error agent identified
- System doesn't crash

#### Scenario 4: Network Failure Simulation
**Test:** Disconnect internet temporarily
**Expected:**
- Data agent falls back to generated data
- System continues to work
- Error is logged but doesn't break flow

### Performance Testing

**Measure:**
- Response time (should be < 5 seconds for typical queries)
- Agent execution order
- Memory usage

**Command:**
```bash
time curl -X POST http://localhost:8000/query/ \
  -H "Content-Type: application/json" \
  -d '{"query": "test query"}'
```

### Validation Checklist

After running tests, verify:

- [ ] All agents are instantiated correctly
- [ ] Coordinator decomposes tasks appropriately
- [ ] Data agent fetches/aggregates data
- [ ] Analysis agent extracts insights
- [ ] Synthesis agent creates coherent summaries
- [ ] Validator agent checks quality
- [ ] Error handling works at each stage
- [ ] Response structure matches schema
- [ ] Frontend displays all metadata correctly
- [ ] Different query types trigger appropriate task plans

### Debugging Tips

**Enable verbose logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Check agent outputs individually:**
```python
from app.agents.data_agent import DataAgent
agent = DataAgent()
result = agent.fetch_data("test query", {"query": "test", "focus": "general_research"})
print(result)
```

**Inspect coordinator workflow:**
```python
from app.agents.coordinator import CoordinatorAgent
coordinator = CoordinatorAgent()
result = coordinator.run_workflow("test query")
print(result)
```

**Quick test script:**
```bash
python test_quick.py
```
