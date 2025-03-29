
import random
gameChoice=["stone","paper","scissor"]

#function code - to find the greatest option in the duel
def highestOption(x):
    if(x==gameChoice[0]):
        return gameChoice[1]
    elif(x==gameChoice[1]):
        return gameChoice[2]
    elif(x==gameChoice[2]):
        return gameChoice[0]

def main():
        
    # Entering Opponent choice
    print("WELCOME TO THE GAME OF STONE/PAPER/SCISSOR !! \n You can play against a second player or the AI/PC itself. \n INSTRUCTIONS: Play the Game by entering any one of the options: Stone / Paper / Scissor. The one who scores 10 wins. \n If you want to quit in the middle, press 'Q'. \n Let's Start...\n Select your opponent (Player or AI): ")
    mainMenuChoice=input().lower()
    print("")

    #code for playerVSplayer option
    if(mainMenuChoice=="player"):
        player1=player2=0
        name1=input("Enter Player(1) name: ")
        name2=input("Enter Player(2) name: ")
        #main rounds of Game
        while(player1!=3 and player2!=3):
            print(name1,"enter your choice: ")
            Player1Choice=input().lower()
            if(Player1Choice=="q"):
                break
            print(name2,"enter your choice: ")
            Player2Choice=input().lower()
            print(" ")
            if(Player2Choice=="q"):
                break
            highest=highestOption(Player1Choice)
            if(Player1Choice in gameChoice and Player2Choice in gameChoice):
                if(Player2Choice==highest):
                    player2+=1
                    print(name2,"wins this round !! 1 point goes to",name2)
                    print(" ")
                elif(Player1Choice==Player2Choice):
                    print("Both entered the same option!! No point given to anyone.")
                    print(" ")
                    continue
                else:
                    player1+=1
                    print(name1,"wins this round !! 1 point goes to",name1)
                    print(" ")
            else:
                print("Invalid Option")
                continue
        #final result of the match
        print("---------------------------------------------------------")
        if(player1>player2):
            print("CONGRATULATIONS!!!",name1,"WINS !!!")
            print(name1,"Score:",player1)
            print(name2,"Score: ",player2)
        elif(player2>player1):
            print("CONGRATULATIONS!!!",name2,"WINS !!!")
            print(name1,"Score:",player1)
            print(name2,"Score: ",player2)
        elif(player1==player2):
            print("Tie Match !!")
            print(name1,"Score: ",player1)
            print(name2,"Score: ",player2)
        else:
            print("Quiting game...")

    #code for playerVS_AI option
    else:
        player=AI=0
        name=input("Enter your name: ")
        print(" ")
        # main rounds of Game
        while(player!=3 and AI!=3):
            PlayerChoice=input("Enter your choice: ").lower()
            if(PlayerChoice=="q"):
                break
            print("AI is choosing...")
            aichoice=random.randint(0,2)
            print("AI chose: ",gameChoice[aichoice])
            print(" ")
            highest=highestOption(PlayerChoice)
            if(PlayerChoice in gameChoice):
                if(highest==gameChoice[aichoice]):
                    AI+=1
                    print("AI wins this round !! 1 point goes to AI.")
                    print(" ")
                elif(gameChoice[aichoice]==PlayerChoice):
                    
                    print("Both have entered the same option")
                    print(" ")
                else:
                    player+=1
                    print(name,"wins this round !! 1 point goes to",name)
                    print(" ")
            else:
                print("Invalid choice")
                continue

        #final result of the match
        print("---------------------------------------------------------")
        if(player>AI):
            print("CONGRATUALTIONS!!!",name,"WINS !!!")
            print(name,"Score: ",player)
            print("AI Score: ",AI)
        elif(player<AI):
            print("DEFEATED !!! AI WON. Better luck next time :) ")
            print(name,"Score: ",player)
            print("AI Score: ",AI)
        elif(player==AI):
            print("Tie Match !!")
            print(name,"Score: ",player)
            print("AI Score: ",AI)
        else:
            print("Quiting Game...")
    print(" ")
    print("Thanks for Playing.\ncreated by TRIO_MIT")
if __name__ =="__main__":
    main()




