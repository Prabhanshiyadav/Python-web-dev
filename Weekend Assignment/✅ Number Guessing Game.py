import random
secret_no = random.randint(1,10)
print("Welcome to the Game!")
print("Guess the number between 1 to 10: ")
while True:
    try:
        guess = int(input("Enter the number:  "))
        if guess < secret_no:
            print("Too low, Try again!")
        elif guess > secret_no:
            print("Too High, Try again!")
        else:
            print("Congratulations, You are right!!")
            break
    except ValueError:
        print("Please enter a valid number")
