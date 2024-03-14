# 5. INPUT FLOW WITH CSV FILES
import pandas as pd
from io import StringIO

data = """Name,Class,DaysOfWeek
"""


# Function to add user input to the data string
def add_input_to_data(data):
    # Getting user input
    name = input("Enter Name: ")
    class_name = input("Enter Class: ")
    days_of_week = input("Enter DaysOfWeek: ")

    # Appending user input to data
    new_row = f"{name},{class_name},{days_of_week}\n"
    data += new_row
    return data


data = add_input_to_data(data)

# Convert the string data to a file-like object
data_io = StringIO(data)

# Read the CSV data into a DataFrame
df = pd.read_csv(data_io)

# Display the DataFrame
print(df)
