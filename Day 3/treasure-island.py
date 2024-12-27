print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to the Treasure Island\n Your Mission is to find the treasure")
print("You are at the center of an unknown Island\n You can go either Left or Right")
Choice1 = input("Type 'L' for Left or 'R' for Right :").lower()

if( Choice1 == "l"):
    print("You came across a still River\n You want to swim or wait")
    choice2 = input("Type 'S' for swim or 'W' for wait :").lower()
    if(choice2 == "w"):
        print("You decided to wait\n And the river suddenly disappeared \n Now you can see 3 doors ahead of you")
        choice3= input("type 'R' for the Red door ,'Y' for the Yellow door or 'B' for the Blue door  :").lower()
        if( choice3 == "y"):
            print("YaY !!! You made a Great Escape")
        elif( choice3 == "r"):
            print("You fell in a pool of blood\n GAME OVER!!!")    
        else:
            print("You got teleported to the sky and you are having a great fall \n GAME OVER!!!")    
    else:
        print("The River was full of crocodiles\n GAME OVER!")    
else:
    print("You fall in a pit\n GAME OVER!")


