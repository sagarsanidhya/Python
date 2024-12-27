#Rollercoaster Ticket price 

print("Welcome to Rollercoaster!")

height = float(input("Please enter your Height (in cm) :"))
bill = 0

if height>=120:
    print("You can Ride the Rollercoaster")
    age = int(input("Enter Your age :"))
    if age<12:
        bill = 5
        print("Child Ticket -- Ticket Price $5")
    elif 12 <= age <18:
        bill = 7
        print("Youth Ticket -- ticket price $7") 
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok , Have a Free ride on us!") 
    else:
        bill = 12
        print("Adult Ticket -- ticket price $12")

    photo = input("Want Photos? Y for Yes or N for NO  :")
    if photo == "Y":
        bill += 3
        print(f"The total bill is ${bill} for the ride")
    else:
        print(f"The Total bill is ${bill} for the ride") 
else:
    print("You have to grow Taller to ride")           