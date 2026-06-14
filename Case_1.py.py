import pandas as pd
import pymysql

connection = pymysql.connect(
    host="35.199.115.174",
    user="looqbox-challenge",
    password="looq-challenge",
    database="looqbox-challenge"
)

# Case 1

def retrieve_data(product_code: int, store_code: int, date: list):
   
    """
    Retrieve sales from data_product_sales!

    Use 0 to ignore product_code or store_code filters, and [0] to ignore date filter.
    
    Parameters:
        1) product_code (int): Product code
        2) store_code (int): Store code
        3) date (list): Start (first) and end (second) dates
            Example:
            ['2019-01-01', '2019-01-31']
    """

    if date != [0]:
        start = date[0]
        end = date[1]


    query = "SELECT * FROM data_product_sales WHERE 1=1"

    if product_code != 0:
        query += f" AND PRODUCT_CODE = {product_code}"

    if store_code != 0:
        query += f" AND STORE_CODE = {store_code}"

    if date != [0]:
        query += f" AND `DATE` BETWEEN '{start}' AND '{end}'"

    df_filtered = pd.read_sql(query, connection)

    return df_filtered
