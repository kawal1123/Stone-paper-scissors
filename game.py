from random import randint
computer_wins = 0
player_wins = 0
while player_wins<5 +1 and computer_wins<5 +1:
    print(computer_wins)
    print(player_wins)
    print("...Stone...")
    print("...Paper...")
    print("...Scissors...")
    rand= randint(0,2)
    player= input("enter your choice: ")
    if rand == 0:
        computer = "stone"
        print("computer chooses: ",computer)
    elif rand ==1:
        computer = "paper"
        print("computer chooses: ",computer)
    else:
        computer ="scissors"
        print("computer chooses: ",computer)

    if player == computer:
        print("wooohhh its a tieeee")
    elif player == "stone" :
        if computer  == "paper":
            print("computer wins")
            computer_wins = computer_wins+1
        elif computer  == "scissors":
            print("player wins")
            player_wins = player_wins+1
    elif player == "paper":
        if computer =="scissors":
            print("computer wins")
            computer_wins = computer_wins+1
        elif computer == "stone":
            print("player wins")
            player_wins = player_wins+1
    elif player == "scissors":
        if computer ==" stone":
            print("computer wins")
            computer_wins = computer_wins+1
        elif computer =="paper":
            print("player wins")    
            player_wins = player_wins+1            
    else:
        print("invalid input ")                    