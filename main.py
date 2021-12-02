from user import *
from word_bank import get_animal_words
##from timer import *
from random import seed
from random import randint
def main():
    seed(1)
    ## Game starts

    ## User can choose what game mode to choose (Animal words or general words)

    ## Timer starts 

    ## Words start showing up and user controls come into play 

    ## Everytime player passes word new word is called (while loop?)

    ##Game ends , score is showed

    ##User decides to play again or not

    ##End of program

    print("Welcome to fish bowl!")
    print("To play, you will enter the number of players playing to begin")
    print("Then, starting with player 1, they will select a category and be given a word fitting that category to act out")
    print("They will then act out that word and if any of the non-actors correctly guess the word, a point will be added to the total score")
    print("The game will then cycle through the rest of the players\n\n")

    numPlayers = input("Enter number of players: ")
    numPlayers = int(numPlayers)
    print("\n")
    currentPlayer = 1
    totalScore = 0

    while 1:
        print("Player %d's turn\nTotal Score: %d" %(currentPlayer,totalScore))
        ##category = getCategory()

        ## Here is when the word to act out would be given
        get_animal_words()
        correct = input("Was this word guessed correctly?:(Y/N) ")
        print("\n")

        if correct == "Y":
            totalScore += 1


        if currentPlayer == numPlayers:
            currentPlayer = 1
        else:
            currentPlayer+=1
        
        ## Trying out a decision tree based on the game type. Should work
        if gameType = 1:
                get_animal_words()
        
        elif gameType = 2:
            category = input("Create a category from this word: ")
            w_list = get_words_like(category)
            r_index = randint(0,99)
            print(w_list[r_index])

        else gameType = 3:
            rhyme = input("Get words that rhyme with this word: ")
            w_list = get_words_like(rhyme)
            r_index = randint(0,99)
            print(w_list[r_index])

if __name__ == "__main__":
    main()
