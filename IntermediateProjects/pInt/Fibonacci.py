'''
Fibonacci Sequence
-------------------------------------------------------------
'''

#fibCache stores fibonacci numbers in a dictionary with the key being the # within the Fibonacci sequence
fibCache = {}

def fibVal(userVal):
    if userVal in fibCache:
        return fibCache[userVal]
    elif userVal==0:
        fibCache[userVal] = 0
    elif userVal==1:
        fibCache[userVal] = 1
    else:
        fibCache[userVal] = fibVal(userVal-1) + fibVal(userVal-2)

    return fibCache[userVal] #returns the value with the userVal key in the dictionary

if __name__ == '__main__':
    #checks the entered user entry is a positive whole number
    while True:
        try:
            userVal = int(input('What number of the fibonacci sequences do you want to generate: '))
            if userVal > 0:
                break
            else:
                print('This is not a positive whole number. Enter in a positive whole number')
        except ValueError:
            print('This is not a positive whole number. Enter in a positive whole number')
    
    #loops through and prints off each Fibonacci number
    for i in range(1,userVal+1):
        fibVal(i)
        print(f'Fibonacci #{i}: {fibCache[i]}')