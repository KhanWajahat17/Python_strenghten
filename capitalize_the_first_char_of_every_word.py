
print("THIS PROGRAM IS DESIGED TO CAPATILIZE EVERY FIRST LETTER OF EVERY WORD------->")
sen = input("Write something:::--->>>")
sen1 = sen.split()
cp = ""
for word in sen1:
    cp += (word[0].upper() + word[1:] + " ")
print(cp.strip())
