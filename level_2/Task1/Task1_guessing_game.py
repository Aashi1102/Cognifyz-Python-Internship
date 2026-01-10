# Guessing Game 

import random 

def guessing_game():

    number_to_guess = random.randint(1,100)
    max_attempts =10
    attempts = 0
   

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")        
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess:"))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")

            elif guess < number_to_guess:
                print("Too low! Try again.")

            elif guess > number_to_guess:   
                print("Too high! Try again.")

            else:
                print("Congratulations! You've guessed the number!")

                return   

        except ValueError:
            print("Invalid input. Please enter a valid number.")    


    print(f"Congratulations! You've guessed the number in {attempts} attempts 🎉")

    

guessing_game()
