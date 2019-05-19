n_students = int(input("How many students are there in the class? "))

student_data = []

for i in range(n_students):
    print("Please enter a name and email address")
    name = input("Name: ")
    email = input("Email: ")
    formatted = name + "#" + email
    student_data.append(formatted)

lookup_name = input("What student would you like to look up? ")
for i in range(n_students):
    name, email = student_data[i].split("#")
    if lookup_name == name:
        print(email)

