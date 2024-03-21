def calc(operation):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if operation == "add":
        print(f"The sum is: {num1 + num2}")
    elif operation == "subtract":
        print(f"The difference is: {num1 - num2}")
    elif operation == "multiply":
        print(f"The product is: {num1 * num2}")
    elif operation == "divide":
        print(f"The quotient is: {num1 / num2}")
    elif operation == "exponent":
        print(f"The exponential value is: {num1 ** num2}")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            calc("add")
        elif choice == '2':
            calc("subtract")
        elif choice == '3':
            calc("multiply")
        elif choice == '4':
            calc("divide")
        elif choice == '5':
            calc("exponent")
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
