# 🤖 AI Recommendation Agents Suite

This repository contains two modular AI-powered command-line assistants:

1. 📚 **Book Recommender** – Suggests books based on your interest.
2. 🧠 **LLM Recommender** – Suggests the most suitable large language model (LLM) for your specific use case.

Both agents are powered by the **Phidata Agentic Framework**, **Google Gemini LLM**, and **Pydantic** for input validation.

---

## 📁 Project Structure

    ```bash
    Phi-Data-Agent/
    │
    ├── main.py               # Entry point for Book Recommender
    ├── agent.py              # Book Recommender agent logic
    ├── schema.py             # Book Recommender schemas (Pydantic)
    ├── .env                  # Your API keys (not committed to repo)
    ├── requirements.txt      # Shared dependencies
    ├── README.md             # This file
    │
    └── LLM-Recommender/      # LLM Recommender folder
        ├── main.py           # Entry point for LLM Recommender
        ├── agent.py          # LLM Recommender agent logic
        ├── schema.py         # LLM Recommender schemas (Pydantic)

📚 Project 1: AI Book Recommender
An LLM-based command-line assistant that takes a user’s interest (e.g., psychology, sci-fi, business) and returns 3 book suggestions with descriptions.

    🔥 Features
    ✅ Validates input with Pydantic
    
    🤖 Uses Gemini LLM via Phidata
    
    📘 Returns book title, author, and description
    
    🧩 Clean and modular file structure
    
    ▶️ How to Run
    bash
    Copy
    Edit
    python main.py
💡 Example

📚 Welcome to the AI Book Recommender!
Enter your interest: productivity

🔍 Searching for book recommendations...

✅ Recommended Books:
1. 📖 Deep Work - Cal Newport
2. 📖 Atomic Habits - James Clear
3. 📖 The 7 Habits of Highly Effective People - Stephen Covey
🧠 Project 2: LLM Recommender
This CLI tool asks for your AI use case (e.g., chatbot, code generation, summarization) and suggests which LLM (e.g., GPT-4, Claude, Gemini, Mistral, LLaMA) best fits the task.

🔥 Features
✅ Validates user input using Pydantic

🤖 Uses Google Gemini via Phidata

🧠 Suggests most suitable LLM and why

▶️ How to Run
bash
Copy
Edit
cd LLM-Recommender
python main.py
💡 Example
java
Copy
Edit
🧠 Welcome to the LLM Recommender!
Enter your use case: summarizing long research papers

🔍 Analyzing...

✅ Best Model: Claude 3 Opus
🔎 Reason: Claude excels at long-context reasoning (100k+ tokens).
🔐 Setup Instructions
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/Phi-Data-Agent.git
cd Phi-Data-Agent
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your Gemini API key:

Create a .env file in the root directory:

ini
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key
📦 requirements.txt
nginx
Copy
Edit
phidata
google-generativeai
pydantic
python-dotenv
💡 Future Improvements
🌐 Web version (e.g., Streamlit or Flask)

🗣️ Voice input/output (TTS/STT)

📥 Export recommended items to CSV

🔎 Filtering based on genre, LLM type, pricing, etc.

📌 Disclaimer
This is a student project. Recommendations are generated using AI and may not be fully accurate or suitable. Use your own judgment when making decisions.

🤝 Credits
Phidata Framework

Google Gemini LLM

Pydantic

Python Dotenv

yaml
Copy
Edit
