print("WRITTING A PROGRAM TO CREATE CALCULATOR USING SEPERATE FUNCTIONS FOR EACH OPERATION----->")
try:
    num1 = int(input("Enter the first Number = "))
    num2 = int(input("Enter the second number = "))
    operation = input("Enter '+' for addition.\nEnter '-' for Subtraction.\nEnter '*' for Multiplication.\nEnter '/' for Division.\nEnter '%' fo Remainder.\nNow Enter the sign: = ")
    while operation not in ['+','-','*','/','%']:
        operation = input("Invalid Input!\nPlease Enter Valid Sign: ")
    def addition(a,b):
        return (f'The sum of {a} and {b} is = {a+b}')
    def subtraction(a,b):
        return (f'The difference between {a} and {b} is = {a-b}')
    def multiplication(a,b): 
        return (f'The multiplication of {a} into {b} is = {a*b}')
    def division(a,b):
        if b == 0:
            return ("Num2 is Zero.So the answer is not defined.\nEnter Greater then Zero")
        else:
            return (f'{a} divide by {b} is = {a/b}')
    def module(a,b):
        if b != 0:    
            return (f'The module of {a}/{b} is = {a%b}')
        else:
            return ("Enter non-zero numbers....")
    if operation == '+':
        result = addition(num1,num2)
    elif operation == '-':
        result = subtraction(num1,num2)
    elif operation == '*':
        result = multiplication(num1,num2)
    elif operation == '/':
        result = division(num1,num2)
    elif operation == '%':
        result = module(num1,num2)
    print(result)
except ValueError:
    print("Please Enter appropirate values in the boxes......\nThank You...")
