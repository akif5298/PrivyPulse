#!/usr/bin/env python3
"""
Quick test script to verify Phase 2 implementation.
Run this to quickly test the multi-agent system.
"""

from app.agents.coordinator import run_workflow


def test_basic_query():
    """Test a basic market research query"""
    print("=" * 70)
    print("Testing Phase 2: Multi-Agent Architecture")
    print("=" * 70)
    print()
    
    test_queries = [
        "What are the current trends in artificial intelligence market?",
        "Compare cloud computing services AWS vs Azure",
        "Explain the growth of electric vehicle market"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{'='*70}")
        print(f"Test {i}: {query}")
        print('='*70)
        
        try:
            result = run_workflow(query)
            
            # Check basic structure
            assert "response" in result, "Missing 'response' in result"
            assert "agents_used" in result, "Missing 'agents_used' in result"
            
            print(f"\n✓ Response received")
            print(f"✓ Agents used: {', '.join(result['agents_used'])}")
            
            if result.get("error"):
                print(f"⚠ Error: {result.get('error_agent')}")
                print(f"  {result['response']}")
            else:
                print(f"✓ Task focus: {result.get('task_plan', {}).get('focus', 'N/A')}")
                if result.get("metadata", {}).get("validation_passed"):
                    print("✓ Validation: PASSED")
                else:
                    print("⚠ Validation: Needs improvement")
                
                # Show first 200 chars of response
                response_preview = result["response"][:200]
                print(f"\nResponse preview:\n{response_preview}...")
            
        except Exception as e:
            print(f"✗ Test failed with error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 70)
    print("Quick test completed!")
    print("=" * 70)


if __name__ == "__main__":
    test_basic_query()
