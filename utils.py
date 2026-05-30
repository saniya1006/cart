import logging
import time
from config import MENUE_OPTIONS
logger= logging.getLogger(__name__)
cart = []
def check_duplicate(cart, item):          
    for list_item in cart:
        if list_item['item'].upper() == item.upper():
            return True
    return False

def add_item_to_cart ( cart,item):
    while True:
        try:
            price = float(input("item price: "))
            if price <=0:
                logging.warning("Price must be greater then 0")
                continue
            break
        except ValueError:
            logging.warning("Please Enter Valid price")
    while True:    
        try:    
            quantity = int(input("Quantity: "))
            if quantity <=0:
                logging.warning("quantity must be greater then 0")
                continue

            break
        except ValueError:
            logging.warning("Please Enter Valid Quantity")
    item_dict =   {}
    item_dict["item"] = item
    item_dict["price"] = price
    item_dict["quantity"] = quantity

    cart.append(item_dict)
    logging.info(f"item :{item}, added in the cart") 
    logging.info(cart)
    return cart

def clear_cart(cart):
    if len(cart) > 0:
        cart.clear()
        logging.info("your cart has been cleared")
    else:
        logging.warning("Your cart is already empty")

def remove_item(cart):
    relove_flag = True
    item = input("\n Enter your item to remove! ").strip()
    print(item)
    print(type(item))
    for cart_item in cart:
        print(cart_item)
        time.sleep(5)
        if cart_item['item'].upper() == item.upper():
            cart.remove(cart_item)
            logging.info(f"Item {item} Removed !")
            relove_flag = False
            break
    if relove_flag:
        logging.warning( f"Item {item} Not available in the cart !")

def cart_view(cart):
    for item in cart:
        logging.info(item)


def exit_program():
    exit(0)


def calculation(cart):
    Total_bill = 0
    print("*"*100)
    print("\n")
    print("-"*50)
    for cart_item in cart:
        logging.info(f"total price of {cart_item['item']} is {cart_item['quantity'] * cart_item['price']}")
        Total_bill = Total_bill + cart_item['quantity'] * cart_item['price']
    print("-"*50)
    print("\n")
    logging.info(f"Total bill is {Total_bill}")
    print("*"*100)

def update_quantity(cart):
    item_found = False
    item = input("Enter Item name to update the quantity: ").strip()
    if item == "":
        logging.warning("Invlaid Item Name ")
        return
    
    for cart_item in cart:
        if cart_item['item'].upper()== item.upper():
            while True:
                try:
                    new_qyt  = int(input("Enter New Quantity: "))
                    if new_qyt <=0:
                        logging.warning("New quantity must be greater then 0")
                        continue
                    cart_item['quantity'] = new_qyt
                    logging.info( f"New Quantity : {new_qyt} updated for the item {cart_item['item']}")

                    return
                except Exception:
                    logging.warning(f"Please enter valid Quantity for the item {item}")
            item_found = True
    
    if item_found == False:
        logging.warning("Item not available in the cart")

def search_cart(cart):
    item = input("Enter item to search...")
    for cart_item in cart:
        if cart_item['item'].upper() == item.upper():
            logging.info("Item found")
            logging.info(cart_item)
            break

def print_menue():
    print("*" * 50)
    print(               "CART MENUES")
    print("*" * 50)
    for num , menu in MENUE_OPTIONS:
        print(f"{num} . {menu}")
    print("*" * 50)