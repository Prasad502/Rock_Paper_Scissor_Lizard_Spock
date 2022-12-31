import random,sys

global ai_score,user_score,User_Name

def prs(User_Name):
    global ai_score, user_score
    ai_score = 0
    user_score = 0
    
    player = input('\nPick One! (rock/paper/scissor/lizard/spock): ')
    ai = random.randint(1,3)
    
    if (ai == 1):
        ai_player = "rock"
    elif (ai == 2):
        ai_player = "paper"
    elif (ai == 3):
        ai_player = "scissor"
    elif (ai == 4):
        ai_player = "lizard"
    elif (ai == 5):
        ai_player = "spock"
            
    print("Computer Played: " + str(ai_player))
    print(User_Name + " Played: " + str(player))
    
    if ((ai_player == "rock" and player == "lizard") or (ai_player == "rock" and player == "scissor")):
        print("Computer Wins!!\n")
        ai_score += 1

    elif ((ai_player == "paper" and player == "rock") or (ai_player == "paper" and player == "spock")):
        print("Computer Wins!!\n")
        ai_score += 1

    elif ((ai_player == "scissor" and player == "paper") or (ai_player == "scissor" and player == "lizard")):
        print("Computer Wins!!\n")
        ai_score += 1

    elif ((ai_player == "lizard" and player == "spock") or (ai_player == "lizard" and player == "paper")):
        print("Computer Wins!!\n")
        ai_score += 1
        
    elif ((ai_player == "spock" and player == "scissor") or (ai_player == "spock" and player == "rock")):
        print("Computer Wins!!\n")
        ai_score += 1
    
    else:
        print("You Win!!\n")
        user_score += 1
    
def Check_Score():
    global User_Name
    print("Computer Score : ", ai_score)
    print(User_Name + " Score : ", user_score + "\n")

def main():
    global User_Name
    print("---- Welcome to Rock-Paper-Scissor-Lizard-Spock game ----")
    User_Name = input("Enter Your Name : ")
    
    while(True):
        print("1. Play Rock-Paper-Scissor-Lizard-Spock \n2. Check Score \n3. Exit")
        Choice = int(input("\nEnter Your Choice (1 / 2 / 3) : "))
        if (Choice == 1):
            prs(User_Name)
        elif (Choice == 2):
            Check_Score()
        elif (Choice == 3):
            sys.exit()
    
    
if __name__ == '__main__':
    main()
    