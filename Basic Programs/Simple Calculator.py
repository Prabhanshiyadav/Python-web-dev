# Simple calculator using match-case (Python 3.10+)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")

user_choice = int(input("Enter choice (1/2/3): "))

match user_choice:
    case 1:
        print(f"Sum: {num1 + num2}")
    case 2:
        print(f"Difference: {num1 - num2}")
    case 3:
        print(f"Product: {num1 * num2}")
    case _:
        print("Invalid choice")
