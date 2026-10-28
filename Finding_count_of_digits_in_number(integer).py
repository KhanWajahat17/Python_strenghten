print("THIS PROGRAM IS DESIGNED FOR FINDING COUNT OF DIGITS IN INTEGERS WITHOUT DIRECTLY CONVERTING OR BY STRING METHOD::==>>")
#This Line will show the user a clear message to enter only integer..
print("Enter an integer....") 
num1 = input("Enter integer: ")
try:
    if num1.strip() != "": #condition for empty.Program will run if the user enter at least one input.
        num = int(num1) # converting string into integer   
        real_num = num # keeping the real number.
        count = 0
        num = abs(num) #avoiding arthimatics signs
        if num == 0: # condtion if the user enter only zero.
            count = 1
        while num :
            if num > 0 :
                count+=1
                num = num//10
        print(f'The number of digits in {real_num} is = {count}')
    else: 
        print("Attention Please! Please Enter at least one integer.....")
except ValueError: #For error handling. if user enter decimal number or string
    print("Please try again!Enter only intergers postive or negative but not having decimal...")
