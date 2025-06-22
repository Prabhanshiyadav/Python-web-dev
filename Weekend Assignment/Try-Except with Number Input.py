user_input = int(input("Enter the num:  "))
try:
    number = int(user_input)
    print("You entered the number:  ", number)
except ValueError:
    print("❌ Error: Please enter a valid numeric value.")


