n_students = int(input("How many students do you want to add to the file? "))
with open("studentData.txt", "a") as f:
    for i in range(n_students):
        name = input("Student name: ")
        email = input("Student email: ")
        f.write(name + "#" + email)
     
