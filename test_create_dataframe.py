"""This module tests hw3.py."""

import hw3

DATA = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD"
FILE = "data.csv"

def test_create_dataframe(num_rows=0):
    """This function tests that hw3.py returns a dataframe in the correct format."""

    d_f = None

    try:
        hw3.download(DATA, FILE)
    except ValueError:
        print("File does not exist.")
        return False

    try:
        d_f = hw3.make_df(num_rows, FILE)
    except ValueError:
        print("File should have more than 2 rows.")
        return False

    columns = hw3.has_right_columns(d_f)
    correct_dtype = hw3.columns_contain_correct_dtype(d_f)
    atleast_10_rows = hw3.there_are_atleast_10_rows(d_f)

    if columns and correct_dtype and atleast_10_rows:
        print("true")
        return True
    print("false")
    return False

test_create_dataframe(2)
