import random
rock = '''
      ___________
_ _ _|    _______)
         (________)
         (________)
         (_______)
-----.___(______)

'''
paper = '''
      ___________
_ _ _|    _______)_____
              _________)__
            ______________)
         _____________)
-----.____________)

'''
scissors = '''
      ___________
_ _ _|    _______)_____
              _________)__
          ________________)
         (_______)
-----.___(______)

'''
choice = [rock,paper,scissors]
print("What do you choose ? Type 0 for rock, 1 for paper, 2 for scissors\n")
myChoice = int(input("what will your choose: "))

print("you chosen : ")
if myChoice>=0 and myChoice<=2 :
   print(choice[myChoice])
else :
    print("You Enter wrong choice")
computerChoice = random.randint(0,2)
print("computer chosen : ")
print(choice[computerChoice])

# if myChoice>=0 and myChoice<=2 :
#     if (myChoice==0 and computerChoice == 2) or (myChoice==2 and computerChoice == 1) or (myChoice==1 and computerChoice==0) :
#        print("YOU WIN")
#     else :
#        print("YOU LOSE")
# else : 
#     print("Please Enter a Valid choice. ")
if (myChoice==0 and computerChoice == 2) or (myChoice==2 and computerChoice == 1) or (myChoice==1 and computerChoice==0) :
    print("YOU WIN")
elif (myChoice==0 and computerChoice == 0) or (myChoice==2 and computerChoice == 2) or (myChoice==1 and computerChoice==1) :
    print("It's draw repeat your the move")
else :
    print("YOU LOSE")