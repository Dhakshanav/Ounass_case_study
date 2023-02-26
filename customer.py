from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from psql_con import postgres_connection 

def customer_data(my_conn):
    #postgres connection
    my_conn = postgres_connection()

    #fetching customer data
    cust_df = pd.read_sql_query('select * from data_mart.customer;',con=my_conn)
    cust_df['customer_name'] = cust_df['first_name'] + cust_df['last_name']
    cust_df = cust_df.rename(columns = {'id': 'customer_id','gender':'customer_gender','email':'customer_email'})
    return cust_df