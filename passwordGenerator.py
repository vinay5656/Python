import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# p1 = ""
# for n in range(0,nr_letters) :
#     p1=p1+random.choice(letters)
# p2 = ""
# for n in range(0,nr_symbols) :
#     p2= p2+random.choice(symbols)
# p3 = ""
# for n in range(0,nr_numbers) :
#     p3 = p3+random.choice(numbers)
# password = p1+p2+p3
# print(password)

#lenghtOfPassword = nr_letters + nr_symbols + nr_numbers
password = ""
possibleList = []
for n in range(0,nr_letters) :
   possibleList.append((random.choice(letters)))
for n in range(0,nr_numbers) :
   possibleList.append(random.choice(numbers))
for n in range(0,nr_symbols) :
   possibleList.append(random.choice(symbols))

# for n in range(0,lenghtOfPassword) :
#     password = password+random.choice(possibleList)
# print(password)
random.shuffle(possibleList)
for n in possibleList :
    password = password+n

print(password)