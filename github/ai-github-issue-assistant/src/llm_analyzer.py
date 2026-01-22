import json
import os
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

# Try to import OpenAI, but allow it to fail for demo mode
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class LLMAnalyzer:
    def __init__(self, api_key: str = None, use_demo: bool = False):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.use_demo = use_demo
        self.api_key_valid = False
        
        if not OPENAI_AVAILABLE:
            raise ValueError("OpenAI SDK not installed. Install with: pip install openai")
        
        # Try to initialize with API key if provided
        if self.api_key and self.api_key.strip():
            try:
                self.client = OpenAI(api_key=self.api_key)
                self.api_key_valid = True
                self.use_demo = False  # Override demo mode if valid key exists
            except Exception as e:
                print(f"⚠️  Invalid API key detected: {str(e)}")
                self.api_key_valid = False
                self.use_demo = True
        else:
            self.use_demo = True

    def analyze_issue(self, issue_data: Dict) -> Dict:
        """Analyze GitHub issue using OpenAI or demo mode"""
        
        if self.use_demo:
            return self._demo_analysis(issue_data)
        
        prompt = self._build_prompt(issue_data)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert GitHub issue analyzer. Return ONLY valid JSON, no markdown formatting."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            text = response.choices[0].message.content.strip()
            
            # Extract JSON from response
            start = text.find('{')
            end = text.rfind('}') + 1
            if start != -1 and end > start:
                json_str = text[start:end]
                result = json.loads(json_str)
                return self._validate_response(result)
            else:
                raise ValueError("No JSON found in response")
                
        except json.JSONDecodeError as e:
            # Fall back to demo mode if JSON parsing fails
            print(f"⚠️  Failed to parse JSON response: {str(e)}. Using demo mode...")
            return self._demo_analysis(issue_data)
        except Exception as e:
            # Fall back to demo mode for any API errors (invalid key, network, etc.)
            error_msg = str(e).lower()
            if "401" in error_msg or "invalid" in error_msg or "api_key" in error_msg or "authentication" in error_msg:
                print(f"⚠️  OpenAI API authentication error: Using demo mode instead...")
                return self._demo_analysis(issue_data)
            # For other errors, still try demo mode as fallback
            print(f"⚠️  LLM error: {str(e)}. Falling back to demo mode...")
            return self._demo_analysis(issue_data)

    def _demo_analysis(self, issue_data: Dict) -> Dict:
        """Generate demo analysis without API key"""
        title = issue_data.get("title", "")
        body = issue_data.get("body", "")
        comments_count = len(issue_data.get("comments", []))
        
        # Analyze title keywords
        title_lower = title.lower()
        
        # Determine type based on keywords
        issue_type = "other"
        if any(word in title_lower for word in ["bug", "error", "fix", "crash", "broken", "fail"]):
            issue_type = "bug"
        elif any(word in title_lower for word in ["feature", "add", "implement", "support", "allow"]):
            issue_type = "feature_request"
        elif any(word in title_lower for word in ["doc", "document", "readme", "guide", "tutorial"]):
            issue_type = "documentation"
        elif any(word in title_lower for word in ["why", "how", "what", "help", "question", "?"]):
            issue_type = "question"
        
        # Determine priority based on content
        priority_score = "2/5 - Low priority"
        if issue_type == "bug":
            if any(word in title_lower for word in ["critical", "severe", "crash", "data loss"]):
                priority_score = "5/5 - Critical - Severe issue affecting users"
            elif comments_count > 5:
                priority_score = "4/5 - High - Multiple users affected"
            else:
                priority_score = "3/5 - Medium - Confirmed bug needs investigation"
        elif issue_type == "feature_request":
            if comments_count > 3:
                priority_score = "3/5 - Medium - Community interest"
            else:
                priority_score = "2/5 - Low - Single feature request"
        
        # Generate labels
        labels = []
        if issue_type == "bug":
            labels.extend(["bug", "needs-investigation"])
            if "performance" in title_lower or "slow" in title_lower:
                labels.append("performance")
            if "memory" in title_lower or "leak" in title_lower:
                labels.append("memory-leak")
        elif issue_type == "feature_request":
            labels.extend(["enhancement", "feature-request"])
        elif issue_type == "documentation":
            labels.extend(["documentation", "good-first-issue"])
        
        # Remove duplicates and limit to 5
        labels = list(set(labels))[:5]
        
        # Generate summary
        summary = title[:100] if len(title) > 0 else "Issue analysis"
        if issue_type == "bug":
            summary = f"Bug: {title[:80]}"
        elif issue_type == "feature_request":
            summary = f"Feature request: {title[:75]}"
        
        # Generate impact
        if issue_type == "bug":
            impact = "Users may experience issues. Reproduction steps needed for verification."
            if "critical" in title_lower or "severe" in title_lower:
                impact = "Critical bug affecting core functionality and users."
        else:
            impact = f"This {issue_type.replace('_', ' ')} has {comments_count} comments indicating community interest."
        
        return {
            "summary": summary[:200],
            "type": issue_type,
            "priority_score": priority_score,
            "suggested_labels": labels,
            "potential_impact": impact[:200]
        }

    def _build_prompt(self, issue_data: Dict) -> str:
        """Build analysis prompt from issue data"""
        title = issue_data.get("title", "")
        body = issue_data.get("body", "")[:2000]  # Limit to 2000 chars
        comments_text = ""
        
        comments = issue_data.get("comments", [])
        if comments:
            comments_text = "\n\nComments:\n"
            for i, comment in enumerate(comments[:5], 1):  # Limit to first 5 comments
                comments_text += f"{i}. {comment.get('body', '')[:500]}\n"
        
        prompt = f"""Analyze this GitHub issue and return ONLY valid JSON (no markdown, no extra text).

Issue Title: {title}

Issue Body: {body}
{comments_text}

Return a JSON object with exactly this structure:
{{
  "summary": "One sentence summary of the issue",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "1-5 with short justification",
  "suggested_labels": ["label1", "label2", "label3"],
  "potential_impact": "Short impact statement if bug, otherwise brief description"
}}

IMPORTANT: Return ONLY the JSON object, no markdown formatting, no extra text."""

        return prompt

    def _validate_response(self, response: Dict) -> Dict:
        """Validate and clean response"""
        required_fields = ["summary", "type", "priority_score", "suggested_labels", "potential_impact"]
        
        for field in required_fields:
            if field not in response:
                response[field] = ""
        
        # Ensure suggested_labels is a list
        if not isinstance(response.get("suggested_labels"), list):
            response["suggested_labels"] = []
        
        # Validate type field
        valid_types = ["bug", "feature_request", "documentation", "question", "other"]
        if response.get("type") not in valid_types:
            response["type"] = "other"
        
        return {
            "summary": str(response.get("summary", ""))[:200],
            "type": response.get("type", "other"),
            "priority_score": str(response.get("priority_score", ""))[:100],
            "suggested_labels": response.get("suggested_labels", [])[:10],
            "potential_impact": str(response.get("potential_impact", ""))[:200],
        }
