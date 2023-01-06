'''
Pocket Universal Principles of Design Randomiser
------------------------------------------------------------------------------------
Randomiser to read a random page everyday from the Pocket Universal Principles of Design book by \
    by William Lidwell, Kritina Holden and Jill Butler.
The application can be applied to any book.

Updates:
updated display location to accomodate length of random number
Prioritises pages that haven't been seen
Introduced confirmation button
Introduced a recall percentage to split time showing recently visited pages \
    and pages that haven't been read in a while
'''

import random
import tkinter
import pandas as pd

PATH = '.\Beginner projects\The pocket universal principles of design pages.csv'
DF = pd.read_csv(PATH)
RECALL_PERCENT = 25 #The percentage of times where I want to revisit a recently viewed pg number
MIN_PAGE = 1 #the earliest page number
MAX_PAGE = 150 #the last page number

def update_csv(DF,random_number):
    """Updates the dataframe and resaves the CSV

    Args:
        DF (dataframe): dataframe from original csv that will be modified and updated
        random_number (int): the page number that was randomly generated and will get \
            iterated in the DF
    """
    DF.loc[DF['Page number'] == random_number,'Number of times randomised'] += 1
    DF.to_csv(PATH,index=False)
    label_saved.configure(text='Page number saved')

def ran_gen(DF):
    """generates a random number and displays the number based on position of number

    Args:
        DF (dataframe): dataframe from original csv that will be modified and updated
    """
    min_count = DF['Number of times randomised'].min()
    max_count = DF['Number of times randomised'].max()

    if min_count == max_count:
        random_number = random.randint(MIN_PAGE,MAX_PAGE)
    else:
        #generate a random number to determine recall percentage
        recall_random = random.randint(1,100)

        if recall_random >= RECALL_PERCENT: #if greater than % of times we want to revisit a pg
            #df_series is a series of the page numbers where number of times randomised == min_count
            df_series = DF.loc[DF['Number of times randomised'] == min_count,'Page number']
            random_number = df_series.iloc[random.randint(0,len(df_series)-1)] \
                #inclusive of both values
        else: #select a page visited recently
            #df_series is a series of the page numbers where number of times randomised == min_count
            df_series = DF.loc[DF['Number of times randomised'] != min_count,'Page number']
            random_number = df_series.iloc[random.randint(0,len(df_series)-1)] \
                #inclusive of both values
            print(recall_random)
            print(random_number)
    label_saved.configure(text='') #clear saved text
    label_random.configure(text=random_number)
    #generate label position
    x_pos, y_pos = label_position(random_number)
    label_random.place(x = x_pos, y = y_pos)

def label_position(random_number):
    """determines the x and y coordinates for the label position

    Args:
        random_number (int): random number that was generated

    Returns:
        x int: x coordinates for label position
        y int: y coordinates for label position
    """
    num_length = len(str(random_number))
    if num_length == 3:
        x_position = 325
        y_position = 200
    elif num_length == 2:
        x_position = 375
        y_position = 200
    elif num_length == 1:
        x_position = 400
        y_position = 200
    return x_position, y_position

if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.geometry('900x600')
    main_window.title('The Pocket Universal Principles of Design Page Randomiser')

    #declare label to confirm page number has been updated
    label_saved = tkinter.Label(main_window, text='', font=('Helvetica',10))
    label_saved.place(x=380, y=150)
    #declare label to display random number
    label_random = tkinter.Label(main_window, text='', font=('Helvetica',100))

    #button to generate a new random number
    button_random = tkinter.Button(main_window, text='Randomise',
                             command=lambda: ran_gen(DF), width=12, bg='white')
    button_random.place(x=250, y=115)

    #button to close the window
    button_close = tkinter.Button(main_window, text='Quit',
                             command=main_window.destroy, width=12, bg='white')
    button_close.place(x=600, y=115)

    ran_gen(DF) #generate first instance of random number

    #button to confirm the page has been read
    button_read = tkinter.Button(main_window, text='I read the page',
                             command= lambda: update_csv(DF,int(label_random['text'])),
                             width=12, bg='white')
    button_read.place(x=400, y=115)

    main_window.mainloop()
