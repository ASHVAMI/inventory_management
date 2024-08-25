from config import get_db

def add_item(item_id, name, quantity, price, category):
    db = get_db()
    item = {
        "item_id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category
    }
    db.insert_one(item)
    print(f"Item '{name}' added successfully.")

def view_items():
    db = get_db()
    items = db.find()
    for item in items:
        print(item)

def update_item(item_id, name=None, quantity=None, price=None, category=None):
    db = get_db()
    update_fields = {}
    if name:
        update_fields["name"] = name
    if quantity is not None:
        update_fields["quantity"] = quantity
    if price is not None:
        update_fields["price"] = price
    if category:
        update_fields["category"] = category
    db.update_one({"item_id": item_id}, {"$set": update_fields})
    print(f"Item with ID '{item_id}' updated successfully.")

def delete_item(item_id):
    db = get_db()
    db.delete_one({"item_id": item_id})
    print(f"Item with ID '{item_id}' deleted successfully.")

def search_item(search_term):
    db = get_db()
    items = db.find({"$or": [
        {"name": {"$regex": search_term, "$options": "i"}},
        {"category": {"$regex": search_term, "$options": "i"}}
    ]})
    for item in items:
        print(item)

if __name__ == "__main__":
    add_item("001", "Laptop", 10, 999.99, "electronics")
    add_item("002", "T-Shirt", 50, 19.99, "clothing")
    print("View all items:")
    view_items()
    print("Search for 'T-Shirt':")
    search_item("T-Shirt")
    update_item("002", price=17.99)
    delete_item("001")
    print("View all items after deletion:")
    view_items()
