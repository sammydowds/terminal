# Dripfeed

## Summary

Find products based a single sentence. 

## Set up

### Database

Start the database
```bash
cd ingestion/db/docker && docker compose up -d
```

Add .env (locally)
```
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
python seed.py
```

Now you have a database running with product table populated. Note: yes, we are using both `psycopg2` (ingestion) and `sqlalchemy` (seeding)... we never said we were perfect 😉 