<img src="assets/background.png" alt="Background Image" style="width:100%; height:auto; border-radius:10px; margin-bottom:4px;">

## Summary
Terminal is a project that helps get a simple RAG (Retrieval-Augmented Generation) up and running based on a user specified set of PDFs.

## Getting started

### Database
Start the database:
```bash
cd terminal/terminal/docker && docker compose up -d
```
Note: this project utilizes the pgvector/pgvector image referenced [here](https://github.com/pgvector/pgvector?tab=readme-ov-file#docker). 

Initialize the table:
```bash
psql -h localhost -p 5432 -U user -d terminal -f ../db/init.sql
```

### Ingest Documents 

Ensure you have a local .env containing the following:
```bash
OPENAI_API_KEY=<insert your openai key>
DATABASE_URL=<insert local database URL>
```

Note: OpenAI is used to generate the embeddings.

Run the ingestion over a specified folder containing PDF's you would like to use as the target for queries. Ingestion consists of looping through files, chunking them (with overlap), and saving the embedding to a postgres db.
```python
ingestor = Ingestor()

ingestor.ingest('documents')
```

### Processing (retrieval and response) 

```python
processor = Processor()

processor.retrieve_content(query) # embed, search in vector DB 
processor.stream_completion(query) 
# OR
processor.completion(query)
```