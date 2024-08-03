# **Inventory Management System**

## **Overview**
The Inventory Management System is a command-line application designed to manage inventory items, categories, suppliers, customers, and orders. The application is built using Python and leverages SQLAlchemy for database interactions and Click for creating the command-line interface (CLI).

## **Features**
- Add, view, and delete inventory items.
- Manage categories, suppliers, customers, and orders.
- Find items, categories, suppliers, and customers by various attributes.
- View all entities in the system.

## **Requirements**
- Python 3
- Pipenv for managing dependencies

## **Setup**

### **Clone the Repository**

git clone https://github.com/mercynjambi/Inventory-management-system.git
cd Inventory-management-system

### **Install Dependencies**
Ensure that you have Pipenv installed. If not, install it using pip:
    _pip install pipenv_
Then, install the project dependencies:
    _pipenv install_

## **Initialize the Database**
Before running the application, initialize the database:
    _python main.py_
    
## **Usage:**
### **Activate the Virtual Environment**

Activate the virtual environment using Pipenv:
    _pipenv shell_


### **Running the CLI**
You can interact with the inventory management system using the CLI:
     _export PYTHONPATH=.
python inventory/cli.py_

### **Available Commands**
***Categories:***

1.addcategory <name>: Add a new category.
2.viewcategories: View all categories.
3.findcategorybyid <id>: Find a category by ID.
4.findcategorybyname <name>: Find a category by name.
    
***Items:***

1.additem <name> <description> <quantity> <price> <category_id>: Add a new item.
2.viewitems: View all items.
3.deleteitem <item_id>: Delete an item by ID.
4.finditembyid <item_id>: Find an item by ID.
5.finditembyname <name>: Find an item by name.
    
***Suppliers:***

1.addsupplier <name> <contact_info>: Add a new supplier.
2.viewsuppliers: View all suppliers.
3.findsupplierbyid <id>: Find a supplier by ID.
4.findsupplierbyname <name>: Find a supplier by name.
    
***Customers:***
    
1.addcustomer <name> <email>: Add a new customer.
2.viewcustomers: View all customers.
3.findcustomerbyid <id>: Find a customer by ID.
4.findcustomerbyemail <email>: Find a customer by email.
    
***Orders:***

1.addorder <item_id> <quantity> <customer_id>: Add a new order.
2.vieworders: View all orders.
3.findorderbyid <order_id>: Find an order by ID.
    
## **Example Usage**
### **Add a new category:**
python inventory/cli.py addcategory "Electronics"

***View all items:***

python inventory/cli.py viewitems

***Find a supplier by name:***

python inventory/cli.py findsupplierbyname "ABC Suppliers"

# **Contributing**
If you'd like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

# **License**
This project is licensed under the MIT License. See the LICENSE file for details.

# **Contact**
For questions or suggestions, please contact:
    ***njambi695@gmail.com***
    
