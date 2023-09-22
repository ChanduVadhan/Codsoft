import random

# Initialize scores
user_score = 0
computer_score = 0

# Define the choices
choices = ["rock", "paper", "scissors"]

while True:
    # Display the current scores
    print(f"User Score: {user_score} | Computer Score: {computer_score}")
    
    # Get user input
    user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
    
    # Check if the user wants to quit
    if user_choice == 'q':
        break
    
    # Check if the user's input is valid
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    # Generate computer's choice
    computer_choice = random.choice(choices)
    
    # Display user's choice and computer's choice
    print(f"User chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("User wins!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

# Display the final scores
print("Final Scores:")
print(f"User Score: {user_score} | Computer Score: {computer_score}")
