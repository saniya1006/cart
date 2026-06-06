import streamlit as st
import logging
import sys
from io import StringIO
from config import LOGGING_FORMAT , LEVEL, MENUE_OPTIONS
from database import init_db , load_cart, save_cart
from utils import check_duplicate

logging.basicConfig(level=LEVEL, format=LOGGING_FORMAT)
logger= logging.getLogger(__name__)

init_db()

if "cart" not in st.session_state:
    st.session_state.cart = load_cart()
def get_total():
    return sum(item["quantity"] * item["price"] for item in st.session_state.cart)

st.set_page_config(page_title="Cart App", layout="centered")
st.title("Shopping Cart")

# Streamlit-friendly processing of your configuration tuple

menue_label = [label_item for label_item in MENUE_OPTIONS]
st.sidebar.header("Meanue")
choice = st.sidebar.radio("Select your choice", menue_label, index=3)
choice = choice[1]

if choice == "Add Item":
    st.subheader("Add Item")
    with st.form("add_from", clear_on_submit=True):
        item = st.text_input("Enter the item to add").strip()
        col1 , col2 = st.columns(2)

        with col1:
           price =  st.number_input("Price", step = .5, format = '%f')
        with col2:
            quantity = st.number_input("Quantity", step= 1, format='%d')
        
        submitted = st.form_submit_button("Add item to cart", type = "primary")
        if not item:
            st.error("Item name cannot be empty !!")
        elif check_duplicate( st.session_state.cart , item):
            st.error(f"Item '{item}', already exists in the cart !!")
        else:
            st.session_state.cart.append(
                {
                    "item": item,
                    "price": price,
                    "quantity": quantity
                }
            )
            save_cart(st.session_state.cart)
            st.success(f"Item '{item}' added to cart successfully !!")

elif choice == "Clear":
    st.subheader("Clear the cart")
    if not st.session_state.cart:
        st.info("Your cart is already empty !!")
    else:
        st.warning(f"are you sure ? you want to clear the cart.Your cart has {len(st.session_state.cart)} items in the cart")
        if st.button("yes , clear  the cart..", type = "primary"):
            st.session_state.cart.clear()
            save_cart(st.session_state.cart)
            st.success("Your cart has been cleared")
elif choice == "Remove Item":
    st.subheader("remove Item from the cart")
    if not st.session_state.cart:
        st.info("Your cart is empty")

    else:
        show_item = [read_item for read_item in st.session_state.cart]
        selected = st.selectbox("Select item to remove", show_item)


        if st.button("Remove item", type="primary"):
            for idx, list_item in enumerate(st.session_state.cart):
                if list_item['item'].upper() == selected['item'].upper():
                    st.session_state.cart.pop(idx)
                    save_cart(st.session_state.cart)
                    st.success("Your Item is successfully deleted")
elif choice == "View Items":
    st.subheader("View cart Item ")
    if not st.session_state.cart:
        st.info("Your cart is empty")

    else:
        for read_item in st.session_state.cart:
            st.write(read_item)
        
elif choice == "Get Total":
    st.subheader("Get Total")
    if not st.session_state.cart:
        st.info("Your cart is empty")

    else:
        total = get_total()
        st.metric(label = "Grand Total:", value=f"{total}")

elif choice == "Search cart Item":
    st.subheader("Search Item")
    if not st.session_state.cart:
        st.info("Your cart is empty")
    else:
        search_item= st.text_input("Enter item name to search").strip()
        if st.button("Search", type="primary"):
            found_items = [item for item in st.session_state.cart if item['item'].upper() == search_item.upper()]#list comprehension to find the item in the cart
            if found_items:#agar list khali nhi hai us m item hasi to ye condition run karegi
                st.success(f"Item '{search_item}' found in the cart !!")#success keyword se success message show hoga green color m
                for item in found_items:
                    st.write(item)
            else:
                st.warning(f"Item '{search_item}' not found in the cart !!")
            
elif choice == "Update quantity":
    st.subheader("Update quantity")
    if not st.session_state.cart:
        st.info("Your cart is empty")
    else:
        show_item = [read_item for read_item in st.session_state.cart]
        selected = st.selectbox("Select item to update quantity", show_item)
        new_quantity = st.number_input("Enter new quantity", step=1, format='%d')
        if st.button("Update quantity", type="primary"):
            for idx, list_item in enumerate(st.session_state.cart):
                if list_item['item'].upper() == selected['item'].upper():
                    st.session_state.cart[idx]['quantity'] = new_quantity
                    save_cart(st.session_state.cart)
                    st.success("Your Item quantity is successfully updated")


elif choice == 'Exit !!':
    st.subheader("Save and Exit the cart")
    save_cart(st.session_state.cart)
    st.success("Your cart is sucessfullt saved !!")
    st.markdown("""
                
                """)

