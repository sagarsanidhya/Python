#BMI Calculator 2.0

print("Welcome to BMI Calculator 2.0")

weight = float(input("Enter your Weight(in kg) :"))
height = float(input("Enter your Height(in m) :"))

BMI = round(weight / height ** 2)


if BMI < 18.5:
    print(f"Your BMI is {BMI} , you are UnderWeight")
elif BMI < 25: #if elif is whole group of statement so it is going to check the conditions in order 
    print(f"Your BMI is {BMI}, You are Normal Weight")
elif BMI <30:
    print(f"Your BMI is {BMI}, you are Overweight")
elif BMI <35:
    print(f"your BMI is {BMI}, You are Obese")
else:
    print(f"your is BMI is {BMI}, you are Clinically Obese")
