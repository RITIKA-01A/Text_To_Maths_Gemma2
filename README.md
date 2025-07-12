# 🧮 Text to Math Problem Solver Using Google Gemma 2

A Streamlit-based AI assistant that can solve math problems, explain them step-by-step, and answer reasoning or factual questions using a combination of:

- [Google Gemma 2](https://ai.google.dev/gemma)
- LangChain agents and tools
- Wikipedia search
- Mathematical expression solver (`LLMMathChain`)

---

## 🔧 Features

- ✅ Accepts **textual math problems** and gives **step-by-step logical answers**
- ✅ Uses **LLM reasoning** to break down complex questions
- ✅ Automatically detects and uses math tools or Wikipedia search
- ✅ Displays interaction in a **chat-like interface**
- ✅ Powered by **Google Gemma 2** via [Groq API](https://groq.com/)

---


## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Langchain-Groq](https://pypi.org/project/langchain-groq/)
- [SymPy-based Math Tool](https://python.langchain.com/docs/integrations/tools/llm_math/)
- [Wikipedia API Wrapper](https://python.langchain.com/docs/integrations/tools/wikipedia/)
- [Google Gemma 2 LLM (via Groq)](https://groq.com/)

---

## 🧪 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/RITIKA-01A/Text_To_Maths_Gemma2
cd text-to-math-gemma2
```
### 2.Create a virtual environment and activate it
# Using conda
```
conda create -n mathsolver python=3.10
conda activate mathsolver
```

# OR using venv
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## 3. Install dependencies
```
pip install -r requirements.txt
```
## 4. Create a .env file (optional)
```
GROQ_API_KEY=your_groq_api_key
```
## 5. Run the Streamlit app
```
streamlit run app.py
```
