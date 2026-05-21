import logging

#Database 
DB_name = "cart.db"
TABLE_NAME = "cart_itema"

#logging
LEVEL = logging.INFO

LOGGING_FOR = "%(asctime)s - %(levelname)s - Line:%(lineno)d - %(message)s"

MENUE_OPTIONS = [
      ("1","Add Item"),
      ("2","Clear"),
      ("3","Remove Item"),
      ("4","View Items"),
      ("5","Update quantity"),
      ("6","Get Total"),
      ("7","Search cart Item"),
      ("8","Exit !!"),

]