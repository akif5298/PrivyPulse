from typing import Dict, List, Any, Optional
from app.agents.data_agent import DataAgent
from app.agents.analysis_agent import AnalysisAgent
from app.agents.synthesis_agent import SynthesisAgent
from app.agents.validator_agent import ValidatorAgent


class CoordinatorAgent:
    """
    Coordinator agent that decomposes tasks and orchestrates specialized agents.
    """
    
    def __init__(self):
        self.data_agent = DataAgent()
        self.analysis_agent = AnalysisAgent()
        self.synthesis_agent = SynthesisAgent()
        self.validator_agent = ValidatorAgent()
        self.agents_used = []
    
    def decompose_task(self, user_query: str) -> Dict[str, Any]:
        """
        Decompose the user query into subtasks for specialized agents.
        Returns a task plan with required steps.
        """
        # Identify query type and required agents
        query_lower = user_query.lower()
        
        task_plan = {
            "query": user_query,
            "requires_data": True,
            "requires_analysis": True,
            "requires_synthesis": True,
            "requires_validation": True,
            "priority": "normal",
            "focus": "general_research"
        }
        
        # Adjust plan based on query characteristics
        # Check for specific keywords with priority order
        # "explain" and "describe" take priority if they appear early in the query
        if query_lower.startswith(("explain", "describe")) or \
           (any(keyword in query_lower[:20] for keyword in ["explain", "describe"]) and 
            not any(keyword in query_lower for keyword in ["trend", "trends"])):
            task_plan["focus"] = "explanation"
        elif any(keyword in query_lower for keyword in ["compare", "versus", "vs", "difference", "vs."]):
            task_plan["focus"] = "comparison"
        elif any(keyword in query_lower for keyword in ["trend", "trends", "growth", "forecast"]):
            task_plan["focus"] = "trend_analysis"
        elif query_lower.startswith("what ") and "trend" not in query_lower and "compare" not in query_lower:
            task_plan["focus"] = "explanation"
        else:
            task_plan["focus"] = "general_research"
        
        return task_plan
    
    def run_workflow(self, user_query: str) -> Dict[str, Any]:
        """
        Orchestrate the multi-agent workflow with error handling.
        """
        self.agents_used = []
        
        try:
            # Step 1: Decompose task
            task_plan = self.decompose_task(user_query)
            
            # Step 2: Data Agent - Fetch relevant data
            self.agents_used.append("DataAgent")
            data_result = self.data_agent.fetch_data(user_query, task_plan)
            if not data_result or not data_result.get("success"):
                return self._handle_error("DataAgent", data_result.get("error", "Failed to fetch data"))
            
            # Step 3: Analysis Agent - Analyze the data
            self.agents_used.append("AnalysisAgent")
            analysis_result = self.analysis_agent.analyze_data(
                data_result.get("data", ""),
                task_plan
            )
            if not analysis_result or not analysis_result.get("success"):
                return self._handle_error("AnalysisAgent", analysis_result.get("error", "Failed to analyze data"))
            
            # Step 4: Synthesis Agent - Synthesize insights
            self.agents_used.append("SynthesisAgent")
            synthesis_result = self.synthesis_agent.synthesize(
                analysis_result.get("analysis", ""),
                task_plan
            )
            if not synthesis_result or not synthesis_result.get("success"):
                return self._handle_error("SynthesisAgent", synthesis_result.get("error", "Failed to synthesize"))
            
            # Step 5: Validator Agent - Validate output quality
            self.agents_used.append("ValidatorAgent")
            validation_result = self.validator_agent.validate(
                synthesis_result.get("synthesis", ""),
                user_query,
                task_plan
            )
            
            # Prepare final response
            final_response = validation_result.get("validated_content", synthesis_result.get("synthesis", ""))
            
            return {
                "response": final_response,
                "agents_used": self.agents_used,
                "task_plan": {
                    "focus": task_plan.get("focus", "general_research"),
                    "priority": task_plan.get("priority", "normal")
                },
                "metadata": {
                    "data_sources": data_result.get("sources", []),
                    "validation_passed": validation_result.get("passed", False),
                    "validation_notes": validation_result.get("notes", [])
                }
            }
            
        except Exception as e:
            return self._handle_error("Coordinator", str(e))
    
    def _handle_error(self, agent_name: str, error_message: str) -> Dict[str, Any]:
        """Handle errors gracefully and return error response."""
        return {
            "response": f"Error in {agent_name}: {error_message}. Please try rephrasing your query.",
            "agents_used": self.agents_used,
            "error": True,
            "error_agent": agent_name
        }


# Global coordinator instance
_coordinator = CoordinatorAgent()


def run_workflow(user_query: str) -> Dict[str, Any]:
    """Entry point for the workflow."""
    return _coordinator.run_workflow(user_query)