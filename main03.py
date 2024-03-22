# 3. INTRO TO PANDAS LIBRARY WITH PYTHON!
import pandas as pd
from io import StringIO

data = """Name,Age,City
Alice,28,New York
Bob,22,Los Angeles
Charlie,35,Chicago
Diana,40,Boston
Evan,31,San Francisco"""

file_obj = StringIO(data)

df = pd.read_csv(file_obj)


def get_data_by_name(name):
    return df[df['Name'] == name]


print(get_data_by_name('Charlie'))

