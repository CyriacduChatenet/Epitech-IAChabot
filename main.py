from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader, CSVLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
chatbot_key = os.getenv("CHATBOT_KEY")
chat = True

def invokeChatbot (user_input) :
    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a journalist."),
    ("user", "{input}")
    ])
    # loader = WebBaseLoader("https://www.bbc.com/sport/football/european-championship/scores-fixtures/2023-11")
    loader = CSVLoader(file_path="results.csv")
    docs = loader.load()
    
    llm = ChatOpenAI(openai_api_key=chatbot_key)
    embeddings = OpenAIEmbeddings(openai_api_key=chatbot_key)
    output_parser = StrOutputParser()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    
    chain = prompt | llm | output_parser
    
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
    
    <context>
    {context}
    </context>
    
    Question: {input}""")
    
    document_chain = create_stuff_documents_chain(llm, prompt)
    
    document_chain.invoke({
        "input": user_input,
        "context": [Document(page_content="this is only only on top14's teams and match results. To win the championship, you have to be win the final match.")]
    })
    
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    response = retrieval_chain.invoke({"input": user_input})
    print(response["answer"])

while chat == True :
    user_input = input("Enter your question: ")
    if user_input == "exit":
        chat = False
    else:
        invokeChatbot(user_input)