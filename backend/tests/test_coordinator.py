import pytest
from app.agents.coordinator import CoordinatorAgent


class TestCoordinatorAgent:
    """Test suite for CoordinatorAgent"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.coordinator = CoordinatorAgent()
    
    def test_coordinator_initialization(self):
        """Test that CoordinatorAgent initializes correctly"""
        assert self.coordinator.data_agent is not None
        assert self.coordinator.analysis_agent is not None
        assert self.coordinator.synthesis_agent is not None
        assert self.coordinator.validator_agent is not None
        assert isinstance(self.coordinator.agents_used, list)
    
    def test_decompose_task_trend_analysis(self):
        """Test task decomposition for trend analysis queries"""
        query = "What are the trends in cloud computing market?"
        task_plan = self.coordinator.decompose_task(query)
        
        assert task_plan["query"] == query
        assert task_plan["focus"] == "trend_analysis"
        assert task_plan["requires_data"] is True
        assert task_plan["requires_analysis"] is True
    
    def test_decompose_task_comparison(self):
        """Test task decomposition for comparison queries"""
        query = "Compare AWS vs Azure cloud services"
        task_plan = self.coordinator.decompose_task(query)
        
        assert task_plan["focus"] == "comparison"
    
    def test_decompose_task_explanation(self):
        """Test task decomposition for explanation queries"""
        query = "Explain the growth of electric vehicle market"
        task_plan = self.coordinator.decompose_task(query)
        
        assert task_plan["focus"] == "explanation"
    
    def test_decompose_task_general(self):
        """Test task decomposition for general queries"""
        query = "Random query without specific keywords"
        task_plan = self.coordinator.decompose_task(query)
        
        assert task_plan["focus"] == "general_research"
    
    def test_run_workflow_success(self):
        """Test successful workflow execution"""
        query = "What are the trends in AI market?"
        result = self.coordinator.run_workflow(query)
        
        assert "response" in result
        assert "agents_used" in result
        assert len(result["agents_used"]) == 4
        assert "DataAgent" in result["agents_used"]
        assert "AnalysisAgent" in result["agents_used"]
        assert "SynthesisAgent" in result["agents_used"]
        assert "ValidatorAgent" in result["agents_used"]
    
    def test_run_workflow_structure(self):
        """Test workflow result structure"""
        query = "Test market research query"
        result = self.coordinator.run_workflow(query)
        
        assert "task_plan" in result
        assert "metadata" in result
        assert result["task_plan"]["focus"] in ["trend_analysis", "comparison", "explanation", "general_research"]
    
    def test_run_workflow_error_handling(self):
        """Test error handling in workflow"""
        # Test with potentially problematic query
        query = "a" * 1000  # Very long query
        result = self.coordinator.run_workflow(query)
        
        # Should still return a result (either success or error)
        assert "response" in result
        assert "agents_used" in result
    
    def test_handle_error(self):
        """Test error handling method"""
        error_result = self.coordinator._handle_error("TestAgent", "Test error message")
        
        assert "response" in error_result
        assert "error" in error_result
        assert error_result["error"] is True
        assert error_result["error_agent"] == "TestAgent"
        assert "Test error message" in error_result["response"]
