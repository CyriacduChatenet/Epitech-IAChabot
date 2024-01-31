from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a journalist."),
    ("user", "{input}")
])
loader = WebBaseLoader("https://www.bbc.com/sport/football/european-championship/scores-fixtures/2023-11")
docs = loader.load()
 
llm = ChatOpenAI(openai_api_key="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")
embeddings = OpenAIEmbeddings(openai_api_key="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")
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
    "input": "What is the score of the france match?",
    "context": [Document(page_content="tell us all matches result")]
})
 
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
 
response = retrieval_chain.invoke({"input": "What is the score of the france matches?"})
print(response["answer"])