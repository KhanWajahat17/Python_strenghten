print("WRITTING A FUNCTION THAT CHECK WHETHER THE GIVEN NUMBER IS PRIME OR NOT----->")
def check_prime(num):
    if num <= 1:
        return (f'{num} Not A Prime Number.')
    elif num == 2:
        return ("2 is Prime Number..")
    elif num > 2 :
        for i in range(2,num):
            if num % i == 0:
                return (f"This Number {num} is Not a Prime Number.")
            
    return (f'The given number {num} is a Prime Number....')
number = check_prime(int(input("Enter number to check whether the given number is prime number or not: ")))
print(number)
