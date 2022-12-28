'''
This Python project for binary search takes in a sorted list (array), then continually compares a search value with the middle of the array.
Depending on whether the search value is less than or greater than the middle value, the list is split (divide and conquer strategy) to reduce the search space, which hones in on the given search value.
'''
import random

def arrSearch(userVal,rndArr,countLoop):
#Finds the entered user value using a recursion function. Outputs the number of loops of the function.
    indMarker = int(len(rndArr)/2)
    if userVal == rndArr[indMarker]:
        if countLoop == 1:
            print(f"Found it in the first try!") 
        else:
            print(f"Found it after {countLoop} tries!") 
    else:
        countLoop += 1
        if userVal < rndArr[indMarker]:
            arrSearch(userVal,rndArr[0:indMarker],countLoop)
        else:
            arrSearch(userVal,rndArr[indMarker::],countLoop)

def checkArr(userVal,rndArr):
#Checks the value entered by the user is actually within the array
    global checkSearch
    if userVal in rndArr:
        checkSearch = True
    else:
        print('The entered value is not found within the array. Enter is a number that exists in the array.\n')

countLoop = 1 #counts the number of times the search function was called
checkSearch = False #boolean to determine whethere the prerequisites for the arrSearch function has been met

#generate an array of a random length up to 100 and random values
rndArr = [random.randint(0,100000) for i in range(0,random.randint(1,100))]
rndArr.sort()

print(rndArr)
while checkSearch == False:
    try:
        userVal = int(input('Enter in the search value: '))
        checkArr(userVal,rndArr)
    except ValueError:
        print('Please enter an integer')
arrSearch(userVal,rndArr,countLoop)