from typing import Dict, Any, List
import re


class SynthesisAgent:
    """
    Synthesis agent responsible for synthesizing analyzed data into coherent insights.
    """
    
    def __init__(self):
        self.synthesis_structure = [
            "executive_summary",
            "key_findings",
            "implications",
            "recommendations"
        ]
    
    def _extract_executive_summary(self, analysis: str, task_plan: Dict[str, Any]) -> str:
        """Create an executive summary from the analysis."""
        focus = task_plan.get("focus", "general_research")
        
        # Extract key sentences for summary
        sentences = re.split(r'[.!?]+', analysis)
        key_sentences = [
            s.strip() for s in sentences 
            if len(s.strip()) > 30 and len(s.strip()) < 200
        ]
        
        if key_sentences:
            summary = key_sentences[0]
            if len(key_sentences) > 1:
                summary += ". " + key_sentences[1]
        else:
            summary = f"Comprehensive analysis completed for {task_plan.get('query', 'the query')}. "
            summary += "Multiple data points and insights have been identified and evaluated."
        
        return summary
    
    def _extract_key_findings(self, analysis: str) -> List[str]:
        """Extract key findings from the analysis."""
        findings = []
        
        # Look for bullet points and numbered items
        bullet_pattern = r'[•\-\*]\s*(.+?)(?=\n|$)'
        numbered_pattern = r'\d+\.\s*(.+?)(?=\n|$)'
        
        bullets = re.findall(bullet_pattern, analysis)
        numbered = re.findall(numbered_pattern, analysis)
        
        findings.extend([b.strip() for b in bullets[:5]])
        findings.extend([n.strip() for n in numbered[:5]])
        
        # If no structured findings, extract key sentences
        if not findings:
            sentences = re.split(r'[.!?]+', analysis)
            key_sentences = [
                s.strip() for s in sentences 
                if len(s.strip()) > 40 and any(keyword in s.lower() for keyword in 
                    ["trend", "growth", "market", "analysis", "data", "insight", "finding"])
            ]
            findings = key_sentences[:5]
        
        return findings[:5] if findings else ["Key findings extracted from comprehensive analysis"]
    
    def _derive_implications(self, analysis: str, task_plan: Dict[str, Any]) -> List[str]:
        """Derive implications from the analysis."""
        implications = []
        
        focus = task_plan.get("focus", "general_research")
        
        if focus == "trend_analysis":
            implications.append("Current trends indicate potential future market directions")
            implications.append("Growth patterns suggest opportunities for strategic positioning")
        elif focus == "comparison":
            implications.append("Comparative analysis reveals relative strengths and weaknesses")
            implications.append("Differences identified may inform decision-making")
        else:
            implications.append("Analysis reveals important market dynamics")
            implications.append("Findings have implications for strategic planning")
        
        # Extract context-specific implications
        if "growth" in analysis.lower():
            implications.append("Positive growth indicators suggest favorable market conditions")
        if "risk" in analysis.lower() or "challenge" in analysis.lower():
            implications.append("Identified challenges require careful consideration")
        
        return implications if implications else ["Analysis provides actionable insights"]
    
    def _generate_recommendations(self, analysis: str, task_plan: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on the analysis."""
        recommendations = []
        
        focus = task_plan.get("focus", "general_research")
        
        recommendations.append("Continue monitoring key metrics and trends")
        recommendations.append("Consider further research in identified opportunity areas")
        
        if focus == "trend_analysis":
            recommendations.append("Leverage identified trends for strategic planning")
        elif focus == "comparison":
            recommendations.append("Use comparative insights to inform competitive strategy")
        
        return recommendations
    
    def synthesize(self, analysis: str, task_plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Synthesize analyzed data into coherent, actionable insights.
        """
        try:
            if not analysis or len(analysis.strip()) == 0:
                return {
                    "success": False,
                    "error": "No analysis provided for synthesis",
                    "synthesis": None
                }
            
            # Extract different components
            executive_summary = self._extract_executive_summary(analysis, task_plan)
            key_findings = self._extract_key_findings(analysis)
            implications = self._derive_implications(analysis, task_plan)
            recommendations = self._generate_recommendations(analysis, task_plan)
            
            # Structure the synthesis
            synthesis_output = self._structure_synthesis(
                executive_summary, key_findings, implications, recommendations, task_plan
            )
            
            return {
                "success": True,
                "synthesis": synthesis_output,
                "metadata": {
                    "findings_count": len(key_findings),
                    "implications_count": len(implications),
                    "recommendations_count": len(recommendations)
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Synthesis failed: {str(e)}",
                "synthesis": None
            }
    
    def _structure_synthesis(self, summary: str, findings: List[str], 
                            implications: List[str], recommendations: List[str],
                            task_plan: Dict[str, Any]) -> str:
        """Structure the synthesis into a coherent, readable format."""
        output = "\n" + "=" * 70 + "\n"
        output += "SYNTHESIZED INSIGHTS\n"
        output += "=" * 70 + "\n\n"
        
        output += "EXECUTIVE SUMMARY\n"
        output += "-" * 70 + "\n"
        output += f"{summary}\n\n"
        
        output += "KEY FINDINGS\n"
        output += "-" * 70 + "\n"
        for i, finding in enumerate(findings, 1):
            output += f"{i}. {finding}\n"
        
        output += "\nIMPLICATIONS\n"
        output += "-" * 70 + "\n"
        for i, implication in enumerate(implications, 1):
            output += f"{i}. {implication}\n"
        
        output += "\nRECOMMENDATIONS\n"
        output += "-" * 70 + "\n"
        for i, recommendation in enumerate(recommendations, 1):
            output += f"{i}. {recommendation}\n"
        
        output += "\n" + "=" * 70 + "\n"
        output += "Synthesis complete. Ready for validation.\n"
        
        return output