import random #importing library 

def get_choices(): #function, everything that is indented
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"] #list, store multiple items in single variable
    computer_choice = random.choice(options) #choose random item from list
    return {"player": player_choice, "computer": computer_choice} #dictionary

def check_win(p, c):
    print(f"You chose {p}, computer chose {c}")
    if p == c: return "It's a tie!"
    elif p == "rock": 
        if c == "scissors": return "Rock smashes scissors! You win!"
        else: return "Paper covers rock! You lose!"
    elif p == "scissors": 
        if c == "rock": return "Rock smashes scissors! You lose!"
        else: return "Scissors cuts paper! You win!"
    elif p == "paper": 
        if c == "rock": "Paper covers rock! You win!"
        else: return "Scissors cuts paper! You lose!"

choices = get_choices()
print(check_win(choices["player"], choices["computer"]))