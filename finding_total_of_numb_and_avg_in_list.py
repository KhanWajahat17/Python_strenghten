nums = []
total = 0
num = int(input("Enter how many number you want to add to list: "))
if num >= 1:
    for i in range (1,num+1):
        number = int(input(f'Enter the {i} number: '))
        total += number
        nums.append(number)
    print(nums)
    avg = total/num
    print(f'The total sum is :{total}')
    print(f'The average is : {avg}')
else:
    print("The Given is zero. so total and average is itslef zero:")
