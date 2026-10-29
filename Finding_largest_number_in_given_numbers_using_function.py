print("THIS PROGRAM IS DESIGNED TO FIND LARGEST NUMBER IN GIVEN NUMBERS USING FUNCTION...")
def largest_numb(a,b,c):
    if a > b and a > c:
        return a
    elif b > c :
        return b
    else:
        return c
s1 = largest_numb(46,46,42)
print(s1)
