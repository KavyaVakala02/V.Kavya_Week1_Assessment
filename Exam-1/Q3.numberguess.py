import random  # To generate a random number
def guess_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    while True:
        # Ask the user for their guess
        guess = int(input("Enter your guess: "))
        if guess < target_number:
            print("Too Low! Try again.")
        elif guess > target_number:
            print("Too High! Try again.")
        else:
            print("Congratulations! You guessed the number correctly.")
            break  # Exit the loop when the user guesses the correct number
# Main function to run the game
def main():
    guess_number()
# Run the program
main()
