import numpy as np
import pandas as pd
from transform import transform
import unittest
from pandas.testing import assert_frame_equal

class TestTransformation(unittest.TestCase):
    def test_transform(self):
    
        cust_data = {'customer_id' : [1],
               'customer_name' : ['wasim akram'],
               'last_name' :  ['akram'],
               'customer_gender' : ['Male'],
               'customer_email' : ['wasimak@gmail.com'],
               'billing_address' : [' 105 Alain'],
               'shipping_address' : [' 105 Alain']}
        cust_df = pd.DataFrame(cust_data)

        salerorder_data = {'order_id' : [1],
                       'customer_id' : [1],
                       'order_number' : ["AOO123"],
                       'created_at' : ["2022-12-23 09:12:23"],
                       'modified_at' : ["2022-12-23 09:12:23"],
                       'order_total' : [235.10],
                       'total_qty_ordered' : [2]}

        salesorder_df = pd.DataFrame(salerorder_data)

        salesitems_data = {'item_id' : [1],
                       'order_id' : [1],
                       'product_id' : [1],
                       'product_sku' : ["AOO123"],
                       'product_name' :["white shirt"],
                       'qty_ordered' : [2],
                       'price' : [235.10],
                       'line_total' : [2],
                       'created_at' : ["2022-12-23 09:12:23"],
                       'modified_at' : ["2022-12-23 09:12:23"],}

        item_df = pd.DataFrame(salesitems_data)

        actual_df = transform(cust_df,salesorder_df,item_df).drop('load_date',axis=1)

        expected_data = {'item_id': [1],
                     'order_id': [1],
                     'order_number': ["AOO123"],
                     'created_at_x': ["2022-12-23 09:12:23"],
                     'order_total': [235.10],
                     'total_qty_ordered': [2],
                     'customer_id': [1],
                     'customer_name': ['wasim akram'],
                     'customer_gender': ['Male'],
                     'customer_email': ['wasimak@gmail.com'],
                     'product_id' : [1],
                     'product_sku': ["AOO123"],
                     'product_name': ["white shirt"],
                     'price': [235.10],
                     'line_total': [2],
                     'qty_ordered': [2],}

        expected_df = pd.DataFrame(expected_data)
        assert_frame_equal(actual_df,expected_df)

if __name__ == '__main__':
    unittest.main()
