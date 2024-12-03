# Terminal

## Summary
Terminal is a Retrieval Augmented Generation (RAG) framework designed to facilitate the creation of chat-like interfaces. It enables users to chunk documents into a vector database, allowing for efficient retrieval of relevant information based on user queries. The system is driven by a frontend that interacts with user-created agents to generate contextually appropriate responses, enhancing the overall user experience.

## Getting started

### Database

Start the database:
```bash
cd docker && docker compose up -d
```

Initialize table:
```bash
psql -h localhost -p 5432 -U user -d terminal -f ../db/init.sql
```

### Populating Vector DB

Run the ingestion over a specified folder containing PDF's you would like to use as the target for queries. Ingestion consists of looping through files, chunking them (with overlap), and saving the embedding to a postgres db.
```python
t = Terminal()

t.ingest('documents')
```

### Starting API 

### Frontend 
