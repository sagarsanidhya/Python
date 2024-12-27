weight = input("Please Enter your Weight(in kg)\n")
height = input("Please Enter your Height(in m)\n")
new_height=float(height)
new_weight=int(weight)
BMI = new_weight / new_height**2
print(round(BMI))