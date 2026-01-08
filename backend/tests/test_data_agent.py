import pytest
from app.agents.data_agent import DataAgent


class TestDataAgent:
    """Test suite for DataAgent"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.agent = DataAgent()
        self.test_query = "What are the trends in AI market?"
        self.test_task_plan = {
            "query": self.test_query,
            "focus": "trend_analysis",
            "priority": "normal"
        }
    
    def test_agent_initialization(self):
        """Test that DataAgent initializes correctly"""
        assert self.agent.max_retries == 3
        assert self.agent.timeout == 10
    
    def test_fetch_data_success(self):
        """Test successful data fetching"""
        result = self.agent.fetch_data(self.test_query, self.test_task_plan)
        
        assert result["success"] is True
        assert "data" in result
        assert result["data"] is not None
        assert len(result["data"]) > 0
        assert "sources" in result
        assert result["source_count"] > 0
    
    def test_fetch_data_structure(self):
        """Test that fetched data has correct structure"""
        result = self.agent.fetch_data(self.test_query, self.test_task_plan)
        
        if result["success"]:
            data = result["data"]
            assert "Data Collection Summary" in data
            assert "Collected Information" in data
            assert "Task Focus" in data
    
    def test_fetch_data_with_different_focuses(self):
        """Test data fetching with different task focuses"""
        focuses = ["trend_analysis", "comparison", "explanation", "general_research"]
        
        for focus in focuses:
            task_plan = {**self.test_task_plan, "focus": focus}
            result = self.agent.fetch_data(self.test_query, task_plan)
            assert result["success"] is True
    
    def test_generate_data_snippet_trend(self):
        """Test data snippet generation for trend queries"""
        snippet = self.agent._generate_data_snippet("market trends in technology")
        assert "Market Analysis" in snippet
        assert "Growth Rate" in snippet
    
    def test_generate_data_snippet_comparison(self):
        """Test data snippet generation for comparison queries"""
        snippet = self.agent._generate_data_snippet("compare AWS vs Azure")
        assert "Comparative Analysis" in snippet
    
    def test_aggregate_data(self):
        """Test data aggregation"""
        search_results = [
            {
                "source": "web_search",
                "title": "Test Title",
                "snippet": "Test snippet",
                "url": "http://test.com"
            }
        ]
        
        aggregated = self.agent._aggregate_data(search_results, self.test_query, self.test_task_plan)
        assert "Data Collection Summary" in aggregated
        assert self.test_query in aggregated
        assert "Test snippet" in aggregated
