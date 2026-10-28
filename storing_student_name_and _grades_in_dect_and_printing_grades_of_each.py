print("Store student names and marks in a dictionary and print each student's grade")
student = {}
try:
    limit = int(input("Enter the number of students you want to add: "))
    for i in range(1,limit+1,1):
        name = input(f'Your {i} student name: ')
        marks = int(input(f'Enter the marks of {name}: '))
        if marks <= 0 :
            marks = 0
        elif marks >= 100:
            marks = 100 
        student.update({name : marks})
    for name,marks in student.items():
        if marks >= 90:
            grade = "A"
            print(f'{name} : {marks} marks ---> {grade}')
        elif marks >= 80:
            grade = "B"
            print(f'{name} : {marks} marks ---> {grade}')
        elif marks >= 70:
            grade = "C"
            print(f'{name} : {marks} marks ---> {grade}')
        elif marks >= 60:
            grade = "D"
            print(f'{name} : {marks} marks ---> {grade}')
        elif marks >= 40:
            grade = "E"
            print(f'{name} : {marks} marks ---> {grade}')
        elif marks < 40:
            grade = "F"
            print(f'{name} : {marks} marks ---> {grade}')
except ValueError:
    print("Attention! Please enter String in Names and Integer in number and marks ...")
