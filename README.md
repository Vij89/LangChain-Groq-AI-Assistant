# LangChain Groq AI Assistant

## Project Overview
A terminal-based AI assistant built using Python, LangChain, and the Groq API. It accepts user questions and generates AI-powered responses using a Large Language Model (LLM).

## Technologies Used
- Python
- LangChain
- Groq API
- python-dotenv
- Large Language Models (LLMs)

## Features
- Accepts questions through the terminal.
- Uses `PromptTemplate` to structure prompts.
- Connects to a language model through Groq.
- Uses `StrOutputParser` to return readable text.
- Loads API credentials from environment variables.

## Project Structure
```text
LangChain-Output-Parser/
├── Langchain_AI_Assistant.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## Configuration

Create a local `.env` file containing your Groq API key:

```text
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Never upload your `.env` file or API key to GitHub.

## Run the Project

```bash
python Langchain_AI Assistant.py
```



## Learning Outcomes
- Python environment variables
- LangChain prompt templates
- LLM API integration
- Output parsing
- Generative AI application development

## Future Enhancements
- Continuous conversation support
- Document question-answering
- AI-powered project report summarization
- Chatbot interface
