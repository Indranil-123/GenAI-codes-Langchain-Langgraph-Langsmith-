from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv


load_dotenv()

#document loadinf
loader = TextLoader('docs.txt')
documents = loader.load()


#text splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)


#vectorization
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)


#retriever
retriever = vector_store.as_retriever()

#query
query = "what is the full form of NLP according to the document?"
retrieved_docs = retriever.invoke(query)


#context
context = "\n\n".join([doc.page_content for doc in retrieved_docs])


#LLM
llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0.7)

#prompt
prompt = f"""Answer the question based only on the context below.
{context}
Question: {query}
Answer: """

response = llm.invoke(prompt)
print(response.content)