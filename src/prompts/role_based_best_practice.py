from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()



prompt = ChatPromptTemplate.from_messages(
    ("system","You are a strict teacher. Explain answers step by step."),
    ("human","what is the capital of {country} ?")
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

formatted_prompt = prompt.format(country="France")


response = llm.invoke(formatted_prompt)

print(response.content)