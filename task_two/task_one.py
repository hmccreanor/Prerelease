n_students = int(input("How many students are there in the class? "))

student_data = []

for i in range(n_students):
    print("Please enter a name and email address")
    name = input("Name: ")
    email = input("Email: ")
    formatted = name + "#" + email
    student_data.append(formatted)

with open("studentData.txt", "a") as f:
    for data in student_data:
        f.write(data)

