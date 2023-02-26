from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import configparser
config = configparser.ConfigParser()
from psql_con import postgres_connection
from customer import customer_data
from salesorder import salesorder_data
from salesorderitem import salesorderitem_data

def transform(customer,salesorder,saleorderitem):

    # reading config file
    config.read('config.ini')

    #joining salesorderitem and salesorder table
    join_order_item = pd.merge(saleorderitem,salesorder, on='order_id', how = 'left')

    #joining with customer table
    final_join = pd.merge(join_order_item,customer, on='customer_id', how = 'left')

    #selecting required columns for final df
    select_cols = config['final_columns']['cols'].split(',')
    final_df = final_join[select_cols]
    final_df['load_date'] = pd.Timestamp.now()

    return final_df

    # #calling functions to get required input for transformation
    # my_conn = postgres_connection()
    # cust_df = customer_data(my_conn)
    # salesorder = salesorder_data(my_conn)
    # item = salesorderitem_data(my_conn)

    # # reading config file
    # config.read('config.ini')

    # #joining salesorderitem and salesorder table
    # join_order_item = pd.merge(item,salesorder, on='order_id', how = 'left')

    # #joining with customer table
    # final_join = pd.merge(join_order_item,cust_df, on='customer_id', how = 'left')

    # #selecting required columns for final df
    # select_cols = config['final_columns']['cols'].split(',')
    # final_df = final_join[select_cols]
    # final_df['load_date'] = pd.Timestamp.now()

    # return final_df

