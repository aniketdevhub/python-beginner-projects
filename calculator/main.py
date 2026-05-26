# Function to add two numbers
def add(x, y):
    return x + y


# Function to subtract two numbers
def subtract(x, y):
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    return x * y


# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y


def calculator():
    print("=== Welcome to the Python Calculator! ===")

    while True:
        # Display options to the user
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if choice == "5":
            print("Goodbye! Thanks for using the calculator.")
            break

        # Check if choice is one of the valid options
        if choice in ("1", "2", "3", "4"):
            try:
                # Get the numbers and convert them to floats
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            # Call the appropriate function based on user choice
            if choice == "1":
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

        else:
            print("Invalid Input. Please choose a valid option (1-5).")


# This actually starts the calculator program
if __name__ == "__main__":
    calculator()
