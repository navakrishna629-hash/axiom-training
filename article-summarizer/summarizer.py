# summarizer.py
# Usage: python summarizer.py <url>

import sys
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from groq import Groq

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Error: GROQ_API_KEY not found.")
    print("Make sure you have a .env file with GROQ_API_KEY=your_key_here")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: python summarizer.py <url>")
    sys.exit(1)

url = sys.argv[1]


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
try:
    request_response = requests.get(url, headers=headers, timeout=10)

    if request_response.status_code != 200:
        print(f"Error: Could not fetch the article. Status code: {request_response.status_code}")
        sys.exit(1)

except requests.exceptions.MissingSchema:
    print(f"Error: '{url}' is not a valid URL. Make sure it starts with http:// or https://")
    sys.exit(1)

except requests.exceptions.ConnectionError:
    print(f"Error: Could not connect to {url}. Check the URL and your internet connection.")
    sys.exit(1)

except requests.exceptions.Timeout:
    print("Error: The request timed out. The website took too long to respond.")
    sys.exit(1)

html = request_response.text


soup = BeautifulSoup(html, 'html.parser')
main_article = soup.find("div", {"id": "mw-content-text"})
if main_article:
    text = main_article.get_text()
else:
    print("Warning: Could not find main article content, falling back to full page text.")
    text = soup.get_text()

truncated = text[:6000]
text = truncated[:truncated.rfind(' ')] if len(text) > 6000 else truncated

print("Fetching and summarizing article, please wait...")
try:
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Summarize this article:\n\n{text}"}]
    )
    summary = response.choices[0].message.content
    print(summary)
except Exception as e:
    print(f"Error: Groq API request failed: {e}")
    sys.exit(1)