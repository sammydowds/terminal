# Dripfeed

## Summary

Find products based on a single sentence. 

## Set up

### Database

Start the database
```bash
cd ingestion/db/docker && docker compose up -d
```

Add .env (locally)
```
OPENAI_API_KEY=<your api key>
DATABASE_URL=postgresql://user:password123@localhost:5432/dripfeed
```

Create the vector extensions
```
psql DATABASE_URL
```
Then
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Setup python env and dependencies
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

Initalize tables and seed product data
```bash
cd backend/ingestion/db && python seed.py
```

Generate embeddings table data

```bash
cd backend/ingestion && python
```

Then run
```python
from ingestion import ProductIngestor
p = ProductIngestor()
p.ingest()
```
This will loop through every product in the database and generate embeddings off of the attributes.

Now you have a database running with `product_table` and `product_embeddings` table populated. Note: yes, we are using both `psycopg2` (ingestion) and `sqlalchemy` (seeding)... we never said we were perfect 😉 

Your database is now ready for the API.