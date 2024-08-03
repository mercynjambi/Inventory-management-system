
from inventory.database import SessionLocal
from inventory.models import Category, Item, Order, Supplier, Customer 

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

def add_item(name, description, quantity, price, category_id, supplier_id=None):
    session = get_session()
    item = Item(name=name, description=description, quantity=quantity, price=price, category_id=category_id, supplier_id=supplier_id)
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

def add_supplier(name, contact_info):
    session = get_session()
    supplier = Supplier(name=name, contact_info=contact_info)
    session.add(supplier)
    session.commit()
    session.close()

def get_suppliers():
    session = get_session()
    suppliers = session.query(Supplier).all()
    session.close()
    return suppliers

def find_supplier_by_id(supplier_id):
    session = get_session()
    supplier = session.query(Supplier).filter(Supplier.id == supplier_id).first()
    session.close()
    return supplier

def find_supplier_by_name(name):
    session = get_session()
    supplier = session.query(Supplier).filter(Supplier.name == name).first()
    session.close()
    return supplier

# Customer Services
def add_customer(name, email):
    session = get_session()
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    session.close()

def get_customers():
    session = get_session()
    customers = session.query(Customer).all()
    session.close()
    return customers

def find_customer_by_id(customer_id):
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    session.close()
    return customer

def find_customer_by_email(email):
    session = get_session()
    customer = session.query(Customer).filter(Customer.email == email).first()
    session.close()
    return customer

# Order Services
def add_order(item_id, quantity, customer_id):
    session = get_session()
    order = Order(item_id=item_id, quantity=quantity, customer_id=customer_id)
    session.add(order)
    session.commit()
    session.close()

def get_orders():
    session = get_session()
    orders = session.query(Order).all()
    session.close()
    return orders

def find_order_by_id(order_id):
    session = get_session()
    order = session.query(Order).filter(Order.id == order_id).first()
    session.close()
    return order



