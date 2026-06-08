from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)


messages = [
    SystemMessage(content="You are a strict teacher. Explain answers step by step."),
    HumanMessage(content="What is the capital of France?")
]

response = llm.invoke(messages)
print(response.content)