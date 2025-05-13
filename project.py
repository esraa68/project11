import random

# Available options
options = ['Rock', 'Paper', 'Scissors']
# Initialize scores
user_score = 0
cpu_score = 0

while True:
    # Random choice by CPU
    cpu_choice = random.choice(options)

    # Get user's input
    user_choice = input("Please enter a choice (Rock, Paper, Scissors), or type 'quit' to stop: ")
    user_choice = user_choice.capitalize()  # Ensure correct capitalization

    # Exit condition
    if user_choice == 'Quit':
        print("Game over!")
        break

    # Validate user input
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # Show choices
    print(f"CPU chose: {cpu_choice}")
    print(f"You chose: {user_choice}")

    # Determine the winner
    if user_choice == cpu_choice:
        print("It's a tie!")
    elif (user_choice == 'Rock' and cpu_choice == 'Scissors') or \
         (user_choice == 'Scissors' and cpu_choice == 'Paper') or \
         (user_choice == 'Paper' and cpu_choice == 'Rock'):
        print("You win this round!")
        user_score += 1
    else:
        print("CPU wins this round!")
        cpu_score += 1

    # Display scores
    print(f"Score -> You: {user_score}, CPU: {cpu_score}\n")