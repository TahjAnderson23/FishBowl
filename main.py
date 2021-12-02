from user import *

print("Hello, welcome to charades!")
print("To play, you will enter the number of players playing to begin")
print("Then, starting with player 1, they will select a category and be given a word fitting that category to act out")
print("They will then act out that word and if any of the non-actors correctly guess the word, a point will be added to the total score")
print("The game will then cycle through the rest of the players\n\n")

numPlayers = input("Enter number of players: ")
numPlayers = int(numPlayers)
print("\n")
currentPlayer = 1

while 1:
    print("Player %d's turn" %(currentPlayer))
    category = getCategory()
    print("\n")

    if currentPlayer == numPlayers:
        currentPlayer = 1
    else:
        currentPlayer+=1







