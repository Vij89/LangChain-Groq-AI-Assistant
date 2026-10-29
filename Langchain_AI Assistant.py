

import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
env_path = Path(
    r"D:\EXCELR OFFLINE\Python\LangChain_Project\.env"
)
load_dotenv(env_path, override=True)

token = os.getenv("GROQ_API_KEY")
if not token:
    raise ValueError(
        "GROQ_API_KEY is missing from your .env file."
    )

model_id = os.getenv(
    "GROQ_MODEL", "openai/gpt-oss-120b"
)

llm = ChatGroq(
    model=model_id,
    api_key=token,
    temperature=0.5,
    max_tokens=128,
)

template = """You are a helpful AI assistant.
Answer the following question clearly and simply.

Question: {question}

Answer:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["question"]
)


llm_chain = prompt | llm | StrOutputParser()


def main():
    print("=== Groq + LangChain Assistant ===")

    question = input(
        "What would you like to ask? "
    ).strip()

    if not question:
        question = "What is the capital of England?"

    try:
        answer = llm_chain.invoke(
            {"question": question}
        )
        print("\nAI Answer:", answer)

    except Exception as error:
        print("\nRequest failed:", repr(error))


if __name__ == "__main__":
    main()
