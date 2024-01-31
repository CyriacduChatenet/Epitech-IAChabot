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
warnings.filterwarnings("ignore", category=UserWarning)

class ChatbotMemory:
    def __init__(self):
        self.previous_responses = []

    def add_response(self, response):
        self.previous_responses.append(response)

    def get_previous_responses(self):
        return self.previous_responses

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a journalist."),
    ("user", "{input}")
])

loader = WebBaseLoader("https://www.lequipe.fr/Rugby/top-14/page-calendrier-resultats/13e-journee")
docs = loader.load()

llm = Ollama(model="llama2")
embeddings = HuggingFaceEmbeddings()
output_parser = StrOutputParser()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings) 

memory = ChatbotMemory()

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)

document_chain.invoke({
    "input": "Tu peux me donner des scores de match du top14?",
    "context": [Document(page_content="affichage des scores de la 13e journee de top14")]
})

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

user_input = "Tu peux me donner des scores de match du top14?"
response = retrieval_chain.invoke({"input": user_input})
memory.add_response(response["answer"])

user_input = "Tu peux me donner les meilleurs équipes du top14?"
response = retrieval_chain.invoke({"input": user_input})
memory.add_response(response["answer"])

# Now you can use the previous responses in future interactions
print("Previous Responses:", memory.get_previous_responses())
