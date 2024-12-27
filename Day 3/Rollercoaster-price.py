#Rollercoaster Ticket price 

print("Welcome to Rollercoaster!")

height = float(input("Please enter your Height (in cm) :"))


if height>=120:
    print("You can Ride the Rollercoaster")
    age = int(input("Enter Your age :"))
    if age<12:
        print("you can ride -- Ticket Price $5")
    elif 12 <= age <18:
        print("You can Ride -- ticket price $7")    
    else:
        print("you can ride -- ticket price $12") 
else:
    print("You have to grow Taller to ride")           