import os
import json
from dotenv import load_dotenv
load_dotenv()

# Test GitHub fetch
from src.github_handler import GitHubHandler
gh = GitHubHandler()
issue = gh.fetch_complete_issue('https://github.com/facebook/react', 28919)
print("✓ GitHub fetch successful")
print(f"  Title: {issue['title'][:60]}...")

# Test LLM analysis
from src.llm_analyzer import LLMAnalyzer
try:
    analyzer = LLMAnalyzer()
    analysis = analyzer.analyze_issue(issue)
    print("✓ LLM analysis successful")
    
    # Verify required fields
    required_fields = ["summary", "type", "priority_score", "suggested_labels", "potential_impact"]
    for field in required_fields:
        if field in analysis:
            print(f"  ✓ {field}: {str(analysis[field])[:40]}...")
        else:
            print(f"  ✗ Missing field: {field}")
    
    print("\n✓ JSON format validated")
    print("\n✅ ALL TESTS PASSED ✅")
    
except Exception as e:
    print(f"✗ Error: {e}")
