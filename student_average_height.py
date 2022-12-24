num_students = input("Number of students?: ")
num_students = int(num_students)

students = {}
for i in range(num_students):
    name = input("Student Name: ")
    height = input("Student height: ")

    students[float(height)] = name

student = list(students)
print(sum(student)/len(student))