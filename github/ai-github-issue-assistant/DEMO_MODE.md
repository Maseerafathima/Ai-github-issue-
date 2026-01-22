# Demo Mode - Use Without API Key

The app now includes **Demo Mode** - you can test everything immediately without any API key!

## ✅ What Works in Demo Mode

- ✅ Analyze real GitHub issues
- ✅ Get realistic AI-powered analysis
- ✅ View all issue details (comments, labels, etc.)
- ✅ Export analysis as JSON
- ✅ Full app functionality

## 🚀 Getting Started (No Setup Needed)

1. **Start the app** (if not already running):
   ```bash
   streamlit run app.py
   ```

2. **Open the browser**: http://localhost:8501

3. **Enter a GitHub repo** (e.g., `https://github.com/facebook/react`)

4. **Enter an issue number** (e.g., `28919`)

5. **Click "Analyze Issue"** - Demo mode will generate realistic AI analysis!

## 💡 How Demo Mode Works

The demo mode intelligently analyzes GitHub issues based on:
- **Keywords** in the title (bug, feature, documentation, etc.)
- **Number of comments** (indicates community interest)
- **Issue content** (determines priority)

It generates realistic analysis that matches the expected format, so you can:
- Test all app features
- Validate your GitHub issues
- Prepare for when you can use real OpenAI

## 🔄 Switching to Real OpenAI

When you can access an OpenAI API key:

1. **Get your API key**:
   - Go to https://platform.openai.com/api-keys
   - Click "Create new secret key"
   - Copy the key

2. **Add to `.env` file**:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

3. **Restart the app**:
   ```bash
   streamlit run app.py
   ```

The app will automatically switch to real OpenAI analysis! The UI will show a green checkmark: ✅ **OpenAI API connected**

## 📊 Example Output (Demo Mode)

```json
{
  "summary": "Bug: Application crashes when uploading large files",
  "type": "bug",
  "priority_score": "5/5 - Critical - Severe issue affecting users",
  "suggested_labels": [
    "bug",
    "needs-investigation",
    "critical"
  ],
  "potential_impact": "Users may experience issues affecting core functionality."
}
```

## 🎯 Tips

- **Free to test**: Demo mode uses no API credits
- **Realistic output**: Analysis matches real AI patterns
- **No limits**: Test as many issues as you want
- **Easy upgrade**: Switch to real AI anytime

## ❓ FAQ

**Q: Will demo mode slow down the app?**  
A: No, demo mode is actually faster (no API calls needed)

**Q: Can I use demo mode forever?**  
A: Yes! But real OpenAI gives more accurate analysis

**Q: Does demo mode require internet?**  
A: No, only the GitHub API call needs internet

**Q: Can I mix demo and real mode?**  
A: Yes, just add your API key to `.env` and restart

---

Enjoy analyzing issues! 🎉
