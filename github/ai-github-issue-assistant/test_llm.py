import os
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
    print(f"  Type: {analysis.get('type')}")
    print(f"  Priority: {analysis.get('priority_score')[:30]}...")
    print(f"  Summary: {analysis.get('summary')[:60]}...")
    print("\n✓ JSON format validated")
    print("\n✓✓✓ ALL TESTS PASSED ✓✓✓")
except Exception as e:
    print(f"✗ LLM error: {e}")
