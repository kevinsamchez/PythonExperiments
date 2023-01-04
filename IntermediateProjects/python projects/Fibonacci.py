'''
Fibonacci Sequence Generator
-------------------------------------------------------------
'''

#fib_cache stores fibonacci numbers in a dictionary with the key being the # within the Fibonacci sequence
fib_cache = {}

def fib_val(user_val):
    """Calculates and returns the number of the fibonacci sequence for a given index

    Args:
        user_val (int): the index of the desired fibonacci sequence number

    Returns:
        int: the number of corresponding index of the fibonacci sequence
    """
    if user_val in fib_cache:
        return fib_cache[user_val]
    elif user_val == 0:
        fib_cache[user_val] = 0
    elif user_val == 1:
        fib_cache[user_val] = 1
    else:
        fib_cache[user_val] = fib_val(user_val - 1) + fib_val(user_val - 2)

    return fib_cache[user_val] #returns the value with the user_val key in the dictionary

if __name__ == '__main__':
#checks the entered user entry is a positive whole number
    while True:
        try:
            user_val = int(input('What number of the fibonacci sequences do you want to generate: '))
            if user_val > 0:
                break
            else:
                print('This is not a positive whole number. Enter in a positive whole number')
        except ValueError:
            print('This is not a positive whole number. Enter in a positive whole number')
#loops through and prints off each Fibonacci number
    for i in range(1, user_val + 1):
        fib_val(i)
        print(f'Fibonacci #{i}: {fib_cache[i]}')
