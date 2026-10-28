print("*******This program will find Postive,Negative,zero number and also Even Odd:")
numb = int(input("Enter Number: "))
if numb <= -1:
    if numb % 2 == 0:
        print(f"The given number {numb} is Negative Even Number...")
    else:
        print(f'The given number {numb} is Negative Odd Number.....')
elif numb >= 1:
    if numb % 2 == 0:
        print(f'The given number {numb} is Postive Even Number.....')
    else:
        print(f'The given number {numb} is Postive Odd Number....')
else:
    print("The given number is Zero")
