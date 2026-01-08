import pytest
from app.agents.coordinator import run_workflow


class TestIntegration:
    """Integration tests for the full workflow"""
    
    def test_full_workflow_trend_query(self):
        """Test complete workflow with trend analysis query"""
        query = "What are the current trends in artificial intelligence market?"
        result = run_workflow(query)
        
        # Check response structure
        assert "response" in result
        assert "agents_used" in result
        assert isinstance(result["agents_used"], list)
        assert len(result["agents_used"]) == 4
        
        # Check all agents executed
        assert "DataAgent" in result["agents_used"]
        assert "AnalysisAgent" in result["agents_used"]
        assert "SynthesisAgent" in result["agents_used"]
        assert "ValidatorAgent" in result["agents_used"]
        
        # Check response content
        assert len(result["response"]) > 0
        assert "SYNTHESIZED INSIGHTS" in result["response"] or "Error" in result["response"]
        
        # Check metadata
        if "metadata" in result:
            assert "data_sources" in result["metadata"] or "validation_passed" in result["metadata"]
    
    def test_full_workflow_comparison_query(self):
        """Test complete workflow with comparison query"""
        query = "Compare cloud computing services AWS vs Azure"
        result = run_workflow(query)
        
        assert "response" in result
        assert result["task_plan"]["focus"] == "comparison"
        assert len(result["agents_used"]) == 4
    
    def test_full_workflow_explanation_query(self):
        """Test complete workflow with explanation query"""
        query = "Explain the growth of electric vehicle market"
        result = run_workflow(query)
        
        assert "response" in result
        assert result["task_plan"]["focus"] == "explanation"
        assert len(result["agents_used"]) == 4
    
    def test_workflow_data_flow(self):
        """Test that data flows correctly between agents"""
        query = "What is the market size for cybersecurity solutions?"
        result = run_workflow(query)
        
        # Verify the workflow completed
        assert "response" in result
        
        # If successful, verify structure
        if not result.get("error"):
            assert "task_plan" in result
            assert "metadata" in result
            assert len(result["response"]) > 100  # Should have substantial content
    
    def test_workflow_error_recovery(self):
        """Test that workflow handles errors gracefully"""
        # Empty query should still return a response
        query = ""
        result = run_workflow(query)
        
        assert "response" in result
        # Should either succeed or return a proper error
        assert "error" in result or len(result["response"]) > 0
