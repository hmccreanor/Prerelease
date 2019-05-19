studentID = input("Please enter the student id you want to look for")
found = False

with open("studentData.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if studentID in line.split("#")[0]:
            print(line.split("#")[1])
            found = True
            break
    if not found:
        print("Sorry. The ID was not found")
