from mcp.server.fastmcp import FastMCP
import feedparser
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import os  

# Create MCP server
mcp = FastMCP("ai-innovation")

# === TOOL 1: Fetch RSS ===
@mcp.tool()
def fetch_rss(url: str):
    """Fetch articles from an RSS feed (title, summary, link)."""
    feed = feedparser.parse(url)
    results = []
    for entry in feed.entries[:10]:
        results.append({
            "title": entry.title,
            "summary": getattr(entry, "summary", ""),
            "link": entry.link,
        })
    return results

# === TOOL 2: Fetch raw webpage text ===
@mcp.tool()
def fetch_text(url: str):
    """Fetch text content from a webpage."""
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.get_text(separator="\n")

# === TOOL 3: Save agent configuration ===
@mcp.tool()
def save_agent(name: str, config: dict):
    """Save an agent configuration to the repository."""
    # Create agents directory if it doesn't exist
    agents_dir = Path(__file__).parent / "agents"
    agents_dir.mkdir(exist_ok=True)
    
    # Save agent configuration as JSON
    agent_file = agents_dir / f"{name}.json"
    with open(agent_file, "w") as f:
      json.dump(config, f, indent=2)
    
    return {
      "status": "saved",
      "name": name,
      "path": str(agent_file),
      "config": config
    }

# === TOOL 4: Perplexity-powered AI news / LinkedIn-style search ===
@mcp.tool()
def search_ai_news(query: str, model: str = "sonar-pro"):
    """
    Use Perplexity API to search for recent AI news, influencer posts,
    or LinkedIn-style insights. Returns answer + citations.
    """
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        return {"error": "PERPLEXITY_API_KEY is missing in environment variables."}

    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"Search and summarize the following with citations: {query}"
            }
        ],
        "max_tokens": 1200
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    data = response.json()

    return {
        "query": query,
        "answer": data.get("choices", [{}])[0]
                 .get("message", {})
                 .get("content", ""),
        "citations": data.get("citations", [])
    }

# === START SERVER ===
if __name__ == "__main__":
    mcp.run()


