import random


minVal = 0
maxVal = 100

bitCoin = 100
costPerGame = 20
costPerHint = 5
winningValue = 20

gameOver = False
hintsEnabled = False

playerGuess = -1
computerGuess = 0

playerName = "Player"
computerName = "Computer"


while not gameOver:
    playerGuess = -1
    computerGuess = random.randint(minVal, maxVal)
    hintsEnabled = False
    print("Play the number guessing game")
    print("I am going to think of a number between", minVal, "and", maxVal)
    bitCoin = bitCoin - costPerGame
    print("For Testing: ", computerGuess)
    print("It costs", costPerGame, "to play, you have", bitCoin, "left")
    print("It costs", costPerHint, "for hints.")
    turnHintsOn = input("Do you want hints? y/n ")
    if turnHintsOn.lower() == "y":
        hintsEnabled = True
    while playerGuess != computerGuess:
        playerGuess = int(input("What is your guess? "))
        if playerGuess == computerGuess:
            print("Winner")
            bitCoin = bitCoin + winningValue
            print("You now have", bitCoin, "bitcoin lefts")
            if bitCoin > costPerGame:
                playAgain = input("Do you want to play again? y/n")
                if playAgain.lower() == "n":
                    gameOver = True
        else:
            print("Wrong")
            if hintsEnabled and bitCoin >= costPerHint:
                bitCoin = bitCoin - costPerHint
                if playerGuess > computerGuess:
                    print("HINT: Too high")
                else:
                    print("HINT: Too low")

print("Thanks for playing")
print("You are cashing out", bitCoin, "bitcoin")
