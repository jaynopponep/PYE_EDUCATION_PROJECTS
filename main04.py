# 4. PRACTICE WITH THE PANDAS LIBRARY IN PYTHON
import pandas as pd
from io import StringIO

data = """Month,WeatherType,Days,Season
April,Breezy,30,Spring
December,Cold,31,Winter
August,Hot,31,Summer
"""

data_io = StringIO(data)
df = pd.read_csv(data_io)

total = df["Days"].sum()
print(total)

