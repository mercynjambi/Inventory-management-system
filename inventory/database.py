from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to the SQLite database
DATABASE_URL = ('sqloite:///./inventory.db')

# create Engine
engine = create_engine(DATABASE_URL)

# Session Local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class
Base = declarative_base()

def init_db(): # ensure db schema is setup by creating the necessary tables based on model definitions
    import inventory.models #import models
    Base.metadata.create_all(bind=engine) # create tables

# init_db()
