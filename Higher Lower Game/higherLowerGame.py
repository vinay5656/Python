from higherLowerGameLogo import logo
from versusArt import vs
from gameData import data
import random

final_score =0
wrongChoose = False
print(logo)
def campareFollower(option1,option2,iChoose) :
    global final_score
    #global wrongChoose
    if iChoose=='A' :
        if option1 > option2 :
            final_score = final_score +1
            print(f"You are wright, your final score : {final_score}")
            return False
        else : 
            #wrongChoose = True
            print(f"Sorry, You are wrong, Your final score : {final_score}")
            return True
    else :
        if option2 > option1 :
            final_score = final_score +1
            print(f"You are wright, your current score : {final_score}")
            return False
        else : 
            #wrongChoose = True
            print(f"Sorry, You are wrong, Your final score : {final_score}")
            return True

while not wrongChoose :
    optionA = random.choice(data)
    print(f"{optionA['name']}, a {optionA['description']} from {optionA['country']}")
    print(vs)
    optionB = random.choice(data)
    print(f"{optionB['name']}, {optionB['description']} from {optionB['country']}")
    iChoose = input("who has more follower : Type 'A' or 'B' :  ")

    wrongChoose=campareFollower(optionA['follower_count'],optionB['follower_count'],iChoose)
# def campareFollower(option1,option2,iChoose) :
#     global final_score
#     if iChoose=='A' :
#         if option1 > option2 :
#             final_score = final_score +1
#             print(f"You are wright, your current score : {final_score}")
#         else : 
#             print(f"Sorry, You are wrong, Your final score : {final_score}")
#     else :
#         if option2 > option1 :
#             final_score = final_score +1
#             print(f"You are wright, your current score : {final_score}")
#         else : 
#             print(f"Sorry, You are wrong, Your final score : {final_score}")
