from user import *
from word_bank import *
from timer import *
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
    print("To play, you will select a game mode and then you will be given a word to act out")
    print("You will then act out that word and if any of the non-actors correctly guess the word, a point will be added to the total score")
    print("The game will run until time runs out\n\n")

    gameType = getCategory()
    gameType = int(gameType)

 
    totalScore = 0

    while 1:
        print("Score: %d"%(totalScore))
        
        ## Trying out a decision tree based on the game type. Should work
        if gameType == 1:
                get_animal_words()
        
        elif gameType == 2:
            category = input("Create a category from this word: ")
            w_list = get_words_like(category)
            r_index = randint(0,99)
            print(w_list[r_index])

        else:
            rhyme = input("Get words that rhyme with this word: ")
            w_list = get_words_rhyme(rhyme)
            r_index = randint(0,99)
            print(w_list[r_index])

        correct = input("Was this word guessed correctly?:(Y/N) ")
        print("\n")
        #countdown()
        if correct == "Y":
            totalScore += 1

if __name__ == "__main__":
    main()
