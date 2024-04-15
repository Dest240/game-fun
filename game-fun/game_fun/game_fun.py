import random

def take_user_input(): 
    while True:
        user_input = input("Enter your selection rock paper scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Try again!")

def random_selection():
    selection_list = ['rock', 'paper', 'scissors']
    return random.choice(selection_list)

def main(user_input, random_choice): 
    if user_input == 'rock':
        rock(random_choice)
    elif user_input == 'paper':
        paper(random_choice)
    elif user_input == 'scissors':
        scissors(random_choice)

def rock(random_choice): 
    if random_choice == 'rock':
        print("We Tied")
    elif random_choice == 'paper':
        print("You LOSE. Paper beats Rock.")
    elif random_choice == 'scissors':
        print("You Win")

def paper(random_choice): 
    if random_choice == 'rock':
        print("You Win")
    elif random_choice == 'paper':
        print("We Tied")
    elif random_choice == 'scissors':
        print("You LOSE. Scissors beats Paper.")

def scissors(random_choice): 
    if random_choice == 'rock':
        print("You LOSE. Rock beats Scissors.")
    elif random_choice == 'paper':
        print("You Win")
    elif random_choice == 'scissors':
        print("We Tied")

if __name__ == "__main__":
    user_input = take_user_input()
    random_choice = random_selection()
    main(user_input, random_choice)

