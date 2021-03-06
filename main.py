from user import *
from word_bank import *
from timer import *
from random import seed
from random import randint

import signal

## This function handles the timer
def timeout_handler(signal, frame):
    raise Exception('Time is up!')
signal.signal(signal.SIGALRM, timeout_handler)

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
    ## This determines how long the program runs
    signal.alarm(5)
    try:
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
            if correct == "Y":
                totalScore += 1
    except:
        print("\ntimes up!\n")
        print("Your final score: ",totalScore)
        val = input("Would you like to play again? (Y/N")

        if(val == 'Y'):
            main()
        else:
            print("\nThank you for playing!!")

if __name__ == "__main__":
    main()
