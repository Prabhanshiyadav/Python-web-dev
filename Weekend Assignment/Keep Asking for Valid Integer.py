while True:
    user_input = input("Enter an integer:  ")
    try:
        number = int(user_input)
        print(f"You entered: {number}")
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

