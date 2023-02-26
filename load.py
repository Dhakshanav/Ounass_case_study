from sqlalchemy import create_engine
from psql_con import postgres_connection 
import numpy as np
import pandas as pd
from customer import customer_data
from salesorder import salesorder_data
from salesorderitem import salesorderitem_data
from transform import transform

def load(my_conn,transform_df):
    my_conn = postgres_connection()
    cust_df = customer_data(my_conn)
    salesorder = salesorder_data(my_conn)
    item = salesorderitem_data(my_conn)
    transform_df = transform(cust_df,salesorder,item)

    #loading final data into target table
    transform_df.to_sql("data_mart.sales_order_item_flat_test",con=my_conn, if_exists='append',index=False)
    transform_df.to_csv("salesorderitemtarget.csv",index=False)
    print("targer table loaded successfully")
    return None