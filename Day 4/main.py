# Random Module

import random

random_integer = random.randint(1,10) #generates random integer values inclusive of number as input
print(random_integer)
 
# 0.00000 - 0.99999
random_float = random.random() #generates Floating point from 0.0 to 1.0 excluding
print(random_float)

random_float *5
#0.0000 - 4.9999

# import my_module
# print(my_module.pi)

#can be implement in love calculator project to give random result
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")