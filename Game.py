from app import clickedTile
from Tile import tiles

incomplete = tiles
complete = []
selectedButton = ?
matchAttempt = 0


def main():
    # A while loop will continuously put the user back after guessing each time
    # I'm having trouble here 'grabbing' the button to compare their values
    keepGoing = True
    while keepGoing == True:
        # The first selection will be named firstChoice
        firstChoice = selectedButton
        # The second selection will be named secondChoice
        secondChoice = selectedButton
        # This if statement will check to see if firstChoice and secondChoice match up
        if firstChoice == secondChoice:
            # Implement the matchCorrect function
            matchCorrect()
            # This is to check if the user has completed all of the matches
            if incomplete == 0:
                # Implement the userWin function
                userWin()
        # This else statement will be used for when the user makes an incorrect guess
        else:
            matchIncorrect()
            # This if statement is for checking for when the user has used all of their guesses
            if matchAttempt == 10:
                # exit the game
                exit()


# This function will remove the correct matches from the incomplete list and append them to the complete list
def matchCorrect():
    # Change both the firstChoice and the secondChoice to be matched
    firstChoice.match = True
    secondChocie.match = True
    # Take both values and append them to the complete list
    complete.append(firstChoice.value)
    complete.append(secondChoice.value)
    # Remove both values from the incomplete list
    incomplete.remove(firstChoice.value)
    incomplete.remove(secondChoice.value)


# This function will decrease the amount of attempts left by one each time it's been implemented
def matchIncorrect():
    # matchAttempt will increment by one
    matchAttempt += 1
    # This will 'flip' the tiles back to black
    firstChoice.faceUp = False
    secondChoice.faceUp = False


# This function will be for when the user has emptied incomplete and has won
def userWin():



if __name__ == '__main__':
    main()