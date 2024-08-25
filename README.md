# Simple Inventory Management System

## Objective
Create a Python-based inventory management system that interacts with a MongoDB database to perform CRUD operations.

## Requirements
- Python 3.x
- MongoDB

## Setup
1. Install the required packages:
'pip install -r requirements.txt'

2. Ensure MongoDB is running and accessible.

3. Run the `inventory_management.py` script:
'python inventory_management.py'


## Functions
- **add_item(item_id, name, quantity, price, category):** Adds a new item to the inventory.
- **view_items():** Retrieves and displays all items in the inventory.
- **update_item(item_id, name=None, quantity=None, price=None, category=None):** Updates details of an existing item.
- **delete_item(item_id):** Removes an item from the inventory.
- **search_item(search_term):** Searches for an item by name or category.

Instructions:
Make sure MongoDB is installed and running locally.
Update config.py if your MongoDB instance is hosted elsewhere.
Install Python packages from requirements.txt using pip install -r requirements.txt.
Run the inventory_management.py script to interact with the inventory system.


1. Set Up Your Python Environment:
'python --version'

Set up a virtual environment:
'python -m venv venv'
'source venv/bin/activate' 

2. Install Required Packages:
'pip install pymongo'

3. Set Up MongoDB:
Start the MongoDB server:
'mongod'

5. Run the Python Script:
'python your_script_name.py'

6. Test Your Functions
Ensure each function (add_item, view_items, update_item, delete_item, search_item) works as expected by running the script and observing the output.


Thank You... 
Ashvani S





