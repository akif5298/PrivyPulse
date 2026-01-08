import pytest
from app.agents.synthesis_agent import SynthesisAgent


class TestSynthesisAgent:
    """Test suite for SynthesisAgent"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.agent = SynthesisAgent()
        self.test_analysis = """
        DATA ANALYSIS REPORT
        ============================================================
        
        KEY METRICS:
        - Growth rate: 25%
        - Market size: $50B
        
        IDENTIFIED TRENDS:
        - Positive growth trajectory observed
        - Upward trend in key indicators
        
        KEY INSIGHTS:
        1. Market is experiencing rapid growth
        2. Multiple opportunities identified
        
        CATEGORIZED FINDINGS:
        Market Dynamics:
        - Market conditions analyzed
        """
        self.test_task_plan = {
            "query": "AI market trends",
            "focus": "trend_analysis",
            "priority": "normal"
        }
    
    def test_agent_initialization(self):
        """Test that SynthesisAgent initializes correctly"""
        assert len(self.agent.synthesis_structure) > 0
        assert "executive_summary" in self.agent.synthesis_structure
    
    def test_synthesize_success(self):
        """Test successful synthesis"""
        result = self.agent.synthesize(self.test_analysis, self.test_task_plan)
        
        assert result["success"] is True
        assert "synthesis" in result
        assert len(result["synthesis"]) > 0
        assert "metadata" in result
    
    def test_synthesize_structure(self):
        """Test that synthesis has correct structure"""
        result = self.agent.synthesize(self.test_analysis, self.test_task_plan)
        
        if result["success"]:
            synthesis = result["synthesis"]
            assert "SYNTHESIZED INSIGHTS" in synthesis
            assert "EXECUTIVE SUMMARY" in synthesis
            assert "KEY FINDINGS" in synthesis
            assert "IMPLICATIONS" in synthesis
            assert "RECOMMENDATIONS" in synthesis
    
    def test_extract_executive_summary(self):
        """Test executive summary extraction"""
        summary = self.agent._extract_executive_summary(self.test_analysis, self.test_task_plan)
        assert len(summary) > 0
        assert isinstance(summary, str)
    
    def test_extract_key_findings(self):
        """Test key findings extraction"""
        findings = self.agent._extract_key_findings(self.test_analysis)
        assert len(findings) > 0
        assert isinstance(findings, list)
    
    def test_derive_implications(self):
        """Test implications derivation"""
        implications = self.agent._derive_implications(self.test_analysis, self.test_task_plan)
        assert len(implications) > 0
        assert isinstance(implications, list)
    
    def test_generate_recommendations(self):
        """Test recommendations generation"""
        recommendations = self.agent._generate_recommendations(self.test_analysis, self.test_task_plan)
        assert len(recommendations) > 0
        assert isinstance(recommendations, list)
    
    def test_synthesize_empty_analysis(self):
        """Test synthesis with empty analysis"""
        result = self.agent.synthesize("", self.test_task_plan)
        assert result["success"] is False
        assert "error" in result
    
    def test_synthesize_with_different_focuses(self):
        """Test synthesis with different task focuses"""
        focuses = ["trend_analysis", "comparison", "explanation"]
        
        for focus in focuses:
            task_plan = {**self.test_task_plan, "focus": focus}
            result = self.agent.synthesize(self.test_analysis, task_plan)
            assert result["success"] is True
