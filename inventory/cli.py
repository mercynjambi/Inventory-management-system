import click
from inventory.services import (
    add_category, get_categories, add_item, get_items, delete_item, find_item_by_id, 
    find_item_by_name, find_category_by_id, find_category_by_name,
    add_supplier, get_suppliers, find_supplier_by_id, find_supplier_by_name,
    add_customer, get_customers, find_customer_by_id, find_customer_by_email,
    add_order, get_orders, find_order_by_id
)
from sqlalchemy.exc import SQLAlchemyError

@click.group()
def cli():
    """CLI for managing inventory."""
    pass

# Category Commands
@click.command()
@click.argument('name')
def addcategory(name):
    """Add a new category."""
    if not name.strip():
        click.echo("Error: Category name cannot be empty.")
        return

    try:
        add_category(name)
        click.echo(f'Category "{name}" added.')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
def viewcategories():
    """View all categories."""
    try:
        categories = get_categories()
        if not categories:
            click.echo("No categories found.")
            return
        for category in categories:
            click.echo(f'{category.id}: {category.name}')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('category_id', type=int)
def findcategorybyid(category_id):
    """Find a category by ID."""
    try:
        category = find_category_by_id(category_id)
        if category:
            click.echo(f'{category.id}: {category.name}')
        else:
            click.echo(f"No category found with ID {category_id}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('name')
def findcategorybyname(name):
    """Find a category by name."""
    try:
        category = find_category_by_name(name)
        if category:
            click.echo(f'{category.id}: {category.name}')
        else:
            click.echo(f"No category found with name {name}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

# Item Commands
@click.command()
@click.argument('name')
@click.argument('description')
@click.argument('quantity', type=int)
@click.argument('price', type=float)
@click.argument('category_id', type=int)
def additem(name, description, quantity, price, category_id):
    """Add a new item."""
    if not name.strip() or not description.strip():
        click.echo("Error: Item name and description cannot be empty.")
        return

    if quantity < 0:
        click.echo("Error: Quantity cannot be negative.")
        return

    if price < 0:
        click.echo("Error: Price cannot be negative.")
        return

    try:
        add_item(name, description, quantity, price, category_id)
        click.echo(f'Item "{name}" added.')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
def viewitems():
    """View all items."""
    try:
        items = get_items()
        if not items:
            click.echo("No items found.")
            return
        for item in items:
            click.echo(f'{item.id}: {item.name} - {item.description} - {item.quantity} - {item.price} - Category ID: {item.category_id}')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('item_id', type=int)
def deleteitem(item_id):
    """Delete an item by ID."""
    if item_id <= 0:
        click.echo("Error: Item ID must be a positive integer.")
        return

    try:
        delete_item(item_id)
        click.echo(f'Item with ID "{item_id}" deleted.')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('item_id', type=int)
def finditembyid(item_id):
    """Find an item by ID."""
    try:
        item = find_item_by_id(item_id)
        if item:
            click.echo(f'{item.id}: {item.name} - {item.description} - {item.quantity} - {item.price} - Category ID: {item.category_id}')
        else:
            click.echo(f"No item found with ID {item_id}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('name')
def finditembyname(name):
    """Find an item by name."""
    try:
        item = find_item_by_name(name)
        if item:
            click.echo(f'{item.id}: {item.name} - {item.description} - {item.quantity} - {item.price} - Category ID: {item.category_id}')
        else:
            click.echo(f"No item found with name {name}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

# Supplier Commands
@click.command()
@click.argument('name')
@click.argument('contact_info')
def addsupplier(name, contact_info):
    """Add a new supplier."""
    if not name.strip() or not contact_info.strip():
        click.echo("Error: Supplier name and contact info cannot be empty.")
        return

    try:
        add_supplier(name, contact_info)
        click.echo(f'Supplier "{name}" added.')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
def viewsuppliers():
    """View all suppliers."""
    try:
        suppliers = get_suppliers()
        if not suppliers:
            click.echo("No suppliers found.")
            return
        for supplier in suppliers:
            click.echo(f'{supplier.id}: {supplier.name} - {supplier.contact_info}')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('supplier_id', type=int)
def findsupplierbyid(supplier_id):
    """Find a supplier by ID."""
    try:
        supplier = find_supplier_by_id(supplier_id)
        if supplier:
            click.echo(f'{supplier.id}: {supplier.name} - {supplier.contact_info}')
        else:
            click.echo(f"No supplier found with ID {supplier_id}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('name')
def findsupplierbyname(name):
    """Find a supplier by name."""
    try:
        supplier = find_supplier_by_name(name)
        if supplier:
            click.echo(f'{supplier.id}: {supplier.name} - {supplier.contact_info}')
        else:
            click.echo(f"No supplier found with name {name}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

# Customer Commands
@click.command()
@click.argument('name')
@click.argument('email')
def addcustomer(name, email):
    """Add a new customer."""
    if not name.strip() or not email.strip():
        click.echo("Error: Customer name and email cannot be empty.")
        return

    try:
        add_customer(name, email)
        click.echo(f'Customer "{name}" added.')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
def viewcustomers():
    """View all customers."""
    try:
        customers = get_customers()
        if not customers:
            click.echo("No customers found.")
            return
        for customer in customers:
            click.echo(f'{customer.id}: {customer.name} - {customer.email}')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('customer_id', type=int)
def findcustomerbyid(customer_id):
    """Find a customer by ID."""
    try:
        customer = find_customer_by_id(customer_id)
        if customer:
            click.echo(f'{customer.id}: {customer.name} - {customer.email}')
        else:
            click.echo(f"No customer found with ID {customer_id}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('email')
def findcustomerbyemail(email):
    """Find a customer by email."""
    try:
        customer = find_customer_by_email(email)
        if customer:
            click.echo(f'{customer.id}: {customer.name} - {customer.email}')
        else:
            click.echo(f"No customer found with email {email}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

# Order Commands
@click.command()
@click.argument('item_id', type=int)
@click.argument('quantity', type=int)
@click.argument('customer_id', type=int)
def addorder(item_id, quantity, customer_id):
    """Add a new order."""
    if quantity <= 0:
        click.echo("Error: Quantity must be positive.")
        return

    try:
        add_order(item_id, quantity, customer_id)
        click.echo(f'Order for item ID "{item_id}" added.')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
def vieworders():
    """View all orders."""
    try:
        orders = get_orders()
        if not orders:
            click.echo("No orders found.")
            return
        for order in orders:
            click.echo(f'Order ID: {order.id} - Item ID: {order.item_id} - Quantity: {order.quantity} - Customer ID: {order.customer_id} - Date: {order.order_date}')
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('order_id', type=int)
def findorderbyid(order_id):
    """Find an order by ID."""
    try:
        order = find_order_by_id(order_id)
        if order:
            click.echo(
                f'Order ID: {order.id} - Item ID: {order.item_id} - Quantity: {order.quantity} - '
                f'Customer ID: {order.customer_id} - Date: {order.order_date}'
            )
        else:
            click.echo(f"No order found with ID {order_id}.")
    except SQLAlchemyError as e:
        click.echo(f"Error: {e}")

cli.add_command(addcategory)
cli.add_command(viewcategories)
cli.add_command(findcategorybyid)
cli.add_command(findcategorybyname)
cli.add_command(additem)
cli.add_command(viewitems)
cli.add_command(deleteitem)
cli.add_command(finditembyid)
cli.add_command(finditembyname)
cli.add_command(addsupplier)
cli.add_command(viewsuppliers)
cli.add_command(findsupplierbyid)
cli.add_command(findsupplierbyname)
cli.add_command(addcustomer)
cli.add_command(viewcustomers)
cli.add_command(findcustomerbyid)
cli.add_command(findcustomerbyemail)
cli.add_command(addorder)
cli.add_command(vieworders)
cli.add_command(findorderbyid)

if __name__ == '__main__':
    cli()
       

        
       
