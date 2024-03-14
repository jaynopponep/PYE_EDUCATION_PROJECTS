# 7. CREATING A USER INTERFACE IN THE CONSOLE

def greeting():
    # Function to display a message
    print("Hello!")


def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {num1 + num2}")


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Display a Message")
        print("2. Add Two Numbers")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            greeting()
        elif choice == '2':
            add()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
