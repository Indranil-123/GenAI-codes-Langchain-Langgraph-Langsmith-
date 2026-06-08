from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

prompt_template = PromptTemplate.from_template(
    "What is the capital of {country}?"
)

prompt = prompt_template.format(country="France")

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.5)

response = llm.invoke(prompt)
print(response)