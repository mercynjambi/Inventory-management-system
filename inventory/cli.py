import click
from inventory.services import add_category, get_categories, add_item, get_items, delete_item
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
@click.argument('price', type=float)  # Change to float for price
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

cli.add_command(addcategory)
cli.add_command(viewcategories)
cli.add_command(additem)
cli.add_command(viewitems)
cli.add_command(deleteitem)

if __name__ == '__main__':
    cli()
