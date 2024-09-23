import random

user_wins=0
computer_wins=0

options =["rock","paper","scissors"]

while True:
    user_input=input("type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
        #if user input is not in this list
    if user_input not in options: 
        continue
    random_number = random.randint(0,2)
    # rock:0,paper:1,scissors:2
    computer_pick =options[random_number]
    print("computer picked",computer_pick +".")
    
    if user_input == "rock" and computer_pick =="scissors":
        print("you win!")
        user_wins +=1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("you win!")
        user_wins +=1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("you win!")
        user_wins +=1
        continue
    elif user_input == computer_pick:
        print("it's a tie!")
    else:
        print("You lost!")  
        computer_wins +=1  
    
    # if user_input == computer_pick:
    #     print("draw")
print("You won",user_wins,"times")  
print("the computerwon",computer_wins,"times.")   
print("goodbye!")    