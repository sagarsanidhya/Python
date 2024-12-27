#To Find Whether is it a Leap year or not

print("Leap Year Finder")

year= int(input("Enter any Year :"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")    
    else:
        print("Leap year")     
else:
    print("Not aLeap year")