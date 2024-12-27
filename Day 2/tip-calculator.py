#Bill Calculator
 
print("Welcome to the Tip Calculator")

bill = float(input("What was the Total bill? Rs."))

tip_percentage = float(input("What percent of tip you want to give? \n 5%, 10%, 15% \n"))
tip = tip_percentage / 100 *bill
bill += tip

person = int(input("How many people will split the bill? \n"))
split = bill / person
split_rounded = round(split,2)
final_amount ="{:.2f}".format(split) #format use to print two place of decimal
print(f"After spliting total amount per head is {final_amount}")


