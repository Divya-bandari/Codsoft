import random

def get_user_choice():
    """Get and validate user input for rock, paper, or scissors"""
    while True:
        user_input = input("Choose rock, paper, or scissors (r/p/s): ").lower()
        if user_input in ['r', 'p', 's']:
            return user_input
        print("Invalid choice. Please enter 'r', 'p', or 's'.")

def get_computer_choice():
    """Generate a random choice for the computer"""
    return random.choice(['r', 'p', 's'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game rules"""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        return 'user'
    else:
        return 'computer'

def display_choices(user_choice, computer_choice):
    """Display the choices in a user-friendly way"""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f"\nYour choice: {choices[user_choice]}")
    print(f"Computer's choice: {choices[computer_choice]}")

def display_result(result, scores):
    """Display the game result and current scores"""
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins!")
    
    print(f"\nCurrent Scores - You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}")

def play_again():
    """Ask if the user wants to play another round"""
    while True:
        choice = input("\nPlay again? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' or 'n'.")

def print_game_header():
    """Print the game header with instructions"""
    print("\n" + "="*40)
    print("ROCK-PAPER-SCISSORS GAME".center(40))
    print("="*40)
    print("Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beat Paper")
    print("- Paper beats Rock")
    print("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors")
    print("="*40 + "\n")

def main():
    """Main game function"""
    scores = {'user': 0, 'computer': 0, 'tie': 0}
    print_game_header()
    
    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        scores[result] += 1
        
        # Display results
        display_choices(user_choice, computer_choice)
        display_result(result, scores)
        
        # Ask to play again
        if not play_again():
            print("\nThanks for playing!")
            print(f"Final Scores - You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}")
            break

if __name__ == "__main__":
    main()