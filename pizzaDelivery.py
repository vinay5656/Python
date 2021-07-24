bill = 0
print("Enter what size pizza, do ypu want ?L/M/S")
select = input("Size of pizza is ")
if select == "L" :
    bill = 30
elif select == "M" :
    bill = 25
elif select == "S" :
    bill =10
else :
    print("Please select which size of pizza do you want")

add_Pepperoni = input("do you want extra pepperoni ? Y/N")
if(add_Pepperoni == "Y") :
    bill = bill+5
add_Extra_Cheese = input("do you want extra cheese ? Y/N")
if(add_Extra_Cheese=="Y") :
    bill = bill+10
print("You have to pay ",bill)
