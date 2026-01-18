import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Generate a random number between the specified range
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while True:
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

number_guesser()

