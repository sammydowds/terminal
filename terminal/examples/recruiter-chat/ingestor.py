from terminal.ingestor import Ingestor 

class ResumeIngestor(Ingestor):
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
            separators=["\n", ".", "!", "?", "▪"]
        )
        chunks = text_splitter.split_text(text)
        return chunks 