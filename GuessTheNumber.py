from random import randint

def main():
    case = 1
    lossCount = 0
    while case:
        num = randint(1,10)
        guess = int(input(print("Guess the number between 1 and 10")))
        if guess > 0 & guess < 11:
            if guess == num:
                print("You win!")
                print("It took you ", lossCount, " tries.")
                lossCount = 0
            else:
                print("Suck it, nerd. The correct answer was ", num)
                lossCount += 1
        else:
            print("Am I a joke to you? I said between 1 and 10. Try again.")
main()
