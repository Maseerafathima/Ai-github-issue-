# START HERE - Get Your OpenAI API Key

## 🚀 Quick Setup (3 Minutes)

### Step 1: Visit OpenAI Platform
**Open in browser:** https://platform.openai.com/api-keys

### Step 2: Sign In or Create Account
- Click "Sign in" (or "Sign up" if new)
- Use your email address
- Verify your email if prompted
- (New accounts get free trial credits!)

### Step 3: Create API Key
- Go to: https://platform.openai.com/api-keys (if not already there)
- Click **"Create new secret key"**
- Give it a name (e.g., "GitHub Issue Assistant")
- Click **"Create secret key"**

### Step 4: Copy Your Key
- Your key appears (like: `sk_test_4eC...`)
- **Important**: You'll only see it once! Copy it now!
- Click the copy button or highlight and copy

### Step 5: Add to .env File
1. Open `.env` file in this project folder
2. Find: `OPENAI_API_KEY=`
3. Paste your key: `OPENAI_API_KEY=sk_test_...`
4. Save the file

### Example:
```
OPENAI_API_KEY=sk_test_4eC39HqLyjWDarhtT1ZdV7dc
GITHUB_TOKEN=
```

### Step 6: Run the App!
- **Windows**: Double-click `start.bat`
- **Mac/Linux**: Run `streamlit run app.py`
- App opens at: http://localhost:8501

---

## Done! 🎉

Your app is now ready to analyze GitHub issues!

### Using the App:
1. Enter GitHub URL: `https://github.com/owner/repo`
2. Enter issue number
3. Click "Analyze Issue"
4. View AI analysis
5. Download JSON results

---

## Pricing & Credits

**Cost:**
- Typically $0.0005 per analysis
- 100 issues = ~$0.05
- New accounts get free trial credits

**Setting Usage Limits:**
1. Go to: https://platform.openai.com/usage
2. Click "Billing" in sidebar
3. Set a monthly limit if desired

---

## Troubleshooting

**"OPENAI_API_KEY is missing" error?**
- Make sure `.env` file exists
- Check you pasted the key correctly
- No spaces before/after the key
- Restart the app

**"Invalid API key" error?**
- Make sure key starts with `sk_`
- Don't include spaces or quotes
- Regenerate a new key if needed
- Check key hasn't been deactivated

**Can't find the API keys page?**
- Direct link: https://platform.openai.com/api-keys
- Or: https://platform.openai.com → Click your account → "API keys"

**Need to check usage?**
- https://platform.openai.com/usage
- Shows cost per day
- Set spending limits there

---

## Key Points ✅

- OpenAI account is free to create
- New accounts get trial credits
- No credit card required initially
- Pay only for what you use
- 30-day credit expiration
- Easy to add payment method later

---

**Ready? Get your API key and run `start.bat`!**
