def sgpaCalculate(semester):
    """This function take a dictionary of subjects name and their credit points as an arguement and return the SGPA after calculating."""
    credits = []
    grades = []

    for subject, credit in semester.items():
        marks = int(input(f"Enter the marks of {subject}: "))
        grade = 0

        if marks >= 0 and marks < 40:
            grade = 0
        elif marks >= 40 and marks <= 49:
            grade = 5
        elif marks >= 50 and marks <= 59:
            grade = 6 
        elif marks >= 60 and marks <= 69:
            grade = 7 
        elif marks >= 70 and marks <= 79:
            grade = 8 
        elif marks >= 80 and marks <= 89:
            grade = 9 
        elif marks >= 90 and marks <= 100:
            grade = 10 
            
        else:
            print("Enter marks between 0 to 100!")
            exit()
            break

        grades.append(grade)
        credits.append(credit)

    sum, creditSum = 0, 0

    for i in range(len(semester)):
        sum += grades[i]*credits[i]
        creditSum += credits[i]

    sgpa = sum/creditSum
    return sgpa

# Semester wise subject along with their credit points.
sem1 = {
    "English": 2,
    "Math-1": 4,
    "BEEE": 3,
    "PPS": 3,
    "BES": 2,
    "English Practical": 1,
    "BEEE Practical": 1,
    "PPS Practical": 1,
    "Workshop": 2.5,
}
sem2 = {
    "Math-2": 4,
    "HVSS": 3,
    "Physics": 4,
    "DSUC": 3,
    "Python": 3,
    "Physics Practical": 1,
    "DSUC Practical": 1,
    "Python Practical": 1,
    "Engineering Graphics": 2
}
sem3 = {
    "DE": 3,
    "ADS": 3,
    "DBMS": 3,
    "DS & AI": 3,
    "AI": 3,
    "DM": 3,
    "DE Lab": 2,
    "ADS Lab": 2,
    "DBMS Lab": 2,
    "DS & AI Lab": 2,
    "Constitution of India": 2
}
sem4 = {
    "OS": 3,
    "R": 3,
    "JAVA": 3,
    "DAA": 3,
    "COA": 3,
    "CN": 3,
    "OS Lab": 2,
    "JAVA LAB": 2,
    "DAA Lab": 2,
    "R Lab": 2
}

semesters = [sem1, sem2, sem3, sem4]

gpa = input("You want to calculate SGPA or CGPA: ").lower()

if gpa == "sgpa":
    sem = int(input("Enter the semester no.: "))
    sgpa = sgpaCalculate(semesters[sem-1])
    print(f"\nYour SGPA of sem no. {sem}: {sgpa}\n")
    
elif gpa == "cgpa":
    sem = int(input("In which semester you are? (1 to 4): "))
    sgpaSum = 0
    for i in range(sem):
        sgpa = sgpaCalculate(semesters[i])
        sgpaSum += sgpa

    cgpa = sgpaSum/sem
    print(f"\nYour CGPA till sem no. {sem} is: {cgpa}\n")

else:
    print("Invalid Input!")

