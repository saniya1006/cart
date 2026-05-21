import sqlite3
import logging

from config import DB_name, TABLE_NAME
logger= logging.getLogger(__name__)

def get_db_connection(): #databse se connection
    conn = sqlite3.connect("cart.db")
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS cart_items (                
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   item TEXT NULL UNIQUE,
                   price REAL NOT NULL,
                   quantity REAL NOT NULL
                   )
                   
                   """) #

    conn.commit()
    conn.close()
    logging.info(f"Databse inittialized successfully")


def load_cart():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT item , price, quantity FROM cart_items")
        rows = cursor.fetchall()
        conn.close

        cart = []
        for row in rows:
            cart.append({
                "item" : row[0],
                "price" :  row[1],
                "quantity" : row[2]})
        
        logging.info("Cart Loaded Succcessfully")
        return cart
    
    except Exception as e:
        logging.info(f"databse connection failed {e}")
        return []

def save_cart(cart):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cart_items")
    

        #INSERT DATA INTO  THE cart
        for cart_item in cart:
            cursor.execute(
                "INSERT INTO cart_items (item , price , quantity) VALUES(? , ? , ? )",
                (cart_item["item"] , cart_item["price"] , cart_item["quantity"])
            )
        conn.commit()
        conn.close()
        logging.info(f"cart saved into the databse table: cart_items")
    except Exception as e:
        logging. info(f"failed to saved cart in memory {e}")
