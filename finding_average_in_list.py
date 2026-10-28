marks_list = []
subjects = int(input("Enter the number of subject: "))
total = 0
greater_then_avg = 0
if subjects >= 1:
    for i in range(1,subjects+1):
        marks = int(input(f'Enter the {i} marks:  '))
        marks_list.append(marks)
        total += marks
    average = total/subjects
    for val in marks_list:
        if val > average:
            greater_then_avg += 1
    print(f'The Average of the marks is = {average}')
    print(f'The marks that is greater then average({average}) is = {greater_then_avg}')


else:
    print("Please enter greater then zero.......")
