# 7. CREATING A USER INTERFACE IN THE CONSOLE

def greeting():
    print("Hello")


def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {num1 + num2}")


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Display a message")
        print("2. Add Two Numbers")
        print("3. Exit the program")
        choice = input("Enter a choice (1-3):")

        if choice == "1":
            greeting()
        elif choice == "2":
            add()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()


