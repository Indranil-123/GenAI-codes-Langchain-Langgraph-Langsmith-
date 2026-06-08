from src.config.llm_build import get_llm

model =get_llm()

response = model.invoke("Hello, how are you?")
print(response)