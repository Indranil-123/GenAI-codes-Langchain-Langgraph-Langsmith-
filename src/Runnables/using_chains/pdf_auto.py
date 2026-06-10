from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Vector store
vector_store = FAISS.from_documents(docs, OpenAIEmbeddings())
retriever = vector_store.as_retriever()

# LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Prompt
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the context below:

Context:
{context}

Question:
{input}
""")

chain = (
    {
        "context": retriever,
        "input": lambda x: x["input"]
    }
    | prompt
    | llm
)


response = chain.invoke({"input": "Summarize this PDF"})

print(response.content)