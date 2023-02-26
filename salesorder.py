from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from psql_con import postgres_connection 

def salesorder_data(my_conn):
    #postgres connection
    my_conn = postgres_connection()

    #fetching salesorder data
    salesorder_df = pd.read_sql_query('select * from data_mart.salesorder;',con=my_conn)
    salesorder_df = salesorder_df.rename(columns={'id': 'order_id'})
    return salesorder_df