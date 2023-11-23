import os
from dotenv import load_dotenv

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

# class Config:
#     chunk_size = 500
#     chunk_overlap = 0
#     model_name = "gpt-3.5-turbo"
#     temperature = 0

class Agent:
    

    def __init__(self, url):
        self.result = None
        self.url = url
        self.load_page()        
        self.split_text()
        self.store_text()


    def load_page(self):
        # specify a DocumentLoader to load in your unstructured data as Documents
        loader = WebBaseLoader(self.url)
        self.data = loader.load()
            
    def split_text(self):
        # Split the Document into chunks for embedding and vector storage.
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
        self.all_splits = text_splitter.split_documents(self.data)
    
    def store_text(self):
        vector_store = Chroma.from_documents(documents=self.all_splits, embedding=OpenAIEmbeddings())
        # question = "What is the title of the job?, the company name?, the job requirements or what are they looking for?, also what is the position, job about?"
        # question = "Please provide specific details from the job posting, including the company name, job title, position, and a concise description of the job responsibilities. if not found tell me you could not found the info."
        question = """
        Please provide specific details from the job posting, including the company name, job title, position, and a concise description of the job responsibilities.

        Por favor, proporcione detalles específicos de la oferta de trabajo, incluyendo el nombre de la empresa, el título del trabajo, la posición y una descripción concisa de las responsabilidades laborales.
        """

        # Distill the retrieved documents into an answer using an LLM/Chat model (e.g., gpt-3.5-turbo) with RetrievalQA chain.
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        qa_chain = RetrievalQA.from_chain_type(llm,retriever=vector_store.as_retriever())
        self.result = qa_chain({"query": question})
    
    def result_query(self):
        return self.result["result"]
        
# if __name__ == "__main__":
#     agent = Agent(url="https://www.linkedin.com/jobs/view/3770664876/?alternateChannel=search&refId=eW9zGFqxf%2BhOUK0uRC2WDw%3D%3D&trackingId=wlK31WeG%2FHXB7guQLVP8ZQ%3D%3D")
#     agent.load_page()
#     agent.split_text()
#     agent.store_text()
