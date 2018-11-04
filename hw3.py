"""This module makes a dataframe"""

# Packages
from urllib import request
import os.path
import pandas as pd

# Get the URL data

def make_df(num_rows, file):
    """This function makes a dataframe"""
    d_f = pd.read_csv(file)
    columns = ['JURISDICTION NAME', 'PERCENT FEMALE', 'PERCENT MALE']
    my_df = pd.DataFrame(data=d_f, columns=columns)

    if len(d_f.index) <= num_rows:
        raise ValueError("DataFrame should have more than 2 rows.")
    return my_df

def download(url, filename):
    """This function downloads a dataset"""
    if os.path.isfile(filename):
        print("Already present %s." % filename)
    else:
        try:
            print("Downloading %s" % filename)
            request.urlretrieve(url, filename)
        except:
            raise ValueError("file doesn't exist")

def has_right_columns(d_f):
    """This function checks if the dataframe has the correct column names"""
    col_names = list(d_f.columns.values)

    if (col_names[0] == 'JURISDICTION NAME' and col_names[1] == 'PERCENT FEMALE'
            and col_names[2] == 'PERCENT MALE'):
        return True
    return False

def columns_contain_correct_dtype(d_f):
    """This function checks if the dataframe has the correct column datatypes"""
    if (d_f['JURISDICTION NAME'].dtypes == 'int64' and d_f['PERCENT FEMALE'].dtypes == 'float64'
            and d_f['PERCENT MALE'].dtypes == 'float64'):
        return True
    return False

def there_are_atleast_10_rows(d_f):
    """This function checks if the dataframe has at least 10 rows"""
    if len(d_f.index) >= 10:
        return True
    return False
