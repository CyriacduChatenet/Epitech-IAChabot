from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader, CSVLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

import warnings

def bot_answer(input):

    warnings.filterwarnings("ignore", category=UserWarning)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a journalist."),
        ("user", "{input}")
    ])

    # Un-comment the line below to be able to scrap the Ligue 1 results and comment the line 25 
    # loader = WebBaseLoader("https://www.lequipe.fr/Football/ligue-1/page-calendrier-resultats")
    loader = CSVLoader(file_path="results.csv")
    docs = loader.load()
    llm = Ollama(model="mistral")
    embeddings = HuggingFaceEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings) 
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)

    document_chain.invoke({
        "input": input,
        "context": [Document(page_content="question's subject are the football results between 1872 and 2023")]
    })

    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": input})

    return(response["answer"])
 
