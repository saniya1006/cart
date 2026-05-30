import logging
from config import LOGGING_FORMAT, LEVEL
from database import init_db, load_cart,save_cart 
from utils import add_item_to_cart,calculation,remove_item,search_cart,update_quantity,print_menue,exit_program,clear_cart,check_duplicate,cart_view

logging.basicConfig(
    level=LEVEL,
    format=LOGGING_FORMAT
    )
logger = logging.getLogger(__name__)

# dummy comment 

init_db ()
flag = True
cart = load_cart() # Load cart ONCE before the loop
while flag:
    print_menue()
    user_input=input("\nPlease Enter Your Choice!! \n")

    if user_input == "1":
        # First check if item already exists in cart
        item = input("Please Enter Item Name to Add ").strip()
        if item == "":
            logger.error("Invalid Item to Add")
            continue
        if check_duplicate(cart, item):
            logger.warning(f"Item '{item}' already exists in cart!")
        else:
            #Fixed: pass cart directly, mutations happen in place inside utils
            add_item_to_cart(cart, item)
        
    elif user_input == "2":
        clear_cart(cart)
        
    elif user_input == "3":
        remove_item(cart)

    elif user_input == "4":
        cart_view(cart)
    
    elif user_input == "5":
        update_quantity(cart)

    elif user_input == "6":
        calculation(cart)

    elif user_input == "7":
        search_cart(cart)

    elif user_input == "8":
        save_cart(cart)
        exit_program()

    else:
        logger.warning("Invalid Choice")
   
 
    
