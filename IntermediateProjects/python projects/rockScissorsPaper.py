'''
Rock Scissors Paper
-------------------------------------------------------------
Play a game of rock scissor paper can keeps a score.
'''
import random

def checkWinner(userNum,machineNum):
    #checks who won and maintains scores using global parameters
    global winScore
    global loseScore
    global tieScore
    if userNum - machineNum == -1 or userNum - machineNum == 2:
        print("*** You win! ***")
        winScore += 1
    elif userNum - machineNum == -2 or userNum - machineNum == 1:
        print("*** You lose :( ***")
        loseScore += 1
    elif userNum - machineNum == 0:
        print("*** It's a tie ***")
        tieScore += 1
    print('')
    print(f'you have won {winScore} games')
    print(f'you have lost {loseScore} games')
    print(f'you have tied {tieScore} games')

def newGame():
    #starts a game of RSP
    #User enters in value with a validation check
    user_RSP = str.upper(input("Enter R, S or P: "))
    while user_RSP not in RSPtoNum.keys():
        print(f'Only {list(RSPtoNum.keys())} values are allowed')
        user_RSP = str.upper(input("Enter R, S or P: "))
    #Randomally generate machine RSP
    MachineRSPNum = random.randint(1,3)

    print(f'You threw down {str.upper(RSP[RSPtoNum[user_RSP]])}')
    print(f'The machine threw down {str.upper(RSP[MachineRSPNum])}')
    print('')

    #checks for the winner and checks if user wants to playa gain
    checkWinner(RSPtoNum[user_RSP],MachineRSPNum)
    againCheck()

def againCheck():
    #checks if user wants to play again
    print('')
    againBoolean = str.upper(input('Do you want to play again (y/n)? '))
    while againBoolean not in ['Y','N']:
        print('Only Y or N is allowed.')
        againBoolean = str.upper(input('Do you want to play again (y/n)? '))
    if againBoolean == 'Y':
        print('')
        newGame()
    elif againBoolean == 'N':
        print('Thanks for playing!')

if __name__ == '__main__':
    #set up dictionaries
    RSPtoNum = {'R':1, 'S':2, 'P':3}
    RSP = {1:'Rock',2:'Scissors',3:'Paper'}

    #initialise scores
    winScore = 0
    loseScore = 0
    tieScore = 0

    newGame()