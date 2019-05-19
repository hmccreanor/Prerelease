n_students = int(input("How many students are there in the class? "))

student_data = []

for i in range(n_students):
    print("Please enter a name and email address")
    name = input("Name: ")
    email = input("Email: ")
    formatted = name + "#" + email
    student_data.append(formatted)

print("\n{0:^12}{1:^12}".format("Name", "Email"))

for j in range(n_students):
    name, email = student_data[j].split("#")
    print("{0:^12}{1:^12}".format(name, email))


