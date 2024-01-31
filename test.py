from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

import warnings

def bot_answer(input):

    print("test1")
    warnings.filterwarnings("ignore", category=UserWarning)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a journalist."),
        ("user", "{input}")
    ])
    loader = WebBaseLoader("https://www.lequipe.fr/Rugby/top-14/page-calendrier-resultats/13e-journee")
    docs = loader.load()

    print("test2")
    llm = Ollama(model="llama2")
    embeddings = HuggingFaceEmbeddings()
    output_parser = StrOutputParser()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings) 

    print("test3")

    #chain = LLMChain(prompt=prompt, llm=llm)

    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    print("test4")

    document_chain = create_stuff_documents_chain(llm, prompt)

    document_chain.invoke({
        "input": input,
        "context": [Document(page_content="affichage des score de la 13ieme journee de top14")]
    })

    print("test5")

    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    print("test6")

    response = retrieval_chain.invoke({"input": input})
    print("test7")
    return(response["answer"])
