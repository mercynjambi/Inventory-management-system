
from inventory.database import SessionLocal
from inventory.models import Category, Item

def get_session():
    return SessionLocal() # create a new db session

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
    item = item(name=name, description=description, quantity=quantity, price=price, category_id=category_id)
    session.add(item)
    session.commit()
    session.close()

def get_items():
    session = get_session()
    items = session.query(Item).all
    session.close()
    return items

def delete_item(item_id):
    session = get_session()
    item = session.query(Item).filter(Item.id == item_id).first()
    if item:
        session.delete()
        session.commit()
    session.close()






