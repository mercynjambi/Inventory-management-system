
from inventory.database import SessionLocal
from inventory.models import Category, Item

def get_session():
    return SessionLocal()  

def add_category(name):
    session = get_session()
    category = Category(name=name)
    session.add(category)
    session.commit()
    session.close()

def get_categories():
    session = get_session()
    categories = session.query(Category).all()
    session.close()
    return categories  

def add_item(name, description, quantity, price, category_id):
    session = get_session()
    item = Item(name=name, description=description, quantity=quantity, price=price, category_id=category_id)
    session.add(item)
    session.commit()
    session.close()

def get_items():
    session = get_session()
    items = session.query(Item).all()  
    session.close()
    return items

def delete_item(item_id):
    session = get_session()
    item = session.query(Item).filter(Item.id == item_id).first()
    if item:
        session.delete(item)  
        session.commit()
    session.close()

def find_item_by_id(item_id):
    session = get_session()
    item = session.query(Item).filter(Item.id == item_id).first()
    session.close()
    return item

def find_item_by_name(name):
    session = get_session()
    item = session.query(Item).filter(Item.name == name).first()
    session.close()
    return item

def find_category_by_id(category_id):
    session = get_session()
    category = session.query(Category).filter(Category.id == category_id).first()
    session.close()
    return category

def find_category_by_name(name):
    session = get_session()
    category = session.query(Category).filter(Category.name == name).first()
    session.close()
    return category


