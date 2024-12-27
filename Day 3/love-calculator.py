print("Welcome to the Love Calculator")

name1 = input("What is your Name? \n")
name2 = input("What is their Name? \n")

#.lower function converts the strings in lower case
#.count("") function use to count the no. of times a alphabet is written (this is CaSe Sensitive) 

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love= l + o + v + e

love_score = str(true) + str(love)

if(int(love_score)<10 or int(love_score)>90):
    print(f"Your Score is {love_score}%, you go together like coke and mentos")
elif(40<int(love_score)<50):
    print(f"Your score is {love_score}%, You are alright together")
else:
    print(f"Your score is {love_score}%")    




