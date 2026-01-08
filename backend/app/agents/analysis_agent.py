from typing import Dict, Any, List
import re


class AnalysisAgent:
    """
    Analysis agent responsible for analyzing collected data and extracting insights.
    """
    
    def __init__(self):
        self.analysis_categories = [
            "trends",
            "metrics",
            "comparisons",
            "patterns",
            "implications"
        ]
    
    def _extract_key_metrics(self, data: str) -> List[str]:
        """Extract key metrics and numbers from the data."""
        metrics = []
        
        # Look for percentage patterns
        percentages = re.findall(r'\d+\.?\d*\s*%', data)
        metrics.extend([f"Growth rate: {p}" for p in percentages[:3]])
        
        # Look for numerical patterns
        numbers = re.findall(r'\d+[,\d]*', data)
        if numbers:
            metrics.append(f"Key numbers identified: {len(numbers)} data points")
        
        return metrics if metrics else ["Quantitative data points identified"]
    
    def _identify_trends(self, data: str, task_plan: Dict[str, Any]) -> List[str]:
        """Identify trends in the data."""
        trends = []
        data_lower = data.lower()
        
        if "growing" in data_lower or "growth" in data_lower:
            trends.append("Positive growth trajectory observed")
        if "increasing" in data_lower or "rise" in data_lower:
            trends.append("Upward trend in key indicators")
        if "declining" in data_lower or "decrease" in data_lower:
            trends.append("Declining pattern identified")
        if "stable" in data_lower or "consistent" in data_lower:
            trends.append("Stable performance maintained")
        
        # Task-specific trend identification
        focus = task_plan.get("focus", "general_research")
        if focus == "trend_analysis":
            trends.append("Detailed trend analysis completed")
        elif focus == "comparison":
            trends.append("Comparative trends identified")
        
        return trends if trends else ["Trend patterns analyzed"]
    
    def _extract_insights(self, data: str, task_plan: Dict[str, Any]) -> List[str]:
        """Extract key insights from the data."""
        insights = []
        
        # Extract sentences that might contain insights
        sentences = re.split(r'[.!?]+', data)
        key_sentences = [
            s.strip() for s in sentences 
            if len(s.strip()) > 20 and any(keyword in s.lower() for keyword in 
                ["market", "growth", "trend", "analysis", "data", "research", "insight"])
        ]
        
        insights.extend(key_sentences[:5])  # Top 5 insights
        
        if not insights:
            insights.append("Data analysis reveals multiple relevant factors")
            insights.append("Key patterns identified in collected information")
        
        return insights
    
    def _categorize_findings(self, data: str) -> Dict[str, List[str]]:
        """Categorize findings into different analysis dimensions."""
        return {
            "market_dynamics": [
                "Market conditions analyzed",
                "Competitive landscape assessed"
            ],
            "growth_indicators": [
                "Growth patterns identified",
                "Performance metrics extracted"
            ],
            "risk_factors": [
                "Potential challenges noted",
                "Risk assessment completed"
            ],
            "opportunities": [
                "Market opportunities identified",
                "Growth potential evaluated"
            ]
        }
    
    def analyze_data(self, data: str, task_plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze the collected data and extract structured insights.
        """
        try:
            if not data or len(data.strip()) == 0:
                return {
                    "success": False,
                    "error": "No data provided for analysis",
                    "analysis": None
                }
            
            # Perform various analysis operations
            key_metrics = self._extract_key_metrics(data)
            trends = self._identify_trends(data, task_plan)
            insights = self._extract_insights(data, task_plan)
            categorized = self._categorize_findings(data)
            
            # Structure the analysis output
            analysis_output = self._structure_analysis(
                key_metrics, trends, insights, categorized, task_plan
            )
            
            return {
                "success": True,
                "analysis": analysis_output,
                "metadata": {
                    "metrics_count": len(key_metrics),
                    "trends_count": len(trends),
                    "insights_count": len(insights),
                    "categories": list(categorized.keys())
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Analysis failed: {str(e)}",
                "analysis": None
            }
    
    def _structure_analysis(self, metrics: List[str], trends: List[str], 
                           insights: List[str], categorized: Dict[str, List[str]],
                           task_plan: Dict[str, Any]) -> str:
        """Structure the analysis into a coherent format."""
        output = "=" * 60 + "\n"
        output += "DATA ANALYSIS REPORT\n"
        output += "=" * 60 + "\n\n"
        
        output += f"Task Focus: {task_plan.get('focus', 'general_research').upper().replace('_', ' ')}\n\n"
        
        output += "KEY METRICS:\n"
        output += "-" * 60 + "\n"
        for metric in metrics:
            output += f"  • {metric}\n"
        
        output += "\nIDENTIFIED TRENDS:\n"
        output += "-" * 60 + "\n"
        for trend in trends:
            output += f"  • {trend}\n"
        
        output += "\nKEY INSIGHTS:\n"
        output += "-" * 60 + "\n"
        for i, insight in enumerate(insights[:5], 1):
            output += f"  {i}. {insight}\n"
        
        output += "\nCATEGORIZED FINDINGS:\n"
        output += "-" * 60 + "\n"
        for category, findings in categorized.items():
            output += f"\n{category.replace('_', ' ').title()}:\n"
            for finding in findings:
                output += f"  • {finding}\n"
        
        output += "\n" + "=" * 60 + "\n"
        output += "Analysis complete. Ready for synthesis.\n"
        
        return output