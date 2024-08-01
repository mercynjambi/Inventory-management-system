from inventory.database import init_db
from inventory.cli import cli

def main():
    """Initialize database and start CLI."""
    print("Initializing database...")
    init_db()
    print("Starting CLI...")
    cli()

if __name__ == '__main__':
    main()
