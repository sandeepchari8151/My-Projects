import random as rd
import os

file = "scores.txt"

def load_score():
    scores={}

    if os.path.exists(file):
        with open(file,"r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data)==3:
                    name,wins,losses=data
                    scores[name]=(int(wins), int(losses))
    return scores

def highest_scores(scores):
    best_player = None
    best_percentage = 0

    for name, (wins,losses) in scores.items():
        total = wins+losses
        if total >= 10:
            percentage = (wins/total) *100
            if percentage > best_percentage:
                best_percentage = percentage
                best_player = name
    if best_player:
        return best_player,best_percentage
    else:
        return None,0
    


scores= load_score()

def leaderBoard(scores):
    result = []
    for name, (wins, losses) in scores.items():
        total = wins + losses
        if total > 0:   # avoid divide by zero
            win_percentage = (wins / total) * 100
        else:
            win_percentage = 0
        result.append([name, wins, losses, win_percentage])
    
    # sort by win_percentage (highest first)
    result.sort(key=lambda x: x[3], reverse=True)

    print("\n===== Leaderboard =====")
    print(f"{'Name':<10} {'Wins':<5} {'Losses':<7} {'Win%':<6}")
    print("-" * 35)
    for name, wins, losses, win_percentage in result:
        print(f"{name:<10} {wins:<5} {losses:<7} {win_percentage:.2f}")


    

def save_score(scores):
    with open ("scores.txt","w") as f:
        for name,(wins, losses) in scores.items(): 
            f.write(f"{name},{wins},{losses}\n")
                               


def playgame():
    computer_guess = rd.randint(1,100)
    count = 5
    while True:
        try:
            user_guess = int(input("\nGuess a Number between 1 - 100...\nwithin five chances : "))
        except ValueError:
            print("\n Invalid Input... Please enter only numbers.")
            continue 
    
        if user_guess == computer_guess:
          if count == 5:
             n = "attempt"
          else:
             n = "attempts"
          print(f"\nCongratulations...\nYou guessed it correct in {6 - count} {n}")
          return 'win'
    
        elif count == 1:
           print(f"\nYou have used all the chances.The correct guess is {computer_guess}...\nTry again next time..")
           return 'lose'
           
        elif user_guess > computer_guess:
           count-=1
           print(f"\nYour guess is too high, Choose lower one, Remaining chances = {count}...")
    
        else:
           count-=1
           print(f"\nYour guess is too low, Choose higher one, Remaining chances = {count}...")


#Start...................

name = input("Enter Your name to start the game... \n")

if name in scores:
    wins, losses = scores[name]
    print(f"Hey welcome back {name}, your currect score: wins = {wins} and losses = {losses}")
else:
    wins,losses = 0,0
    print(f"welcome {name}, your currect score: wins = {wins} and losses = {losses}")


while True:
    result = playgame()
    if result == 'win':
        wins +=1
    else:
        losses +=1
    
    scores[name]=(wins,losses)
    save_score(scores)

    b_player,b_percentage =highest_scores(scores) 

    while True:
        choice = input("\nDo you want play again, press (y/n) ").strip().lower()
        if choice == 'n':
            print(f"Final Score: Wins = {wins}, Losses = {losses}\n")
            print("\nThanks for playing! Goodbye.\n")
            print(f"Best player so far is {b_player} with {round(b_percentage,2)}% win rate..")
            n = input("Do you want to check top leaderboard players (y/n) ").strip().lower()
            if n =='y':
                leaderBoard(scores)
            elif n =='n':
                exit()
            else:
                print("enter valid input...")

            
            
        elif choice == 'y':
            break
        else:
            print("\nPlease enter only 'y' or 'n'.")




   

