from products import products
from users import users
from orders import orders, add_order

def show_menu():
    print("=== Welcome to Hanouma Marketplace ===")
    print("Products available:")
    for i, p in enumerate(products):
        print(f"{i+1}. {p['name']} - ${p['price']}")
    
    print("\nUsers:")
    for u in users:
        print(f"- {u['name']} (Balance: ${u['balance']})")
