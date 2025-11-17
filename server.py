from mcp.server.fastmcp import FastMCP
import feedparser
import requests
from bs4 import BeautifulSoup

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

# === START SERVER ===
if __name__ == "__main__":
    mcp.run()

