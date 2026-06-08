from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()


moel = ChatOpenAI()
parser = StrOutputParser()

facts_prompt = PromptTemplate(
    template="Give 2 interesting facts about {topic}",
    input_variables=["topic"]
)

# Prompt 2: Summary
summary_prompt = PromptTemplate(
    template="Give a short 2-line summary about {topic}",
    input_variables=["topic"]
)


fact_chain = facts_prompt | moel | parser
summary_chain = summary_prompt | moel | parser

parallel_chain = RunnableParallel(
    facts = fact_chain,
    summary = summary_chain
)

result = parallel_chain.invoke({'topic': "the moon"})
print(result)