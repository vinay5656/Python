# import random
# love_Score = random.randint(1,100)
# print(f"Your love score {love_Score}")

# percentage = random.random()*100
# print(f"Your would be {percentage} ")

# earn  = random.randrange(500,1000)
# print(earn)

# state1 = "rajasthan"
# state2 = "heryana"
# state3 = "dehli"
# state4 = "punjab"

# stateOfIndia = ['Rajasthan','Punjab','Dehli','Heryana','UP']
# print(stateOfIndia)
# print(stateOfIndia[2])
# print(stateOfIndia[-1])
# print(stateOfIndia[-3])
# stateOfIndia.append("MP")
# print(stateOfIndia)
# stateOfIndia.extend(["karnataka","maharashtra","Jamu Kashmir"])
# print(stateOfIndia)
# someOftheState = stateOfIndia.copy()
# someOftheState.append("punducherry")
# print(someOftheState)
# someOftheState.remove("Dehli")
# print(someOftheState)
# someOftheState.reverse()
# print(someOftheState)
# stateOfIndia.sort()
# print(stateOfIndia)
# number = stateOfIndia.index("Punjab")
# print(number+1)

# import random
# giveUsYourNames = input("We are taking everybody name")
# names = giveUsYourNames.split(", ")
# numnerOfParticipant = len(names)
# hereAreYou = random.randint(0,numnerOfParticipant-1)
# #print(hereAreYou)
# print(f"{names[hereAreYou]} is going to buy the meal today!")

row1 = ["🚗","🚗","🚗"]
row2 = ["🚗","🚗","🚗"]
row3 = ["🚗","🚗","🚗"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
column = int(input("Enter the column number"))
row = int(input("Enter the row number"))
map[row][column] = "🚎"
print(f"{row1}\n{row2}\n{row3}")