# AI Research Agent

A portfolio-ready AI agent built with Python, Streamlit, and the OpenAI API. It can decide when to use tools, search the web, perform calculations, and synthesize a sourced response.

## Features

- **Tool calling:** the model chooses tools based on the user request.
- **Web research:** searches the web and provides result URLs.
- **Calculator:** evaluates basic arithmetic without using `eval()`.
- **Agent loop:** executes tool calls, feeds results back to the model, and generates a final answer.
- **Streamlit UI:** chat interface with an expandable activity trace.
- **Configurable model:** set the model in the sidebar or `.env`.

## Architecture

```text
User
 |
 v
Streamlit UI
 |
 v
ResearchAgent -----> OpenAI model
 |                       |
 |<---- tool decision ---|
 |
 +---- web_search -----> DuckDuckGo
 |
 +---- calculator -----> Safe arithmetic evaluator
 |
 v
Tool results returned to model
 |
 v
Final answer + source URLs
```

## Setup (Windows)

1. Install Python 3.10 or newer.
2. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-research-agent.git
   cd ai-research-agent
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\\Scripts\\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create your environment file:

   ```bash
   copy .env.example .env
   ```

6. Open `.env` and add your API key. Never commit `.env` or expose your API key.

7. Start the app:

   ```bash
   streamlit run app.py
   ```

## Example prompts

- Research the latest developments in retrieval-augmented generation and summarize three useful sources.
- Compare supervised learning and reinforcement learning with practical examples.
- Calculate the compound growth of 15000 at 8% annually for 5 years.
- Find recent sources about AI agents in healthcare and summarize the main opportunities and risks.

## Project structure

```text
ai-research-agent/
├── app.py
├── agent.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Push to GitHub

Create an empty repository on GitHub, then run:

```bash
git init
git add .
git commit -m "Build AI research agent"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-research-agent.git
git push -u origin main
```

## Security notes

- Keep API keys in `.env`; `.gitignore` excludes it.
- If a key is accidentally committed, revoke it immediately and create a new one.
- Treat web pages and search snippets as untrusted input.
- This is a learning/portfolio project, not a verified fact-checking system.

## Future improvements

- Add PDF/document question answering with embeddings and a vector database.
- Add conversation memory.
- Add tests and structured logging.
- Add a source-quality/ranking layer.
- Deploy on Streamlit Community Cloud with secrets configured in the platform settings.

## Tech stack

Python · OpenAI API · Tool Calling · DuckDuckGo Search · Streamlit · python-dotenv
