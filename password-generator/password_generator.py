import random
import string

def generate_password():
    print("========================================")
    print("Welcome to the Secure Password Generator!")
    print("========================================")
    
    # Character pools
    letters = string.ascii_letters  # Uppercase and lowercase letters
    numbers = string.digits         # Digits from 0 to 9
    symbols = string.punctuation    # Special characters (!, @, #, etc.)
    
    try:
        # Get user preferences
        nr_letters = int(input("How many letters would you like in your password? "))
        nr_numbers = int(input("How many numbers would you like? "))
        nr_symbols = int(input("How many symbols would you like? "))
        
        # Build the password list
        password_list = []
        
        for _ in range(nr_letters):
            password_list.append(random.choice(letters))
            
        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))
            
        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))
            
        # Shuffle the list to make it random and secure
        random.shuffle(password_list)
        
        # Convert list to string
        final_password = "".join(password_list)
        
        print("\n----------------------------------------")
        print(f"Your secure password is: {final_password}")
        print("----------------------------------------")
        
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    generate_password()