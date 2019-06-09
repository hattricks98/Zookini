from fuzzywuzzy import fuzz


print("Hey , there lets's start with your name : ")
name = input()
print("Welcome to Zookini %s" % name)
print('Zookini is a top end alphabet numbers puzzle, the only one in the world!\nSo here"s your first question: ')

print("""You can only use any letter once, What is the largest number that you could write down in words?\nExample: NINETY
\nBut in NINETY N is used twice""")


jawab = "five thousand"


class ScoreBoard:
    ANSWER = input()
    Ratio = fuzz.ratio(jawab.lower(),ANSWER.lower())


    def playingf(self):
        playing = True
        while playing:
            choice = input("Would you like to play again? y/n:  \n")
            if choice == "n":
                print("Thanks for playing")
                playing = False
            else:
                print("""You can only use any letter once, what are the largest that you could write down in words?\nExample: Six Million
                \nBut in Six Million as I & L is used thrice and twice""")
                soch = input('Try Again: ')
                
                lev = fuzz.ratio(jawab.lower(),soch.lower())
                # if self.ANSWER == jawab:
                if lev > 95:
                    print('Your Levenshtein score: ' + str(lev))
                    self.score += 1
                    print(self.score)
                    print("You won!")
                    exit()
                else:
                    self.score -= 1
                    print('Your Levenshtein score: ' + str(lev))
                    print("Your score is :")
                    print(self.score)
                    print("""HINT: As per standard numbering system you may go upto billion, trillion, quadrillion, 
                      quintillion, sextillion, septillion, octillion, nonillion, and decillion.....
                      ...""")







    def __init__(self):
        self.score = 0



    def my_score(self):

        if self.Ratio >95:
            self.score += 1
            print('Your Levenshtein score: ' + str(self.Ratio))
            
        else:
            self.score -= 1

        print("Your score is :")
        print(self.score)
        print('Your Levenshtein score: ' + str(self.Ratio))







player1= ScoreBoard()
player1.my_score()
player1.playingf()

