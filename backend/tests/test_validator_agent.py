import pytest
from app.agents.validator_agent import ValidatorAgent


class TestValidatorAgent:
    """Test suite for ValidatorAgent"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.agent = ValidatorAgent()
        self.test_content = """
        SYNTHESIZED INSIGHTS
        ======================================================================
        
        EXECUTIVE SUMMARY
        ----------------------------------------------------------------------
        Comprehensive analysis of AI market trends reveals significant growth
        opportunities and emerging patterns in the technology sector.
        
        KEY FINDINGS
        ----------------------------------------------------------------------
        1. Market is experiencing rapid growth with 25% annual increase
        2. Multiple key players are expanding their market presence
        3. Regional distribution shows global expansion
        
        IMPLICATIONS
        ----------------------------------------------------------------------
        1. Current trends indicate potential future market directions
        2. Growth patterns suggest opportunities for strategic positioning
        
        RECOMMENDATIONS
        ----------------------------------------------------------------------
        1. Continue monitoring key metrics and trends
        2. Consider further research in identified opportunity areas
        3. Leverage identified trends for strategic planning
        """
        self.test_query = "What are the trends in AI market?"
        self.test_task_plan = {
            "query": self.test_query,
            "focus": "trend_analysis",
            "priority": "normal"
        }
    
    def test_agent_initialization(self):
        """Test that ValidatorAgent initializes correctly"""
        assert self.agent.min_length > 0
        assert len(self.agent.required_sections) > 0
        assert 0 <= self.agent.quality_threshold <= 1
    
    def test_validate_success(self):
        """Test successful validation"""
        result = self.agent.validate(self.test_content, self.test_query, self.test_task_plan)
        
        assert result["success"] is True
        assert "validated_content" in result
        assert "passed" in result
        assert "notes" in result
        assert "scores" in result
    
    def test_check_completeness(self):
        """Test completeness checking"""
        completeness = self.agent._check_completeness(self.test_content, self.test_task_plan)
        
        assert "checks" in completeness
        assert "score" in completeness
        assert "passed" in completeness
        assert isinstance(completeness["score"], float)
        assert 0 <= completeness["score"] <= 1
    
    def test_check_quality(self):
        """Test quality checking"""
        quality = self.agent._check_quality(self.test_content)
        
        assert "checks" in quality
        assert "score" in quality
        assert "passed" in quality
        assert isinstance(quality["score"], float)
        assert 0 <= quality["score"] <= 1
    
    def test_check_sections(self):
        """Test section checking"""
        has_sections = self.agent._check_sections(self.test_content)
        assert isinstance(has_sections, bool)
    
    def test_check_query_relevance(self):
        """Test query relevance checking"""
        is_relevant = self.agent._check_query_relevance(self.test_content, self.test_task_plan)
        assert isinstance(is_relevant, bool)
    
    def test_validate_empty_content(self):
        """Test validation with empty content"""
        result = self.agent.validate("", self.test_query, self.test_task_plan)
        assert result["success"] is False
        assert result["passed"] is False
    
    def test_enhance_content(self):
        """Test content enhancement"""
        completeness = {"checks": {"has_sufficient_length": False}, "score": 0.5, "passed": False}
        quality = {"checks": {}, "score": 0.5, "passed": False}
        
        enhanced = self.agent._enhance_content(self.test_content, completeness, quality, self.test_task_plan)
        assert len(enhanced) >= len(self.test_content)
    
    def test_generate_validation_notes(self):
        """Test validation notes generation"""
        completeness = {"checks": {}, "score": 0.8, "passed": True}
        quality = {"checks": {}, "score": 0.7, "passed": True}
        
        notes = self.agent._generate_validation_notes(completeness, quality)
        assert len(notes) > 0
        assert isinstance(notes, list)
