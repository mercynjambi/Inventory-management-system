from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./inventory.db'

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def init_db(): 
    print("Initializing database...")
 
    from inventory.models import Category, Item, Supplier, Customer, Order
    Base.metadata.create_all(bind=engine) 


