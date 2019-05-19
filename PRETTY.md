# Task 1.1
~~~~
INPUT number_of_students
DECLARE students: ARRAY[1: number_of_students] OF STRING
CONSTANT headers = "Student Name/Email Address"

FOR n <- 1 TO number_of_students
    INPUT id
    INPUT email
    students[n] <- id & '#' & email
ENDFOR

FOR n <- 1 TO number_of_students
    element <- students[n]
    hashIndex <- FIND(element, '#')
    outputString <- LEFT(element, hashIndex - 1) & " " & RIGHT(hashIndex, LENGTH(element))
    OUTPUT outputString
ENDFOR

FUNCTION FIND(Name : STRING, C: CHAR) RETURNS INTEGER
    FOR n <- 1 TO LENGTH(Name)
        IF Name[n] = C THEN
            RETURN n
	ENDIF
    RETURN -1
ENDFUNCTION 
~~~~

~~~~
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
~~~~

# Task 1.2
~~~~
INPUT number_of_students
DECLARE students: ARRAY[1: number_of_students] OF STRING
CONSTANT headers = "Student Name/Email Address"

FOR n <- 1 TO number_of_students
    INPUT id
    INPUT email
    students[n] <- id & '#' & email
ENDFOR

FUNCTION FIND(Name : STRING, C: CHAR) RETURNS INTEGER
    FOR n <- 1 TO LENGTH(Name)
        IF Name[n] = C
            RETURN n
    RETURN -1
ENDFUNCTION
        
INPUT number_of_students_to_delete

FOR n <- 1 TO number_of_students_to_delete
    INPUT id
    INPUT email
    formattedEntry <- id & '#' & email
    FOR j <- 1 TO number_of_students
        IF students[j] = formattedEntry THEN
            students[j] <- ""
        ENDIF
    ENDFOR 
ENDFOR
    	
FOR n <- 1 TO number_of_students
    IF students[n] <> "" THEN
        OUTPUT students[n]
    ENDIF
ENDFOR


FOR n <- 1 TO number_of_students
    element <- students[n]
    hashIndex <- FIND(element, '#')
    outputString <- LEFT(element, hashIndex - 1) & " " & RIGHT(hashIndex, LENGTH(element))
    OUTPUT outputString
ENDFOR
~~~~

~~~~
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
~~~~

# Task 1.3
~~~~
INPUT number_of_students
DECLARE students: ARRAY[1: number_of_students] OF STRING
CONSTANT headers = "Student Name/Email Address"

FOR n <- 1 TO number_of_students
    INPUT id
    INPUT email
    students[n] <- id & '#' & email
ENDFOR 

FUNCTION FIND(Name : STRING, C: CHAR) RETURNS INTEGER
    FOR n <- 1 TO LENGTH(Name)
        IF Name[n] = C
            RETURN n
    RETURN -1
ENDFUNCTION
 
INPUT lookUpName

FOR n <- 1 TO number_of_students
    element <- students[n]

    hashIndex <- FIND(element, '#')
    name <- LEFT(element, hashIndex - 1)
    email <- RIGHT(hashIndex, LENGTH(element))

    IF name = lookUpName THEN
      OUTPUT email
    ENDIF
ENDFOR
~~~~

~~~~
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
~~~~

# Task 1.4
~~~~
INPUT number_of_students
DECLARE students: ARRAY[1: number_of_students] OF STRING
CONSTANT headers = "Student Name/Email Address"

FOR n <- 1 TO number_of_students
    INPUT id
    INPUT email
    students[n] <- id & '#' & email
ENDFOR 

FUNCTION FIND(Name : STRING, C: CHAR) RETURNS INTEGER
    FOR n <- 1 TO LENGTH(Name)
        IF Name[n] = C
            RETURN n
    RETURN -1
ENDFUNCTION
 
FUNCTION IS_IN(s1 : STRING, s2 : STRING) RETURNS BOOL
    FOR n <- 1 TO LENGTH(s1)
      IF MID(s1, n, LENGTH(s2)) = s2 THEN
        RETURN TRUE
      ENDIF
    ENDFOR
    RETURN FALSE
ENDFUNCTION

INPUT lookUpName

FOR n <- 1 TO number_of_students
    element <- students[n]

    hashIndex <- FIND(element, '#')
    name <- LEFT(element, hashIndex - 1)
    email <- RIGHT(hashIndex, LENGTH(element))

    IF IS_IN(name, lookUpName) THEN
      OUTPUT name	
      OUTPUT email
    ENDIF
ENDFOR
~~~~

~~~~
n_students = int(input("How many students are there in the class? "))

student_data = []

for i in range(n_students):
    print("Please enter a name and email address")
    name = input("Name: ")
    email = input("Email: ")
    formatted = name + "#" + email
    student_data.append(formatted)

lookup_name = input("What student would you like to look up? ")

print("\n{0:^12}{1:^12}".format("Name", "Email"))

for i in range(n_students):
    name, email = student_data[i].split("#")
    if lookup_name in name:
        print("{0:^12}{1:^12}".format(name, email))
~~~~

# Task 2.1
~~~~
INPUT number_of_students
CONSTANT headers = "Student Name/Email Address"

OPENFILE "studentData.txt" FOR WRITE

FOR n <- 1 TO number_of_students
    INPUT id
    INPUT email
    WRITEFILE "studentData.txt", id & '#' & email	
ENDFOR

CLOSEFILE 
~~~~

~~~~
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
~~~~

# Task 2.2
~~~~
INPUT studentID
DECLARE data : STRING

OPENFILE "studentData.txt" FOR READ

FUNCTION FIND(s1 : STRING, s2 : STRING)
  FOR n <- 1 TO LEN(s1) 
    IF s1[n] = s2 THEN
      RETURN n
    ENDIF 
  ENDFOR 
  RETURN -1
ENDFUNCTION

WHILE NOT EOF("studentData.txt")
  READFILE "studentData.txt" data
  hashIndex <- FIND(data, '#')
  IF hashIndex <> -1 THEN
    email <- RIGHT(hashIndex, LENGTH(data))
    OUTPUT email
  ENDIF
ENDFOR
~~~~

~~~~
studentID = input("Please enter the student id you want to look for")
found = False

with open("studentData.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if studentID = line.split("#")[0]:
            print(line.split("#")[1])
            found = True
            break
    if not found:
        print("Sorry. The ID was not found")
~~~~

# Task 2.3
~~~~
INPUT studentIDSubstring
DECLARE data : STRING

FUNCTION FIND(Name : STRING, C: CHAR) RETURNS INTEGER
    FOR n <- 1 TO LENGTH(Name)
        IF Name[n] = C
            RETURN n
    RETURN -1
ENDFUNCTION
 
FUNCTION IS_IN(s1 : STRING, s2 : STRING) RETURNS BOOL
    FOR n <- 1 TO LENGTH(s1)
      IF MID(s1, n, LENGTH(s2)) = s2 THEN
        RETURN TRUE
      ENDIF
    ENDFOR
    RETURN FALSE
ENDFUNCTION

OPENFILE "studentData.txt" FOR READ

WHILE NOT EOF("studentData.txt")
  READFILE "studentData.txt", data
  hashIndex <- FIND(data, "#")
  name <- LEFT(data, hashIndex - 1) 
  email <- RIGHT(hashIndex, LENGTH(element))

  IF IS_IN(name, studentIDSubstring) THEN
    OUTPUT name
    OUTPUT email
  ENDIF
ENDFOR

CLOSEFILE
~~~~

~~~~
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
~~~~

# Task 2.4
~~~~
INPUT number_of_students
OPENFILE "studentData.txt" FOR APPEND

FOR n <- 1 TO number_of_students
    INPUT id
    INPUT email
    WRITEFILE "studentData.txt", id & '#' & email	
ENDFOR

CLOSEFILE 
~~~~

~~~~
n_students = int(input("How many students do you want to add to the file? "))
with open("studentData.txt", "a") as f:
    for i in range(n_students):
        name = input("Student name: ")
        email = input("Student email: ")
        f.write(name + "#" + email)    
~~~~
