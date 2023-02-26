from sqlalchemy import create_engine
import numpy as np
import pandas as pd

def postgres_connection():
    my_conn = create_engine('postgresql://postgres@localhost:5432/postgres')
    return my_conn