from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()


#document loader
loader = PyPDFLoader('pdfs.pdf')
documents = loader.load()


#text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

#vectorization
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)


#retriever
retriever = vector_store.as_retriever()

llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0.7)

#query
query = "Summarize the document"

retrieved_docs = retriever.invoke(query)
context = "\n\n".join([doc.page_content for doc in retrieved_docs])

prompt = f"Answer based on context:\n{context}\n\nQuestion: {query}"

response = llm.invoke(prompt)
print(response.content)