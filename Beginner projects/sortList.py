'''
Sort List
-------------------------------------------------------------
Sorts an array based on user input
'''

import random

def sort_list(ran_array,sort):
    """Sorts the list based on user input

    Args:
        ran_array (list): An array of numbers to be sorted
        sort (string): the type of sorting user has requested
    """
    if sort == 'ASC':
        ran_array.sort()
    elif sort == 'DESC':
        ran_array.sort(reverse = True)
    print(ran_array)

if __name__ == '__main__':
    sortValues = ['ASC','DESC','NONE']

    ran_array = [random.randint(0,100) for x in range(0,random.randint(10,100))]

    print(ran_array)

    while True:
        try:
            sort = str.upper(input('Enter in ASC, DESC or NONE: '))
            break
        except ValueError:
            print('Invalid sorting style. Sorting style must be ASC, DESC or NONE. Enter in the style again.')

    sort_list(ran_array,sort)
    