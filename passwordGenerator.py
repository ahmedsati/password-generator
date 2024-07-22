#Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print()
print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

listL = []
for l in range(nr_letters):
    val = (random.choice(letters))
    listL.append(val)
    
listN = []
for n in range(nr_letters):
    val= random.choice(numbers)
    listN.append(val)

listS = []
for s in range(nr_symbols):
    val = random.choice(symbols)
    listS.append(val)


passwordList = []
passwordList.extend(listL)
passwordList.extend(listN)
passwordList.extend(listS)

random.shuffle(passwordList)

for i in passwordList:
    password+=i
    
print()
print(f"Your password is: {password}")

