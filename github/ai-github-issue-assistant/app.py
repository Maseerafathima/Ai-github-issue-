import streamlit as st
import json
from src.github_handler import GitHubHandler
from src.llm_analyzer import LLMAnalyzer
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI GitHub Issue Assistant", layout="wide")

st.title("🤖 AI GitHub Issue Assistant")
st.markdown("Analyze GitHub issues using AI-powered insights")

# Check API key configuration
openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()

# Determine if we should try real API
if openai_api_key and openai_api_key.startswith("sk-"):
    st.success("✅ **Real OpenAI API Connected** - Using gpt-3.5-turbo for accurate analysis", icon="🚀")
    use_demo_mode = False
elif openai_api_key:
    st.warning("⚠️  Invalid API key format detected. Using Demo Mode instead.", icon="⚠️")
    use_demo_mode = True
else:
    st.info("ℹ️  **Demo Mode Active** - No API key. Get one at https://platform.openai.com/api-keys", icon="🎯")
    use_demo_mode = True

# Sidebar for inputs
with st.sidebar:
    st.header("Configuration")
    repo_url = st.text_input(
        "GitHub Repository URL",
        placeholder="https://github.com/owner/repo",
        help="Public GitHub repository URL"
    )
    issue_number = st.number_input(
        "Issue Number",
        min_value=1,
        step=1,
        help="The issue number to analyze"
    )

# Main content area
col1, col2 = st.columns([1, 1])

if repo_url and issue_number:
    if st.sidebar.button("🔍 Analyze Issue", use_container_width=True):
        try:
            with st.spinner("Fetching issue from GitHub..."):
                gh = GitHubHandler()
                issue_data = gh.fetch_complete_issue(repo_url, int(issue_number))
            
            with col1:
                st.subheader("📋 Issue Details")
                st.write(f"**Title:** {issue_data['title']}")
                st.write(f"**State:** {issue_data['state']}")
                st.write(f"**Labels:** {', '.join(issue_data['labels']) if issue_data['labels'] else 'None'}")
                
                with st.expander("Full Issue Body"):
                    st.write(issue_data['body'] if issue_data['body'] else "No description provided")
                
                if issue_data['comments']:
                    with st.expander(f"Comments ({len(issue_data['comments'])})"):
                        for i, comment in enumerate(issue_data['comments'], 1):
                            st.write(f"**Comment {i}** - by {comment.get('user', 'Unknown')}")
                            st.write(comment['body'])
                            st.divider()
            
            with col2:
                st.subheader("🤖 AI Analysis")
                with st.spinner("Analyzing with AI..."):
                    analyzer = LLMAnalyzer(api_key=openai_api_key or None, use_demo=use_demo_mode)
                    analysis = analyzer.analyze_issue(issue_data)
                
                # Display analysis
                st.json(analysis)
                
                # Copy button
                json_str = json.dumps(analysis, indent=2)
                st.download_button(
                    label="📋 Copy JSON",
                    data=json_str,
                    file_name=f"analysis_{issue_number}.json",
                    mime="application/json"
                )
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
else:
    st.info("👈 Enter a GitHub repository URL and issue number in the sidebar to get started")

st.divider()
st.markdown("""
### How to use:
1. Enter a public GitHub repository URL (e.g., https://github.com/owner/repo)
2. Enter the issue number
3. Click "Analyze Issue"
4. View the AI analysis and download as JSON
""")
