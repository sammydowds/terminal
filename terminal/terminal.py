from openai import OpenAI 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# import psycopg2
import os

class Terminal:
  def __init__(self):
    # self.db = psycopg2.connect(f"dbname={dbname} user={dbuser} password={dbpassword} host={dbhost}")
    # self.openai = new OpenAI()
    self.ingestion_chunk_size = 1024*8
  
  def save_embedding(self, embedding):
    # saved embedding to pgvector
    print(embedding)
    
    # cursor = self.db.cursor()
    # cursor.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (document, embedding))
    # connection.commit()
    # cursor.close()
   
    # return true

  def generate_embedding(self, chunk):
    # generates embedding from text
    print(chunk)

    # const input = text.replace(/\n/g, ' ')
    # const embeddingResponse = await self.openai.embeddings.create({
    #   model: 'text-embedding-ada-002',
    #   input,
    # })
    # const [{ embedding }] = embeddingResponse.data.data
    # return embedding
  
  def chunk_pdf(self, path):
    loader = PyPDFLoader(path)
    text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=500, 
      chunk_overlap=50
    )
    chunks = loader.load_and_split(text_splitter)
    return chunks

  def ingest(self, folder=None):
    if folder is None:
      raise ValueError("No folder supplied for ingestion.")

    for file in os.listdir(folder):
      file_path = os.path.join(folder, file)
      chunks = self.chunk_pdf(file_path)
      for chunk in chunks:
        embedding = self.generate_embedding(chunk)
        self.save_embedding(embedding)

    return True 

  def __del__(self):
    if self.db:
      self.db.close()