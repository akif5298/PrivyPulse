import pytest
from app.agents.analysis_agent import AnalysisAgent


class TestAnalysisAgent:
    """Test suite for AnalysisAgent"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.agent = AnalysisAgent()
        self.test_data = """
        Market Analysis Data for: AI trends
        - Market Size: Growing sector with 25% annual growth
        - Growth Rate: Positive trajectory observed
        - Key Players: Multiple established companies
        - Regional Distribution: Global presence
        """
        self.test_task_plan = {
            "query": "AI market trends",
            "focus": "trend_analysis",
            "priority": "normal"
        }
    
    def test_agent_initialization(self):
        """Test that AnalysisAgent initializes correctly"""
        assert len(self.agent.analysis_categories) > 0
        assert "trends" in self.agent.analysis_categories
    
    def test_analyze_data_success(self):
        """Test successful data analysis"""
        result = self.agent.analyze_data(self.test_data, self.test_task_plan)
        
        assert result["success"] is True
        assert "analysis" in result
        assert len(result["analysis"]) > 0
        assert "metadata" in result
    
    def test_analyze_data_structure(self):
        """Test that analysis has correct structure"""
        result = self.agent.analyze_data(self.test_data, self.test_task_plan)
        
        if result["success"]:
            analysis = result["analysis"]
            assert "DATA ANALYSIS REPORT" in analysis
            assert "KEY METRICS" in analysis
            assert "IDENTIFIED TRENDS" in analysis
            assert "KEY INSIGHTS" in analysis
            assert "CATEGORIZED FINDINGS" in analysis
    
    def test_extract_key_metrics(self):
        """Test metric extraction"""
        metrics = self.agent._extract_key_metrics(self.test_data)
        assert len(metrics) > 0
        assert isinstance(metrics, list)
    
    def test_identify_trends(self):
        """Test trend identification"""
        trends = self.agent._identify_trends(self.test_data, self.test_task_plan)
        assert len(trends) > 0
        assert isinstance(trends, list)
    
    def test_extract_insights(self):
        """Test insight extraction"""
        insights = self.agent._extract_insights(self.test_data, self.test_task_plan)
        assert len(insights) > 0
        assert isinstance(insights, list)
    
    def test_categorize_findings(self):
        """Test finding categorization"""
        categorized = self.agent._categorize_findings(self.test_data)
        assert isinstance(categorized, dict)
        assert "market_dynamics" in categorized
        assert "growth_indicators" in categorized
    
    def test_analyze_empty_data(self):
        """Test analysis with empty data"""
        result = self.agent.analyze_data("", self.test_task_plan)
        assert result["success"] is False
        assert "error" in result
    
    def test_analyze_with_different_focuses(self):
        """Test analysis with different task focuses"""
        focuses = ["trend_analysis", "comparison", "explanation"]
        
        for focus in focuses:
            task_plan = {**self.test_task_plan, "focus": focus}
            result = self.agent.analyze_data(self.test_data, task_plan)
            assert result["success"] is True
