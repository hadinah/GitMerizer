from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import requests
import google.generativeai as genai
from collections import defaultdict

app = Flask(__name__)
genai.configure(api_key="AIzaSyBNfWzgEc_NB9A1Ke81wGpPUltLOArXfnM")

model = genai.GenerativeModel(
    model_name='gemini-2.0-flash',
    system_instruction = """
You are a Markdown writer that generates beautifully styled summaries of GitHub activity. 
Write summaries using **Markdown syntax** for full compatibility with `marked.js`. 

🟢 Every summary should:
- Start with the **repository name(owner/repo) as a bold `##` header**
- Use **paragraphs** with `**bold**`, `_italic_`, and `code` formatting to highlight details
- Format repo events naturally as storytelling, avoiding plain lists
- Include markdown features like `**bold**, _italic_, [links](https://github.com), and \`inline code\`` wherever it adds clarity
- Avoid generic headers like "Here's the summary" — just start with the content

The output must be fully styled Markdown ready for rendering using `marked.js`.
Do NOT use HTML tags. Only pure Markdown syntax.
"""
)
generation_config = {
    "temperature": 2.0
}

headers = {
    "Accept": "application/vnd.github.v3+json"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    usernames = data.get("usernames", [])
    hours = int(data.get("time_window", 72))
    max_pages = int(data.get("max_pages", 1))
    
    now = datetime.now()
    time_threshold = now - timedelta(hours=hours)
    BASE_URL = "https://api.github.com/users/{}/events/public?page={}"
    
    ai_friendly_report = []
    raw_map = defaultdict(list)  # repo -> list of raw lines

    for username in usernames:
        for page_no in range(1, max_pages+1):
            response = requests.get(BASE_URL.format(username, page_no), headers=headers)
            if response.status_code != 200:
                continue
            events = response.json()

            for event in events:
                event_time = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                if event_time < time_threshold and hours != 0:
                    break
                repo = event["repo"]["name"]

                if event["type"] == "PushEvent":
                    for commit in event['payload']['commits']:
                        msg = commit.get("message", "").strip()
                        entry = f"{repo}: Commit - {msg}"
                        ai_friendly_report.append(entry)
                        raw_map[repo].append(f"[{username}] Commit: {msg}")

                elif event["type"] == "PullRequestEvent":
                    action = event['payload'].get("action", "unknown")
                    title = event['payload'].get("pull_request", {}).get("title", "").strip()
                    entry = f"{repo}: Pull Request {action} - {title}"
                    ai_friendly_report.append(entry)
                    raw_map[repo].append(f"[{username}] PR {action}: {title}")

                elif event["type"] == "IssuesEvent":
                    action = event['payload'].get("action", "unknown")
                    title = event['payload'].get("issue", {}).get("title", "").strip()
                    entry = f"{repo}: Issue {action} - {title}"
                    ai_friendly_report.append(entry)
                    raw_map[repo].append(f"[{username}] Issue {action}: {title}")

    ai_input = "\n".join(ai_friendly_report)
    try:
        response = model.generate_content(ai_input, generation_config=generation_config)
        return jsonify({
            "success": True,
            "summary": response.text,
            "raw_map": raw_map
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
