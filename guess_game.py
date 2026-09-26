import random

def guess_number_game():
    print("========================================")
    print("Welcome to the Number Guessing Game!")
    print("========================================")
    
    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user input
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            # Check the guess
            if user_guess < secret_number:
                print("Too low! Try a higher number.")
            elif user_guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You found the secret number {secret_number} in {attempts} attempts!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")

if __name__ == "__main__":
    guess_number_game()