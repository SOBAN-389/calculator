from add import add
from subtract import subtract
from multiply import multiply
from divide import divide


def main():
    while True:
        try:
            # Input numbers and operator
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            # Perform calculation based on operator
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue

            # Display result
            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        # Ask user if they want to quit
        quit_choice = input("Do you want to quit? (Y for Yes, N for No): ").upper()
        if quit_choice == 'Y':
            break


if __name__ == "__main__":
    main()
