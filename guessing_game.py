from random import randint

def playGame(MaxRangeChances):
    secretNumber = randint(1, MaxRangeChances[0])
    print(f"\nI've chosen a secret number between 1 and {MaxRangeChances[0]}.")
    for numberOfGuesses in range(MaxRangeChances[1], 0, -1):
        print(f"You have {numberOfGuesses} guess(es).")
        guess = int(input("What is the number? "))
        if guess == secretNumber:
            return
        else:
            print("That was wrong.\n")
    return secretNumber

level = int(input("""Choose a difficulty level:
1. Easy
2. Medium
3. Hard\n"""))

while level not in [1, 2, 3]:
    level = int(input("invalid choice. Try again: "))

play = [[10, 6], [20, 4], [50, 3]]
rightGuess = playGame(play[level - 1])
if rightGuess == None:
    print("You got it right!")
else:
    print("Game over.")
    print("The secret number is", rightGuess)
