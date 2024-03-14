# 6. HOW TO STORE INPUT DATA WITH PANDAS
import pandas as pd
def add_input_to_data(filename):
    # Read existing data
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Class", "DaysOfWeek"])

    # Getting user input
    name = input("Enter Name: ")
    class_name = input("Enter Class: ")
    days_of_week = input("Enter DaysOfWeek: ")

    # Create a new row and append to the dataframe
    new_row = {"Name": name, "Class": class_name, "DaysOfWeek": days_of_week}
    df = df.append(new_row, ignore_index=True)

    # Write the updated dataframe to the file
    df.to_csv(filename, index=False)

    return df

# File to store the data
filename = "data.csv"

df = add_input_to_data(filename)

# Display the DataFrame
print(df)