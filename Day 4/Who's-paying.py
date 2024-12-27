#Who's Paying 
import random
names_string = input("Write the names of everyone seprating by a comma\n")
names = names_string.split(",")

## code start from here
# x = len(names) #len function give the no. element
# lucky_name = random.randint(0,x-1)
# person_who_will_pay = names[lucky_name] #extract the list name from the index value

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to pay for meal today")