import random

sortValues = ['ASC','DESC','NONE']

def sortList(ranArray,sort):
    if sort == 'ASC':
        ranArray.sort()
    elif sort == 'DESC':
        ranArray.sort(reverse = True)
    print(ranArray)

ranArray = [random.randint(0,100) for x in range(0,random.randint(10,100))]

print(ranArray)
sort = str.upper(input('Enter in ASC, DESC or NONE: '))

while sort not in sortValues:
    print('Invalid sorting style. Sorting style must be ASC, DESC or NONE. Enter in the style again.')
    sort = str.upper(input('Enter in ASC, DESC or NONE: '))

sortList(ranArray,sort)   