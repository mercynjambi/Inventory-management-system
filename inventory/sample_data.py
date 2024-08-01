from inventory.services import add_item


CATEGORY_ID_ELECTRONICS = 1
CATEGORY_ID_KITCHENWARE = 3


electronics_items = [
    {"name": "Smart TV", "description": "55-inch 4K Ultra HD Smart TV", "quantity": 10, "price": 499.99, "category_id": CATEGORY_ID_ELECTRONICS},
    {"name": "Bluetooth Headphones", "description": "Over-ear Bluetooth headphones with noise cancellation", "quantity": 20, "price": 129.99, "category_id": CATEGORY_ID_ELECTRONICS},
    {"name": "Desktop", "description": "15-inch laptop with Intel Core i7, 16GB RAM, 512GB SSD", "quantity": 15, "price": 899.99, "category_id": CATEGORY_ID_ELECTRONICS},
    {"name": "Smartphone", "description": "6.5-inch smartphone with 128GB storage and 6GB RAM", "quantity": 25, "price": 699.99, "category_id": CATEGORY_ID_ELECTRONICS},
    {"name": "Digital Camera", "description": "DSLR camera with 18-55mm lens", "quantity": 8, "price": 549.99, "category_id": CATEGORY_ID_ELECTRONICS},
]


kitchenware_items = [
    {"name": "Chef's Knife", "description": "8-inch stainless steel chef's knife", "quantity": 30, "price": 39.99, "category_id": CATEGORY_ID_KITCHENWARE},
    {"name": "Non-stick Frying Pan", "description": "12-inch non-stick frying pan", "quantity": 25, "price": 24.99, "category_id": CATEGORY_ID_KITCHENWARE},
    {"name": "Blender", "description": "High-speed blender with 6 blades and 1.5-liter jar", "quantity": 12, "price": 89.99, "category_id": CATEGORY_ID_KITCHENWARE},
    {"name": "Cutting Board", "description": "Large bamboo cutting board", "quantity": 40, "price": 19.99, "category_id": CATEGORY_ID_KITCHENWARE},
    {"name": "Toaster", "description": "4-slice toaster with variable browning control", "quantity": 15, "price": 29.99, "category_id": CATEGORY_ID_KITCHENWARE},
]


for item in electronics_items:
    add_item(item["name"], item["description"], item["quantity"], item["price"], item["category_id"])


for item in kitchenware_items:
    add_item(item["name"], item["description"], item["quantity"], item["price"], item["category_id"])

print("Sample items added successfully.")
