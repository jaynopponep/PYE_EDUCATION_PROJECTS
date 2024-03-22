# 6. HOW TO STORE INPUT DATA WITH PANDAS
import pandas as pd


def add_input_to_data(filename):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Class", "DaysOfWeek"])

    # Get user input:
    name = input("Enter your name: ")
    class_name = input("Enter your class name: ")
    days_of_week = input("Enter DaysOfWeek: ")

    # let's create a new row, then append it to the data frame
    new_row = pd.DataFrame([{"Name": name, "Class": class_name, "DaysOfWeek": days_of_week}])
    df = pd.concat([df, new_row], ignore_index=True)
    # ^ Here, we set df = df + new_row for simplicity

    df.to_csv(filename, index=False)

    return df

# Let's try to use this function:


filename = "data.csv"  # Create a new csv file (a real one!)
df = add_input_to_data(filename)
print(df)

