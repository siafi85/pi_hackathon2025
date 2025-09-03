from menu import show_menu
from orders import add_order
from products import products
from users import users

show_menu()

# مثال: إضافة طلب تلقائي للتجربة
add_order(users[0]["name"], products[0]["name"])

print("\nCurrent orders:")
from orders import orders
for o in orders:
    print(f"{o['user']} ordered {o['product']}")
