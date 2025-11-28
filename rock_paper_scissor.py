import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🤘🏻', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print(f"Invalid choice! Please choose {choices}.")

def display_choices(user_choice, computer_choice):
    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or \
        (user_choice == SCISSORS and computer_choice == PAPER) or \
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You wn!")
    else:
        print("Computer wins!")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Play again? (y/n): ').lower()

        if should_continue == 'n':
            print('Thanks for playing!')
            break

play_game()