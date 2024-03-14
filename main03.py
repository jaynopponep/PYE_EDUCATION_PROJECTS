# 3. INTRO TO PANDAS LIBRARY WITH PYTHON!
import pandas as pd
from io import StringIO

# Sample data for a CSV file
data = """Name,Age,City
Alice,28,New York
Bob,22,Los Angeles
Charlie,35,Chicago
Diana,40,Boston
Evan,31,San Francisco"""

# Using StringIO to simulate a file object
file_obj = StringIO(data)

# Creating a DataFrame from the file object
df = pd.read_csv(file_obj)


# Function to retrieve data by name
def get_data_by_name(name):
    return df[df['Name'] == name]


print(get_data_by_name("Bob"))
