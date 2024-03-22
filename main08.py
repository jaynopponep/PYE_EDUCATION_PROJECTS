# 8. USER INTERACTION WITH THE CSV FILE
import pandas as pd

def greeting():
    print("Hello")


def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {num1 + num2}")


# add input to data function:
def add_input_to_data(filename):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Class", "DaysOfWeek"])

    name = input("Enter Name: ")
    class_name = input("Enter Class: ")
    days_of_week = input("Enter DaysOfWeek: ")

    new_row = pd.DataFrame([{"Name": name, "Class": class_name, "DaysOfWeek": days_of_week}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(filename, index=False)

    return df


def main_menu():
    filename = "data.csv"
    while True:
        print("\nMenu:")
        print("1. Display a Message")
        print("2. Add Two Numbers")
        print("3. Add Data to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            greeting()
        elif choice == '2':
            add()
        elif choice == '3':
            df = add_input_to_data(filename)
            print(df)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
