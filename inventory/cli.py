# inventory/cli.py

import click
from inventory.services import add_category, get_categories, add_item, get_items, delete_item

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def addcategory(name):
    add_category(name)
    click.echo(f'Category "{name}" added.')

@click.command()
def viewcategories():
    categories = get_categories()
    for category in categories:
        click.echo(f'{category.id}: {category.name}')

@click.command()
@click.argument('name')
@click.argument('description')
@click.argument('quantity', type=int)
@click.argument('price', type=int)
@click.argument('category_id', type=int)
def additem(name, description, quantity, price, category_id):
    add_item(name, description, quantity, price, category_id)
    click.echo(f'Item "{name}" added.')

@click.command()
def viewitems():
    items = get_items()
    for item in items:
        click.echo(f'{item.id}: {item.name} - {item.description} - {item.quantity} - {item.price} - {item.category_id}')

@click.command()
@click.argument('item_id', type=int)
def deleteitem(item_id):
    delete_item(item_id)
    click.echo(f'Item with ID "{item_id}" deleted.')

cli.add_command(addcategory)
cli.add_command(viewcategories)
cli.add_command(additem)
cli.add_command(viewitems)
cli.add_command(deleteitem)

if __name__ == '__main__':
    cli()
