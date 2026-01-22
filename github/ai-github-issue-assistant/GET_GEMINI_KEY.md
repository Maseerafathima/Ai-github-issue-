# Get Your Free Gemini API Key

## Step-by-Step Instructions (2 minutes)

### 1. Open Google AI Studio
- Go to: **https://ai.google.dev/**

### 2. Click "Get API Key"
- Look for the "Get API Key" button in the top right corner
- Click it

### 3. Sign In (if needed)
- Sign in with your Google account
- Create a free Google account if you don't have one (also free)

### 4. Create API Key
- Click **"Create API Key"**
- Choose **"Create API key in a new Google Cloud project"**
- Click **"Create API key"** button
- Your API key will appear (it looks like: `AIzaSy...`)

### 5. Copy Your Key
- Click the copy button next to your API key
- The key is now in your clipboard

### 6. Add to .env File
- Open the `.env` file in this project folder
- Find the line: `GEMINI_API_KEY=`
- Paste your key after the `=` sign
- Save the file

### Example:
```
GEMINI_API_KEY=AIzaSyDscJqF9kNJ-QjgwZZ-Zz4Zn7pZ8h1kL2M
GITHUB_TOKEN=
```

### 7. Restart the App
- Close and restart the Streamlit app
- Go to http://localhost:8501
- Start analyzing issues!

## Free Tier Details

✅ Completely free
✅ No credit card required
✅ 15 requests per minute
✅ 1 million requests per day

## Troubleshooting

**"API key not valid" error:**
- Double-check your key is copied correctly
- Make sure there are no extra spaces
- Generate a new key at https://ai.google.dev/

**Can't find "Get API Key" button:**
- You might already be logged in
- Go directly to: https://aistudio.google.com/app/apikey
- If not, start at https://ai.google.dev/ and look for the button

**Still not working:**
- Clear your browser cache
- Try a different browser
- Create a new Google account and try again

---

**Questions?** Check the README.md for full documentation.
