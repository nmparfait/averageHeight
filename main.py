print("AVERAGE HEIGHTS")

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0 
for height in student_heights:
  total_height += height
print(f"The total of the height is {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students +=1
print(f"The number of the students is {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"The average of our student height is{average_height}")



