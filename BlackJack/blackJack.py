import random
from art import logo

def deal_card() :
    """ return a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def campareboth(userScore,computerScore):
    if userScore == computerScore : 
        print(f"match is drawed by {userScore,computerScore}")
    elif computerScore == 0 or userScore > 21 :
        print("you loses")
    elif userScore == 0 or computerScore > 21 :
        print("you won")
    else :
        print(f"you won by {userScore}") if (userScore > computerScore) else print(f"You loses by {computerScore}")

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# user_cards = []
# computer_cards = []

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

def calcScore(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) ==2 :
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def BlackJack() : 
    print(logo)
    user_cards = []
    computer_cards = []
    isGameOver = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"your cards :",user_cards)

    while not isGameOver:
        userScore = calcScore(user_cards)
        computerScore = calcScore(computer_cards)

        if userScore == 0 or computerScore == 0 or userScore > 21 :
            isGameOver = True
        else: 
            user_should_deal =input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal == 'y' : 
                user_cards.append(deal_card())
            else :
                isGameOver = True



    while computerScore != 0 and computerScore < 17: 
        computer_cards.append(deal_card())
        computerScore = calcScore(computer_cards)
    print(f"your final hand: {user_cards} and final score {userScore}")
    print(f"computer final hand : {computer_cards} and final score {computerScore}")

    campareboth(userScore,computerScore)

while input("do yo want to play a game of blackjack ? y/n : ") == 'y' : 
    BlackJack()
