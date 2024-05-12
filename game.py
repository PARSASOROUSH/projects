import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 101)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it.")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number()