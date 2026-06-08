#problem statemen:
#we have reviwes and we need summary and sentiment analysis of the reviews

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated


load_dotenv()


model = ChatOpenAI()

#schema for the output of the model
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review (positive, negative, or neutral)"]


structure_model = model.with_structured_output(Review)

result = structure_model.invoke("The product is great, but the delivery was late.")

print(result)
print(result["sentiment"])
print(result["summary"])

