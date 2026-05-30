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
