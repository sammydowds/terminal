from dotenv import load_dotenv
from openai import OpenAI 
import psycopg2
import os

load_dotenv()
DB_URL=os.getenv('DATABASE_URL')

class Processor:
    def __init__(self):
        """
        Initializes the Processor class by establishing a database connection
        and setting up the OpenAI client.
        """
        try:
            self.db = psycopg2.connect(DB_URL)
            self.cursor = self.db.cursor()
            self.openai = OpenAI()
        except psycopg2.Error as e:
            raise ConnectionError(f"Failed to connect to database: {e}")

    def completion(self, content, query):
        """
        Take search results, and expand with openAI
        """
        prompt = f'You are given an answer and question, please create a more clear answer for the question based on the answer provided: Answer: {content[0]}, Question: {query}'
        response = self.openai.completions.create(
            model="gpt-4o-mini",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    def retrieve_content(self, query):
        """
        Retrieves content via L2 distance
        """
        query_embedding = self.generate_embedding(query)
        self.cursor.execute("""
            SELECT content FROM documents ORDER BY embedding <-> %s::vector LIMIT 5;
        """, (query_embedding,))

        results = self.cursor.fetchall()
        return [result[0] for result in results]

    def generate_embedding(self, query):
        """
        Generates an embedding for a given text chunk using OpenAI.
        """
        embeddings_res = self.openai.embeddings.create(model='text-embedding-ada-002', input=query)
        return embeddings_res.data[0].embedding
    
     def stream_completion(self, content, query):
        """
        Streams the response from OpenAI for a given question and retrieved content.
        """
        if not content:
            return "I am sorry, I could not find an exact answer for that."

        prompt = f'You are given an answer and question, please create a more clear answer for the question based on the answer provided: Answer: {content[0]}, Question: {query}'
        stream = self.openai.completions.create(
            model="gpt-4o-mini",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
            stream=True
        )
        for chunk in stream:
            yield chunk.choices[0].text
