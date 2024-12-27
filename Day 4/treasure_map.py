# Don't Change the code below
row1= [" ", " ", " "]
row2= [" ", " ", " "]
row3= [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?" )

# Don't change the code above 

# write your code here

horizontal = int(position[0]) # to detemine the position
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

#don't change the code below
print(f"{row1}\n{row2}\n{row3}")