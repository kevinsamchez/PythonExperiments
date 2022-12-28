import random

RSPtoNum = {'R':1, 'S':2, 'P':3}
RSP = {1:'Rock',2:'Scissors',3:'Paper'}
winScore = 0
loseScore = 0
tieScore = 0

def checkWinner(userNum,machineNum):
    global winScore
    global loseScore
    global tieScore
    if userNum - machineNum == -1 or userNum - machineNum == 2:
        print("You win!")
        winScore += 1
    elif userNum - machineNum == -2 or userNum - machineNum == 1:
        print("You lose :(")
        loseScore += 1
    elif userNum - machineNum == 0:
        print("It's a tie")
        tieScore += 1
    print(f'you have won {winScore} games')
    print(f'you have lost {loseScore} games')
    print(f'you have tied {tieScore} games')

def newGame():
    user_RSP = str.upper(input("Enter R, S or P: "))
    while user_RSP not in RSPtoNum.keys():
        print(f'Only {RSPtoNum.keys()} values are allowed')
        user_RSP = str.upper(input("Enter R, S or P: "))
    MachineRSPNum = random.randint(1,3)

    print(f'You threw down {RSP[RSPtoNum[user_RSP]]}')
    print(f'The machine threw down {RSP[MachineRSPNum]}')
    print('')
    checkWinner(RSPtoNum[user_RSP],MachineRSPNum)
    againCheck()

def againCheck():
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
        
newGame()