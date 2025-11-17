# **Innovation Radar — MCP-Powered AI PM Intelligence Agent**  
*A custom Model Context Protocol (MCP) project that automates weekly AI & Product Management research using real data from newsletters + Perplexity search.*

---

## 🚀 Overview  
**Innovation Radar** is an AI agent designed for staying ahead of the curve in **AI, Product Management, and Agentic technology**.  
It uses a custom **MCP server** with real tools to gather verified insights from:

- 🧠 Product thought leaders (Lenny, Paweł, Aakash, Claire, etc.)  
- 🤖 AI/LLM/agent ecosystem news  
- 🛠️ New tools & frameworks  
- 📈 Early signals & emerging trends  

This agent automatically generates a **structured weekly briefing** using only **real data**, fetched through custom tools.

---

## 🔧 Features

### ✔ **RSS-powered newsletter intelligence**
Pulls real posts from Substack / blogs using:

- `fetch_rss(url)`  
- `fetch_text(url)` to extract full article bodies

### ✔ **AI news + LinkedIn-style insights via Perplexity**
Uses your Perplexity API key through:

- `search_ai_news(query)` to fetch recent:
- AI model releases  
- Agent framework updates  
- Influencer commentary  
- LinkedIn-style summaries (legally via LLM search)  

### ✔ **Agent configuration persistence**
- `save_agent(name, config)` saves agent definitions into `/agents`.

### ✔ **Runs locally using MCP + Cursor**
- No cloud, no external hosting.

---

## 🧩 Architecture

### **1. MCP Server (`server.py`)**

The server exposes **4 tools**:

| Tool | Purpose |
|------|---------|
| `fetch_rss(url)` | Fetches RSS entries (title, summary, link) |
| `fetch_text(url)` | Extracts full article text |
| `save_agent(name, config)` | Saves agent config to `/agents` |
| `search_ai_news(query, model)` | Uses Perplexity API for AI + LinkedIn-style search |

All insights the agent uses must come from these tools — no hallucinations.

---

### **2. Agent (`innovation-radar.json`)**

The agent is optimized for **AI PM workflows** and performs:

- RSS pulls (Lenny, Paweł, Aakash, etc.)
- LinkedIn/public insight pulls using Perplexity
- Global AI ecosystem monitoring
- Weekly summaries in strict markdown format

This ensures reliable, skimmable intelligence tailored for PM leadership roles.

---

### **3. MCP Client (`mcp.json`)**

Cursor acts as the MCP client, connecting to the server and enabling:

- Agent execution  
- Tool invocation  
- Local evaluation / exploration  

---

## 🛠️ Running Locally

### **1. Install dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install feedparser beautifulsoup4 requests fastmcp
```

### **2. Set Perplexity API key**
Mac:
```bash
export PERPLEXITY_API_KEY="your_key_here"
```

Zsh users add this to `~/.zshrc`.

### **3. Start the MCP server**
```bash
python server.py
```

### **4. Connect via Cursor**
Cursor → Tools → MCP → “ai-innovation” server should appear.

### **5. Run the agent**
In Cursor chat:
```
Run the Innovation Radar agent now.
```

---

## 🧠 Example Use Cases

- Automated weekly PM research  
- AI ecosystem monitoring  
- Thought-leader intelligence  
- Competitive AI agent analysis  
- Tutorial/tool discovery for PMs  
- Trend prediction / early signal detection  

---

## 🎯 Why This Project Matters (AI PM Perspective)

This project demonstrates end-to-end skills in:

- Agent architecture  
- MCP tooling  
- AI workflow orchestration  
- RSS + LLM integration  
- Agentic research automation  
- Product-grade AI reasoning systems  

It reflects the emerging future of PM work:
**AI-augmented research pipelines and agentic tools enabling deeper, faster strategic awareness.**

---

