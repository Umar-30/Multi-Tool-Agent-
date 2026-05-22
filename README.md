---
title: Multi Tool Ai Agent
emoji: 🦾
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.31.0
app_file: app.py
pinned: false
---

# 🤖 Multi-Tool AI Agent

A sophisticated, asynchronous AI agent built with Python, Cohere, and Streamlit. This agent automates the workflow of searching the web, synthesizing information using advanced AI models, saving results to a local database, and emailing a concise summary to any specified recipient.

## ✨ Features

- **AI-Driven Reasoning:** Uses Cohere's `command-a-03-2025` model to generate optimized search queries and synthesize search results into meaningful summaries.
- **Web Search Integration:** Powered by `duckduckgo-search` to fetch real-time information from the web.
- **Automated Emailing:** Sends AI-generated summaries via Gmail SMTP using `aiosmtplib` for non-blocking operations.
- **Local Persistence:** Saves every search and result into an SQLite database (`agent.db`) using `aiosqlite`.
- **Modern UI:** A sleek, GitHub-inspired **Dark Mode** interface built with Streamlit.
- **History Dashboard:** View, clear, and interact with your past search history directly from the sidebar.

## 🛠️ Tech Stack

- **Language:** Python 3.14+
- **AI Model:** Cohere API
- **UI Framework:** Streamlit
- **Package Manager:** [uv](https://github.com/astral-sh/uv)
- **Database:** SQLite (Async)
- **Email:** SMTP (Async)

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have `uv` installed. If not, install it via:
```powershell
pip install uv
```

### 2. Clone the Repository
```bash
git clone <your-repo-url>
cd Multi-Tool-Agent
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory and add your credentials:
```env
COHERE_API_KEY="your_cohere_api_key"
EMAIL_USER="your_gmail_address@gmail.com"
EMAIL_PASSWORD="your_app_password" # 16-character Google App Password
```

### 4. Install Dependencies
`uv` will automatically handle the environment and dependencies:
```bash
uv sync
```

## 🖥️ Usage

To launch the Streamlit UI, run the following command:

```powershell
$env:PYTHONPATH = "."; uv run streamlit run app/ui.py
```

1. Enter your search request (e.g., "Latest AI news about OpenAI").
2. Provide the receiver's email address.
3. Click **Run Agent**.
4. Watch the live status as the agent searches, saves, and emails the result!

## 📂 Project Structure

```text
├── app/
│   ├── services/       # Cohere client configuration
│   ├── tools/          # Web search, Email, and Database tools
│   ├── agent.py        # Core agentic logic
│   ├── config.py       # Pydantic settings management
│   ├── main.py         # CLI entry point
│   └── ui.py           # Streamlit Dark UI
├── .env                # Secrets (not committed)
├── agent.db            # SQLite database
├── pyproject.toml      # Project dependencies
└── README.md           # Documentation
```

## 🛡️ Security Note
- Never commit your `.env` file.
- Use **Google App Passwords** instead of your primary Gmail password for the SMTP configuration.

---
Built with ❤️ for AI Automation.
