n_students = int(input("How many students are there in the class? "))

student_data = []

for i in range(n_students):
    print("Please enter a name and email address")
    name = input("Name: ")
    email = input("Email: ")
    formatted = name + "#" + email
    student_data.append(formatted)

n_students_to_delete = int(input("How many students do you want to delete? "))

for i in range(n_students_to_delete):
    id = input("Name: ")
    email = input("Email: ")
    formatted = name + "#" + email
    for j in range(n_students):
        if student_data[j] == formatted:
            student_data.pop(j)
            break

print("\n{0:^12}{1:^12}".format("Name", "Email"))

for j in range(n_students):
    name, email = student_data[j].split("#")
    print("{0:^12}{1:^12}".format(name, email))


