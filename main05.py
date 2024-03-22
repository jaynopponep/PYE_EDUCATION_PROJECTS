# 5. INPUT FLOW WITH CSV FILES
import pandas as pd
from io import StringIO

data = """Name,Class,DaysOfWeek
"""

# Let's create a function that adds rows to the data table:


def add_input_to_data(data):
    name = input("Enter name: ")
    class_name = input("Enter class name: ")
    days_of_week = input("Enter DaysOfWeek: ")

    new_row = f"{name},{class_name},{days_of_week}\n"
    data += new_row
    return data
    # this will return data, which now has new_row added to it!!


data = add_input_to_data(data)
data_io = StringIO(data)
df = pd.read_csv(data_io)
# Now we are simply just reading the new data table, and then we are going to print it out!
print(df)
# When we run the program, it should prompt us to put three inputs, and it will show us the new table.