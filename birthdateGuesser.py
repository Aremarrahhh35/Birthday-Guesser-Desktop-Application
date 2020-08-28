from tkinter import *
import tkinter as tk

HEIGHT = 450
WIDTH = 550

date = 0


root = tk.Tk()
root.resizable(False, False)
root.iconbitmap('party.ico')
root.title('Birthdate Guesser')

background_image = tk.PhotoImage(file='birthdate.png')
setbackground_image = tk.PhotoImage(file='birthdate1.png')
firebackground_image = tk.PhotoImage(file='firebirth2.png')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='green')
canvas.pack()

coverbg = tk.Frame(root, bg='pink')
coverbg.place(relwidth=1, relheight=1)

coverpage = tk.Frame(coverbg, bg='pink')
coverpage.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

opentext = tk.Button(coverpage,text='I CAN GUESS YOUR BIRTH DATE!\n Click anywhere to continue', image=background_image, font='Helvetica 17 bold',bg='pink', relief='flat', command=lambda :setA())
opentext.place(relwidth=1, relheight=1)


def setA():
    setbackground = tk.Frame(root, bg='gray')
    setbackground.place(relwidth=1, relheight=1)
    setbackgroundlabel = tk.Label(setbackground, image=setbackground_image)
    setbackgroundlabel.place(relwidth=1, relheight=1)

    setAFrame = tk.Frame(setbackground, bg='#FDB0FE')
    setAFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    setAQuestion = tk.Label(setAFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 12 bold', bg='#FDB0FE')
    setAQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    setADates = tk.Label(setAFrame, text='1\t3\t5\t7\n\n 9\t 11 \t 13 \t 15\n\n 17 \t 19 \t 21 \t 23\n\n 25 \t 27 \t 29 \t 31 ', font='Helvetica 17 bold')
    setADates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    setAYes = tk.Button(setAFrame, text='YES', font='Helvetica 12 bold', command=lambda:yesA())
    setAYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    setANo = tk.Button(setAFrame, text='NO', font='Helvetica 12 bold', command=lambda:noA())
    setANo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)

def yesA():
    global date
    date = date + 1
    setB()
    return date

def noA():
    global date
    date = date + 0
    setB()
    return date

def setB():
    setBFrame = tk.Frame(root, bg='#9C5AFD')
    setBFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    setBQuestion = tk.Label(setBFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 12 bold', bg='#9C5AFD')
    setBQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    setBDates = tk.Label(setBFrame,
                         text=' 2\t3\t6\t7\n\n 10\t11\t14\t15\n\n 18\t19\t22\t23\n\n 26\t27\t30\t31',
                         font='Helvetica 17 bold')

    setBDates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    setBYes = tk.Button(setBFrame, text='YES', font='Helvetica 12 bold', command=lambda:yesB())
    setBYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    setBNo = tk.Button(setBFrame, text='NO', font='Helvetica 12 bold', command=lambda:noB())
    setBNo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)

def yesB():
    global date
    date = date + 2
    setC()
    return date

def noB():
    global date
    date = date + 0
    setC()
    return date


def setC():
    setCFrame = tk.Frame(root, bg='#44CDFE')
    setCFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    setCQuestion = tk.Label(setCFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 12 bold', bg='#44CDFE')
    setCQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    setCDates = tk.Label(setCFrame,
                         text=' 4\t5\t6\t7\n\n 12\t13\t14\t15\n\n 20\t21\t22\t23\n\n 28\t29\t30\t31',
                         font='Helvetica 17 bold')

    setCDates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    setCYes = tk.Button(setCFrame, text='YES', font='Helvetica 12 bold', command=lambda:yesC())
    setCYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    setCNo = tk.Button(setCFrame, text='NO', font='Helvetica 12 bold', command=lambda:noC())
    setCNo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)

def yesC():
    global date
    date = date + 4
    setD()
    return date

def noC():
    global date
    date = date + 0
    setD()
    return date


def setD():
    setDFrame = tk.Frame(root, bg='#27DDFE')
    setDFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    setDQuestion = tk.Label(setDFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 12 bold', bg='#27DDFE')
    setDQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    setDDates = tk.Label(setDFrame,
                         text=' 8\t9\t10\t11\n\n 12\t13\t14\t15\n\n 24\t25\t26\t27\n\n 28\t29\t30\t31',
                         font='Helvetica 17 bold')

    setDDates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    setDYes = tk.Button(setDFrame, text='YES', font='Helvetica 12 bold', command=lambda: yesD())
    setDYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    setDNo = tk.Button(setDFrame, text='NO', font='Helvetica 12 bold', command=lambda: noD())
    setDNo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)


def yesD():
    global date
    date = date + 8
    setE()
    return date


def noD():
    global date
    date = date + 0
    setE()
    return date


def setE():
    setEFrame = tk.Frame(root, bg='#02AD99')
    setEFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    setEQuestion = tk.Label(setEFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 12 bold', bg='#02AD99')
    setEQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    setEDates = tk.Label(setEFrame,
                         text='16\t17\t18\t19\n\n 20\t21\t22\t23\n\n 24\t25\t26\t27\n\n 28\t29\t30\t31',
                         font='Helvetica 17 bold')

    setEDates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    setEYes = tk.Button(setEFrame, text='YES', font='Helvetica 12 bold', command=lambda: yesE())
    setEYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    setENo = tk.Button(setEFrame, text='NO', font='Helvetica 12 bold', command=lambda: noE())
    setENo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)


def yesE():
    global date
    date = date + 16
    birthdate()
    return date


def noE():
    global date
    date = date + 0
    birthdate()
    return date


def birthdate():
    global date
    if date == 0:
        finaldate = "You don't have a Birth Date!"
    elif date == 1:
        finaldate = "You were born on the 1ST!"
    elif date == 2:
        finaldate = "You were born on the 2ND!"
    elif date == 3:
        finaldate = "You were born on the 3RD!"
    elif date == 4:
        finaldate = "You were born on the 4TH!"
    elif date == 5:
        finaldate = "You were born on the 5TH!"
    elif date == 6:
        finaldate = "You were born on the 6TH!"
    elif date == 7:
        finaldate = "You were born on the 7TH!"
    elif date == 8:
        finaldate="You were born on the 8TH!"
    elif date == 9:
        finaldate="You were born on the 9TH!"
    elif date == 10:
        finaldate="You were born on the 10TH!"
    elif date == 11:
        finaldate="You were born on the 11TH!"
    elif date == 12:
        finaldate="You were born on the 12TH!"
    elif date == 13:
        finaldate="You were born on the 13TH!"
    elif date == 14:
        finaldate="You were born on the 14TH!"
    elif date == 15:
        finaldate="You were born on the 15TH!"
    elif date == 16:
        finaldate="You were born on the 16TH!"
    elif date == 17:
        finaldate="You were born on the 17TH!"
    elif date == 18:
        finaldate="You were born on the 18TH!"
    elif date == 19:
        finaldate="You were born on the 19TH!"
    elif date == 20:
        finaldate="You were born on the 20TH!"
    elif date == 21:
        finaldate="You were born on the 21ST!"
    elif date == 22:
        finaldate="You were born on the 22ND!"
    elif date == 23:
        finaldate="You were born on the 23RD!"
    elif date == 24:
        finaldate="You were born on the 24TH!"
    elif date == 25:
        finaldate="You were born on the 25TH!"
    elif date == 26:
        finaldate="You were born on the 26TH!"
    elif date == 27:
        finaldate="You were born on the 27TH!"
    elif date == 28:
        finaldate="You were born on the 28TH!"
    elif date == 29:
        finaldate="You were born on the 29TH!"
    elif date == 30:
        finaldate="You were born on the 30TH!"
    else:
        finaldate="You were born on the 31ST!"

    dateFrame = tk.Frame(root)
    dateFrame.place(relwidth=1, relheight=1)
    background_label = tk.Label(dateFrame, text=finaldate, font='Helvetica 30 bold', fg='white', image=firebackground_image, compound='center')
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


root.mainloop()