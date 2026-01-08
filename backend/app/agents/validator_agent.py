from typing import Dict, Any, List
import re


class ValidatorAgent:
    """
    Validator agent responsible for validating output quality and completeness.
    """
    
    def __init__(self):
        self.min_length = 100
        self.required_sections = [
            "summary", "findings", "insights", "recommendations"
        ]
        self.quality_threshold = 0.6
    
    def _check_completeness(self, content: str, task_plan: Dict[str, Any]) -> Dict[str, Any]:
        """Check if the content is complete and addresses the query."""
        checks = {
            "has_sufficient_length": len(content) >= self.min_length,
            "has_structure": bool(re.search(r'[=|\-]{3,}', content)),  # Has section dividers
            "has_key_sections": self._check_sections(content),
            "addresses_query": self._check_query_relevance(content, task_plan)
        }
        
        passed = sum(checks.values())
        total = len(checks)
        score = passed / total if total > 0 else 0
        
        return {
            "checks": checks,
            "score": score,
            "passed": score >= self.quality_threshold
        }
    
    def _check_sections(self, content: str) -> bool:
        """Check if content has required sections."""
        content_lower = content.lower()
        found_sections = 0
        
        for section in self.required_sections:
            if section in content_lower:
                found_sections += 1
        
        return found_sections >= 2  # At least 2 required sections
    
    def _check_query_relevance(self, content: str, task_plan: Dict[str, Any]) -> bool:
        """Check if content is relevant to the original query."""
        query = task_plan.get("query", "").lower()
        if not query:
            return True  # Can't validate without query
        
        # Extract key terms from query
        query_terms = set(re.findall(r'\b\w{4,}\b', query))  # Words with 4+ chars
        content_lower = content.lower()
        
        # Check if key terms appear in content
        matches = sum(1 for term in query_terms if term in content_lower)
        relevance_score = matches / len(query_terms) if query_terms else 1.0
        
        return relevance_score >= 0.3  # At least 30% of key terms should appear
    
    def _check_quality(self, content: str) -> Dict[str, Any]:
        """Check overall quality of the content."""
        quality_checks = {
            "has_clear_structure": bool(re.search(r'(SUMMARY|FINDINGS|INSIGHTS|RECOMMENDATIONS)', content, re.IGNORECASE)),
            "has_actionable_content": bool(re.search(r'(recommend|suggest|consider|should|may)', content, re.IGNORECASE)),
            "has_data_references": bool(re.search(r'(data|analysis|research|study|finding)', content, re.IGNORECASE)),
            "proper_formatting": content.count('\n') >= 5  # Has reasonable line breaks
        }
        
        passed = sum(quality_checks.values())
        total = len(quality_checks)
        score = passed / total if total > 0 else 0
        
        return {
            "checks": quality_checks,
            "score": score,
            "passed": score >= self.quality_threshold
        }
    
    def _generate_validation_notes(self, completeness: Dict[str, Any], 
                                   quality: Dict[str, Any]) -> List[str]:
        """Generate notes about validation results."""
        notes = []
        
        if completeness["passed"]:
            notes.append("Content completeness: PASSED")
        else:
            notes.append(f"Content completeness: Needs improvement (score: {completeness['score']:.2f})")
        
        if quality["passed"]:
            notes.append("Content quality: PASSED")
        else:
            notes.append(f"Content quality: Needs improvement (score: {quality['score']:.2f})")
        
        # Add specific feedback
        if not completeness["checks"].get("has_sufficient_length"):
            notes.append("Note: Content could be more detailed")
        
        if not quality["checks"].get("has_actionable_content"):
            notes.append("Note: Could include more actionable recommendations")
        
        return notes
    
    def validate(self, content: str, original_query: str, task_plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate the synthesized content for quality and completeness.
        """
        try:
            if not content or len(content.strip()) == 0:
                return {
                    "success": False,
                    "passed": False,
                    "error": "No content provided for validation",
                    "validated_content": None,
                    "notes": ["Validation failed: Empty content"]
                }
            
            # Perform validation checks
            completeness = self._check_completeness(content, task_plan)
            quality = self._check_quality(content)
            
            # Overall validation result
            overall_passed = completeness["passed"] and quality["passed"]
            
            # Generate validation notes
            notes = self._generate_validation_notes(completeness, quality)
            
            # If validation passed, return content as-is
            # If validation failed but content exists, still return it with warnings
            validated_content = content
            if not overall_passed:
                validated_content = self._enhance_content(content, completeness, quality, task_plan)
                notes.append("Content enhanced based on validation feedback")
            
            return {
                "success": True,
                "passed": overall_passed,
                "validated_content": validated_content,
                "notes": notes,
                "scores": {
                    "completeness": completeness["score"],
                    "quality": quality["score"],
                    "overall": (completeness["score"] + quality["score"]) / 2
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "passed": False,
                "error": f"Validation failed: {str(e)}",
                "validated_content": content,  # Return original content even on error
                "notes": [f"Validation error: {str(e)}"]
            }
    
    def _enhance_content(self, content: str, completeness: Dict[str, Any],
                         quality: Dict[str, Any], task_plan: Dict[str, Any]) -> str:
        """Enhance content based on validation feedback."""
        enhanced = content
        
        # Add note if content is too short
        if not completeness["checks"].get("has_sufficient_length"):
            enhanced += "\n\n[Note: Additional details may be available upon request]"
        
        # Ensure query relevance
        if not completeness["checks"].get("addresses_query"):
            query = task_plan.get("query", "")
            if query:
                enhanced = f"Analysis for: {query}\n\n" + enhanced
        
        return enhanced