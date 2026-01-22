# AI GitHub Issue Assistant

Analyze GitHub issues using AI-powered insights. This tool automatically fetches issue details, comments, and metadata, then generates intelligent analysis including summaries, priority scores, suggested labels, and impact assessments.

**⚡ NEW: Demo Mode - No API key required!** Get started immediately with realistic simulated AI analysis.

## Features

- 🔍 **Automatic Issue Fetching**: Retrieve issue details and comments directly from GitHub
- 🤖 **AI-Powered Analysis**: Uses OpenAI GPT-3.5 for intelligent issue classification (or demo mode)
- 📊 **Structured Output**: Returns analysis in strict JSON format
- 💾 **Easy Export**: Download analysis results as JSON
- 🎨 **Clean UI**: User-friendly Streamlit interface
- ⚡ **Fast Processing**: Efficient caching and API handling
- 🎯 **Demo Mode**: Test everything without API keys!

## Quick Start (2 Minutes)

### Option 1: Demo Mode (Recommended First)
```bash
# No setup needed! Just run:
streamlit run app.py

# Open http://localhost:8501
# Enter any GitHub repo URL and issue number
# Click "Analyze Issue" - works immediately!
```

### Option 2: Real OpenAI Mode
```bash
# Get API key from https://platform.openai.com/api-keys
# Add to .env file: OPENAI_API_KEY=sk-...
# Run: streamlit run app.py
```

See [DEMO_MODE.md](DEMO_MODE.md) for detailed demo mode guide.

## Analysis Output

The AI generates a structured JSON response:

```json
{
  "summary": "One sentence summary of the issue",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "1-5 with short justification",
  "suggested_labels": ["label1", "label2", "label3"],
  "potential_impact": "Short impact statement if bug"
}
```

## Installation

### Prerequisites
- Python 3.9+
- pip package manager

### Step 1: Clone Repository
```bash
git clone https://github.com/gousi/ai-github-issue-assistant.git
cd ai-github-issue-assistant
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Environment Variables (Optional - Demo Mode Works Without This!)
Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
GITHUB_TOKEN=your_github_token_here (optional, for higher rate limits)
```

### Getting API Keys

**OpenAI API Key (Pay-As-You-Go):**

1. Go to: https://platform.openai.com/api-keys
2. Sign in with your OpenAI account
   - Don't have one? [Sign up here](https://platform.openai.com/signup) (takes 2 minutes)
3. Click **"Create new secret key"**
4. Name it (e.g., "GitHub Issue Assistant")
5. Click **"Create secret key"**
6. Copy the key (you'll only see it once!)
7. Open `.env` file in the project folder
8. Paste the key: `OPENAI_API_KEY=sk_test_...`
9. Save the file
10. Restart the app

**Pricing:**
- GPT-3.5-turbo: $0.0005 per 1K input tokens
- ~1,000 issues = ~$0.50
- Free trial credits available for new accounts
- Set usage limits in OpenAI dashboard

**GitHub Token (Optional - Higher Rate Limits):**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Name it: `ai-github-assistant`
4. Select scope: `public_repo`
5. Click "Generate token"
6. Copy the token
7. Add to `.env`: `GITHUB_TOKEN=ghp_...`

## How to Run

### Local Development
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Usage

1. **Enter Repository URL**: Paste a public GitHub repository URL
   - Example: `https://github.com/torvalds/linux`

2. **Enter Issue Number**: Specify the issue number to analyze
   - Example: `12345`

3. **Click "Analyze Issue"**: Wait for the AI to process
   - GitHub API fetches the issue data
   - AI analyzes the content
   - Results display in JSON format

4. **Download Results**: Click "Copy JSON" to export analysis

## Example Usage

Analyzing a real GitHub issue:
- Repository: `https://github.com/facebook/react`
- Issue: `25000`
- Output:
```json
{
  "summary": "Performance degradation in React.memo with large prop objects",
  "type": "bug",
  "priority_score": "4/5 - Affects component performance across many applications",
  "suggested_labels": ["performance", "react.memo", "bug", "high-priority"],
  "potential_impact": "Developers using React.memo with complex props may experience 30-50% slowdown"
}
```

## Project Structure

```
ai-github-issue-assistant/
├── src/
│   ├── github_handler.py    # GitHub API integration
│   └── llm_analyzer.py      # AI analysis engine
├── app.py                   # Streamlit main app
├── requirements.txt         # Python dependencies
├── .env.example             # Environment template
└── README.md               # This file
```

## Edge Cases Handled

✅ Issues with no comments
✅ Large issue content (auto-truncated)
✅ Invalid GitHub URLs
✅ Missing authentication (falls back to unauthenticated requests)
✅ Malformed AI responses (validation & cleanup)

## Error Handling

- **Invalid URL**: Clear error message with correct format
- **Invalid Issue Number**: GitHub API 404 error
- **API Rate Limits**: Graceful fallback with error message
- **Missing API Keys**: Clear instructions to set environment variables
- **Network Issues**: Comprehensive error reporting

## Performance

- First request: ~3-5 seconds (includes GitHub fetch + AI processing)
- Subsequent identical requests: Cached in session
- Handles issues with 100+ comments
- Processes up to 2000 characters of issue body

## Technology Stack

- **Backend & UI**: Streamlit (Python web framework)
- **AI Model**: OpenAI GPT-3.5-turbo (pay-as-you-go)
- **HTTP Client**: requests library + OpenAI Python SDK
- **GitHub API**: REST API v3
- **Environment**: python-dotenv

## Troubleshooting

### "OPENAI_API_KEY not found"
- Check `.env` file exists in project root
- Verify `OPENAI_API_KEY=` is not empty (no spaces around the key)
- Get a free key from https://platform.openai.com/api-keys
- Restart the Streamlit app

### "Invalid API key" error
- Make sure the key starts with `sk_`
- Don't include any extra spaces or characters
- Generate a new key if needed: https://platform.openai.com/api-keys
- Check key hasn't been deactivated in OpenAI dashboard

### "Invalid GitHub URL format"
- Use format: `https://github.com/owner/repo`
- Remove trailing slashes
- Ensure repository is public

### Rate Limit Errors
- Add `GITHUB_TOKEN` to `.env` for higher limits
- Free tier allows 60 requests/hour without token
- With token: 5000 requests/hour
- OpenAI may rate limit on free tier - see usage dashboard

### OpenAI API Errors
- Verify API key is active at https://platform.openai.com/api-keys
- Check you haven't exceeded usage limits
- View billing/usage at https://platform.openai.com/usage
- Try regenerating API key if it's not working

## Limitations

- Requires public GitHub repositories
- Maximum 5 comments displayed in UI (all processed in analysis)
- Issue body limited to 2000 characters for AI processing
- OpenAI rates: Pay-as-you-go ($0.0005 per 1K input tokens)

## Future Enhancements

- Batch analysis of multiple issues
- Custom analysis templates
- Issue metrics dashboard
- Integration with GitHub Actions
- Support for private repositories
- Multiple LLM provider support

## License

MIT License - feel free to use and modify

## Support

For issues and questions, please open an issue on GitHub.

---

**Made with ❤️ for the open-source community**
