import random
# Rock, Paper, Scissors ASCII art
rock = '''                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a \n '''

paper = '''8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88      \n   '''


scissors = '''                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  \n'''


user_choice = int(input("What do you Choose? Type 0 for Rock, 1 for Paper, for Paper or 2 for Scissors : "))

if user_choice < 0 or user_choice > 2:
    print("Invalid input! Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")
    exit()
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else :
    print(scissors)

computer_choice = random.randint(0,2)
print("\nComputer Choice: \n ")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else :
    print(scissors)

# #game_logic

# if user_choice == computer_choice :
#     print("Game Draw")
#     #Rock conditions
# elif user_choice == 0  and computer_choice == 1:
#     print("You Lose")   
# elif user_choice == 0  and computer_choice == 2:
#     print("You won")   

#     #Paper Condition
# elif user_choice == 1  and computer_choice == 0:
#     print("You won")   
# elif user_choice == 1  and computer_choice == 2:
#     print("You lose")  
    
#     #Scissors Condition
# elif user_choice == 2  and computer_choice == 0:
#     print("You Lose")   
# elif user_choice == 2  and computer_choice == 1:
#     print("You won")          

#consice Game Logic
if user_choice == computer_choice:
    print("Game Draw")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You won!")
else:
    print("You lose.")