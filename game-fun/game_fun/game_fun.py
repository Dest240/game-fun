import random
#in poetry shell,python3,>>>import game_fun>>>dir(game_fun)>>>game_fun.RPS('','')
class RPS():
    def __init__(self,arg1,arg2): # Are the user input and the random choice.
        self.arg1 = self.take_user_input()
        self.arg2 = self.random_selection()
        self.main()
    
    def take_user_input(self): #Greet and take user input ASCII art and random
        while True:
            user_input = input("Enter your selection rock paper scissors: " ).lower();
            if user_input in ['rock','paper','scissors']:
                self.arg1 = user_input
                return self.arg1
            else:
                print("Invalid input. Try again!");
                
    def random_selection(self):
        selection_list = ['rock', 'paper', 'scissors']
        choice = random.choice(selection_list)
        self.arg2 = choice
        return self.arg2
    
    def main(self): #user input check
        if self.arg1 == 'rock':
            self.rock();
        if self.arg1 == 'paper':
            self.paper();
        if self.arg1 == 'scissors':
            self.scissors();
    
    def rock(self): #random check
        if self.arg2 == 'rock':
            print("We Tied");
            print('''
            
            
            ''');#ASCII ART
        if self.arg2 == 'paper':
            print("You LOSE. Paper beats Rock.");
            print('''
            
            
            ''');#ASCII ART   
        if self.arg2 == 'scissors':
            print("You Win");
            print('''
            
            
            ''');#ASCII ART            

