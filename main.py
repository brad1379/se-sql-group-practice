import pandas as pd
import sqlite3


conn = sqlite3.connect('data.sqlite')

#  -------------- SELECT all product data --------------
products = pd.read_sql("""
SELECT *
 FROM products;
""", conn)

print(products)