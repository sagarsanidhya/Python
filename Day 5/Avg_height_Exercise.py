student_heights = input("Input a list of Student heights :").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#code below
sumof_height= 0; 
for height in student_heights:
        sumof_height += height
        
number_of_students = 0
for student in student_heights:
    number_of_students += 1
average_height = sumof_height/number_of_students
print(f"The average Height of the students in the class {average_height}")