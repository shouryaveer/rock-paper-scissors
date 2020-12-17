import random

print("********Welcome to Rock Paper Scissors********")
def play():
    n = 1
    u = 0
    c = 0
    while n <= 5:
        user = input("Press r for Rock, p for Paper, s for Scissors: ")
        comp = random.choice(['r','p','s'])
        print("Computer:",comp)
        n += 1
        if user == comp:
            print("It's a tie!")
            continue
        
        if (user=='r' and comp=='s') or (user=='p' and comp=='r') \
            or (user =='s' and comp =='p'):
            u += 1
            print("You Won this round!")
            continue
        c += 1
        print("You lost this round.")
        
    print("******************************************")
    print("Final Scores are:\nUser: {}\nComputer: {}".format(u,c))

play()

