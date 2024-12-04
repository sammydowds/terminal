from openai import OpenAI 
from langchain_text_splitters import RecursiveCharacterTextSplitter
import psycopg2
from dotenv import load_dotenv
import os
import pymupdf 

load_dotenv()
DB_NAME=os.getenv('DB_NAME')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')

class Ingestor:
  def __init__(self):
    """
    Initializes the Ingestor class by establishing a database connection
    and setting up the OpenAI client.
    """
    try:
      self.db = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST}")
      self.cursor = self.db.cursor()
      self.openai = OpenAI()
    except psycopg2.Error as e:
      raise ConnectionError(f"Failed to connect to database: {e}")
  
  def save_embedding(self, embedding, content):
    """
    Persists the embeddings and content to the database.
    """
    try:
      self.cursor.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (content, embedding))
      self.db.commit()
      return True
    except psycopg2.Error as e:
      self.db.rollback()
      raise Exception(f"Failed to save embedding: {e}")

  def generate_embedding(self, chunk):
    """
    Generates an embedding for a given text chunk using OpenAI.
    """
    embeddings_res = self.openai.embeddings.create(model='text-embedding-ada-002', input=chunk)
    return embeddings_res.data[0].embedding
  
  def chunk_pdf(self, path):
    """
    Loads a PDF file and splits its content into overlapping chunks splitting on lines.
    """
    doc = pymupdf.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=0,
        length_function=len,
        separators=["\n", ".", "!", "?"]
    )
    chunks = text_splitter.split_text(text)
    return chunks 

  def ingest(self, folder=None):
    """
    Processes PDF files in a specified folder, generating embeddings
    for each chunk and saving them to the database.
    """
    if folder is None:
      raise ValueError("No folder supplied for ingestion.")
    
    if not os.path.exists(folder):
      raise ValueError(f"Folder does not exist: {folder}")

    processed_files = 0
    for file in os.listdir(folder):
      file_path = os.path.join(folder, file)
      
      if not file_path.lower().endswith('.pdf'):
        continue
        
      try:
        chunks = self.chunk_pdf(file_path)
        for chunk in chunks:
          embedding = self.generate_embedding(chunk)
          self.save_embedding(embedding, chunk)
        processed_files += 1
      except Exception as e:
        print(f"Error processing {file_path}: {e}")
        continue

    return processed_files

  def __del__(self):
    """
    Cleans up database resources by closing the cursor and connection.
    """
    try:
      if hasattr(self, 'cursor'):
        self.cursor.close()
      if hasattr(self, 'db'):
        self.db.close()
    except Exception:
      pass