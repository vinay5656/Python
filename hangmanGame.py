import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

wordList = ["Vinay", "Ravi", "Bhavesh"]
word = random.choice(wordList)

lives = 6

blankList = []
for i in range(0,len(word)) :
    blankList.append("_")
print(blankList)

end_of_game = False
while not end_of_game :

    chosenLatter = input("Choose a latter")
    for position in range(len(word)) :
        if chosenLatter==word[position]:
            blankList[position]=chosenLatter
            if not "_" in blankList:
                end_of_game=True
                print("You Win")
                print("Game Over")
                
        else:
            continue
        print(blankList)
    if not chosenLatter in word :
        lives = lives-1
        print(stages[lives])
        if lives==0:
            print("You lose")
            print("GAME OVER")
            end_of_game=True
