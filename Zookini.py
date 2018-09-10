


print("Hey , there lets's start with your name : ")
name = input()
print("Welcome to Zookini %s" % name)
print('Zookini is a top end alphabet numbers puzzle, the only one in the world! \n So here"s your first question: ')

print("""You can only use any letter once, what are the largest that you could write down in words?\nExample: NINETY
\nBut NINETY as N is used twice""")


jawab = "five thousand"


class ScoreBoard:
    ANSWER = input()


    def playingf(self):
        playing = True
        while playing:
            choice = input("Would you like to play again? y/n:  \n")
            if choice == "n":
                print("Thanks for playing")
                playing = False
            else:
                print("""You can only use any letter once, what are the largest that you could write down in words?\nExample: NINETY
                \nBut NINETY as N is used twice""")
                self.ANSWER = input()
                if self.ANSWER == jawab:
                    self.score += 1
                    print(self.score)
                    print("You won!")
                    exit()
                else:
                    self.score -= 1

                print("Your score is :")
                print(self.score)







    def __init__(self):
        self.score = 0



    def my_score(self):

        if self.ANSWER == jawab:
            self.score += 1
        else:
            self.score -= 1

        print("Your score is :")
        print(self.score)







player1= ScoreBoard()
player1.my_score()
player1.playingf()

