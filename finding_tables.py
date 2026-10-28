num = int(input("Enter a number to find its Table: "))
lst = int(input("Enter the last number upto you want to find table: "))
for i in range(1,lst+1):
    print(f"{num} * {i} = {num * i}")
