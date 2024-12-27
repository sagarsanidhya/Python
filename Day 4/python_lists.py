#lists is a way to organisning and storing data in python
# fruits = [item1, item2] syntax of list 

states_of_america = ["Delaware", "pennsylvania"]
#order is determined from the order in list
print(states_of_america[0]) 
print(states_of_america[-1]) #the negative index here represents that order is being started form the last of the list

states_of_america[1]  = "Pencilvania" #this syntax can be used to update any data within the list

states_of_america.append("Rauy's Land") #add item to the end of the list
print(states_of_america[2])

states_of_america.extend(["Yay land" , "Lelaynd"])
print(states_of_america[4])