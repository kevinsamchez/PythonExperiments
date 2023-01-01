'''
Sort List
-------------------------------------------------------------
Sorts an array based on user input
'''

import random

def sortList(ranArray,sort):
    if sort == 'ASC':
        ranArray.sort()
    elif sort == 'DESC':
        ranArray.sort(reverse = True)
    print(ranArray)

if __name__ == '__main__':
    sortValues = ['ASC','DESC','NONE']

    ranArray = [random.randint(0,100) for x in range(0,random.randint(10,100))]

    print(ranArray)

    while True:
        try:
            sort = str.upper(input('Enter in ASC, DESC or NONE: '))
            break
        except ValueError:
            print('Invalid sorting style. Sorting style must be ASC, DESC or NONE. Enter in the style again.')

    sortList(ranArray,sort)