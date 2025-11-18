from dotenv import load_dotenv, find_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Search for .env in parent folders
load_dotenv(find_dotenv())
POSTGRES_URL = os.getenv('POSTGRES_URL')
print(POSTGRES_URL)

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



