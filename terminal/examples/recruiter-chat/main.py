from .ingestor import ResumeIngestor 
from .processor import ResumeProcessor 

def main():
    try:
        ingestor = Ingestor()
        processed_files = ingestor.ingest("./terminal/examples/recruiter-chat/documents")
        print(f"Successfully processed {processed_files} PDF files")

        processor = ResumeProcessor()
        print(processor.process_query("When have you used React?"))
        print(processor.process_query("When have you used Python?"))
        print(processor.process_query("When have you used AWS?"))
        print(processor.process_query("WHen did you graduate college?"))
    except Exception as e:
        print(f"Error during ingestion: {e}")

if __name__ == "__main__":
    main()
