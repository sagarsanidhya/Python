student_scores = input("Input a list of Student heights :").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# #write your code below
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score 
# print(max_score)       

#using the max() function
print("The highest score in the class is:", max(student_scores))