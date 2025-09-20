import random as r

def computer_choice():
    cc=r.randint(1,3)
    return cc

def game(user,computer):
      #rock,paper,scissors = 1,2,3
      result ={
           (1,3),
           (2,1),
           (3,2)
      }

      if (user,computer) in result:
           return 1
      elif (computer,user) in result:
           return 0
      else:
           return None
      

def score_update(user,computer,scores):
    scores['user'] += user
    scores['computer'] += computer
    return scores


def display(scores):
     print("\n--------LeaderBoard-------")
     print(f"{'User Score':<12} {'Computer Score':<15}")
     print(f"{scores['user']:<12} {scores['computer']:<15}")


scores={
     'user':0,
     'computer':0
}

print("Welcome to Rock, Paper, Scissors Game.....")
while True:
     try:
        user = int(input('''choose
        1 for Rock 
        2 for Paper
        3 for Scissors
        :- '''))
     except:
          print("invalid input please enter 1,2 or 3")
          continue

     computer=computer_choice()
     choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
     print(f"\nYou chose {choices.get(user,'Invalid')}, computer chose {choices.get(computer,'Invalid')}")
     if user == computer:
         print("\nIts a Draw")
         
     elif game(user,computer)==1:
          print(f"You Won...")
          score_update(1,0,scores)
          
     elif game(user,computer)==0:
          print(f"you lost... ")
          score_update(0,1,scores)
          
     elif game(user,computer)==None:
          print("Invalid input")
          
     display(scores)
     c = input("\nwant to continue press(y/n)").strip().lower()
     if c == 'y':
          continue
     elif c == 'n':
          print("\nThanks for playing and the final scores:")
          display(scores)
          break    
     else:
          print("Invalid input....") 

