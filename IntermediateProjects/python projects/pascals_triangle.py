'''
Pascal's Triangle
-------------------------------------------------------------
Number of combinations via "n choose k" or nCk = n! / [k! * (n-k)!]
'''

from math import factorial

def gen_triangle(n):
    """generates and prints Pascals triangle

    Args:
        n (int): The desired level of Pascals triangle

    Returns:
        prints Pascals triangle
    """
    for lvl in range(1,n+1): #outer loop to produce each level starting at level 1, need to add 1 to n to accomodate
        print(end=(n-lvl)*' ') #the position is correct without it creating a new line after print
        j = lvl-1 #j is used to calculate the actual value in the equation because how indexes start at 0, it needs to be -1 from n

        for i in range(0,lvl): #lvl needs to include 0 and n to get all of pascals triangle
            print(factorial(j)//(factorial(i)*factorial(j-i)), end=' ') #// is used for floor division to display integers
        print('')

def check_number():
    """user enters in a number that needs to be a positive integer

    Returns:
        int: a positive integer described the desired number of levels within Pascal's triangle
    """
    while True:
        try:
            n = int(input('How many levels of the triangle do you want? '))
            if n>0:
                return n
            else:
                print('A positive number needs to be entered. Enter in a positive whole number.')
        except ValueError:
            print('An integer was not entered. Only integers are allowed. Enter in a postive whole number.')

if __name__ == '__main__':
    n = check_number()
    gen_triangle(n)
