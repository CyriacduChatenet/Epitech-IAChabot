# from langchain.llms import OpenAI

#from langchain_openai import ChatOpenAI
#from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from getpass import getpass
from langchain_community.llms import HuggingFaceHub
from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain.chains import LLMChain
#from langchain.prompts import PromptTemplate
import os
import getpass

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a journalist."),
    ("user", "{input}")
])
loader = WebBaseLoader("https://www.lequipe.fr/Rugby/top-14/page-calendrier-resultats/13e-journee")
docs = loader.load()

llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    model_kwargs={
        "max_new_tokens": 512,
        "top_k": 30,
        "temperature": 0.1,
        "repetition_penalty": 1.03,
    },
)
embeddings = HuggingFaceEmbeddings()
output_parser = StrOutputParser()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings) 

#chain = LLMChain(prompt=prompt, llm=llm)

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)

document_chain.invoke({
    "input": "Tu peux me donner des score de match du top14?",
    "context": [Document(page_content="affichage des score de la 13ieme journee de top14")]
})

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "Tu peux me donner des score de match du top14?"})
print("Chatbot",response["answer"].split("Réponse:")[1])