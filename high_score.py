num_students = input("Number of students?: ")
num_students = int(num_students)

students = {}
for i in range(num_students):
    name = input("Student Name: ")
    score = input("Student Score: ")

    students[int(score)] = name

student = list(students)
print(max(student))