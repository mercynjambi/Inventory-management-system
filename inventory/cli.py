import click
from inventory.services import add_category, get_categories, add_item, get_items, delete_item, find_item_by_id, find_item_by_name, find_category_by_id, find_category_by_name
from sqlalchemy.exc import SQLAlchemyError

@click.group()
def cli():
    """CLI for managing inventory."""
    pass

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

cli.add_command(addcategory)
cli.add_command(viewcategories)
cli.add_command(additem)
cli.add_command(viewitems)
cli.add_command(deleteitem)
cli.add_command(finditembyid)
cli.add_command(finditembyname)
cli.add_command(findcategorybyid)
cli.add_command(findcategorybyname)

if __name__ == '__main__':
    cli()
