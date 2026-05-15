# Article Summarizer

## What it does
Takes a URL as input, fetches the article content from the page, and uses the Groq API to generate a concise summary. Works best with Wikipedia articles, but can fall back to summarizing any webpage.

## How to set it up
1. Make sure you have **Python 3.8 or higher** installed. Check your version with:
   ```
   python --version
   ```
2. Install the required dependencies:
   ```
   pip install requests beautifulsoup4 groq python-dotenv
   ```
2. Create a `.env` file in the same directory with your Groq API key:
   ```
   GROQ_API_KEY=your_key_here
   ```

## How to use it
Run the script from the terminal with a URL as the argument:
```
python summarizer.py <url>
```

Example:
```
python summarizer.py https://en.wikipedia.org/wiki/Python_(programming_language)
```

## Tech used
- [Groq API](https://groq.com/) — LLM inference for generating summaries (model: `llama-3.3-70b-versatile`)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing to extract article text
- [Requests](https://requests.readthedocs.io/) — Fetching webpage content
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Loading the API key from a `.env` file
