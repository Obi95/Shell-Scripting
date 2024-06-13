import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors")
    player_choice = input().lower()
    
    if player_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_game()
