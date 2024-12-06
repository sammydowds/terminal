from terminal.ingestor import Ingestor
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pymupdf 

class ResumeIngestor(Ingestor):
    def chunk_text(self, text):
        """
        Chunks text recursively.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=200,
            chunk_overlap=0,
            length_function=len,
            separators=["\n", ".", "!", "?"]
        )
        chunks = text_splitter.split_text(text)
        return chunks 