from sqlalchemy import Column, Integer, String, ForeignKey
from inventory.database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nulable=True)
    items = relationship('item', back_populates='category')

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nulable=False)
    description = Column(String)
    quantity = Column(Integer, default=0)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='items')







    

