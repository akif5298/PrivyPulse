from app.agents.data_agent import fetch_data
from app.agents.analysis_agent import analyze_data
from app.agents.synthesis_agent import synthesize
from app.agents.validator_agent import validate

def run_workflow(user_query: str):
    data = fetch_data(user_query)
    analysis = analyze_data(data)
    summary = synthesize(analysis)
    validated = validate(summary)

    return {
        "response": validated,
        "agents_used": [
            "DataAgent"
            "AnalysisAgent",
            "SynthesisAgent",
            "ValidationAgent"
        ]
    }