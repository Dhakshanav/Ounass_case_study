from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from psql_con import postgres_connection 

def salesorderitem_data(my_conn):
    #postgres connection
    my_conn = postgres_connection()

    #fetching salesorderitem data
    salesorderitem_df = pd.read_sql_query('select * from data_mart.salesorderitem;',con=my_conn)
    salesorderitem_df = salesorderitem_df.drop_duplicates(subset=['item_id','order_id'],keep=False)
    return salesorderitem_df