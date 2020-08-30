from tkinter import *
import tkinter as tk

HEIGHT = 450
WIDTH = 550

date = 0
month = 0
finaldate =""

root = tk.Tk()
root.resizable(False, False)
root.iconbitmap('party.ico')
root.title('Birthdate Guesser')

background_image = tk.PhotoImage(file='birthdate.png')
setbackground_image = tk.PhotoImage(file='birthdate1.png')
firebackground_image = tk.PhotoImage(file='firebirth2.png')


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='green')
canvas.pack()

def openingPage():
    coverbg = tk.Frame(root, bg='pink')
    coverbg.place(relwidth=1, relheight=1)

    coverpage = tk.Frame(coverbg, bg='pink')
    coverpage.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    opentext = tk.Button(coverpage,text='I CAN GUESS YOUR BIRTH DATE!\n Click anywhere to continue', image=background_image, font='Helvetica 17 bold',bg='pink', relief='flat', command=lambda :setA())
    opentext.place(relwidth=1, relheight=1)
openingPage()

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
    global finaldate
    datewithmonth = date
    if date == 0:
        finaldate = ""
    elif date == 1:
        finaldate = " 1ST"
    elif date == 2:
        finaldate = " 2ND"
    elif date == 3:
        finaldate = " 3RD"
    elif date == 4:
        finaldate = " 4TH"
    elif date == 5:
        finaldate = " 5TH"
    elif date == 6:
        finaldate = " 6TH"
    elif date == 7:
        finaldate = " 7TH"
    elif date == 8:
        finaldate=" 8TH"
    elif date == 9:
        finaldate=" 9TH"
    elif date == 10:
        finaldate=" 10TH"
    elif date == 11:
        finaldate=" 11TH"
    elif date == 12:
        finaldate=" 12TH"
    elif date == 13:
        finaldate=" 13TH"
    elif date == 14:
        finaldate=" 14TH"
    elif date == 15:
        finaldate=" 15TH"
    elif date == 16:
        finaldate=" 16TH"
    elif date == 17:
        finaldate=" 17TH"
    elif date == 18:
        finaldate=" 18TH"
    elif date == 19:
        finaldate=" 19TH"
    elif date == 20:
        finaldate=" 20TH"
    elif date == 21:
        finaldate=" 21ST"
    elif date == 22:
        finaldate=" 22ND"
    elif date == 23:
        finaldate=" 23RD"
    elif date == 24:
        finaldate=" 24TH"
    elif date == 25:
        finaldate=" 25TH"
    elif date == 26:
        finaldate=" 26TH"
    elif date == 27:
        finaldate=" 27TH"
    elif date == 28:
        finaldate=" 28TH"
    elif date == 29:
        finaldate=" 29TH"
    elif date == 30:
        finaldate=" 30TH"
    else:
        finaldate=" 31ST"
    anotherfinaldate = finaldate


    date = 0
    monthA()
    return finaldate



def monthA():
    setbackground = tk.Frame(root, bg='gray')
    setbackground.place(relwidth=1, relheight=1)
    setbackgroundlabel = tk.Label(setbackground, image=setbackground_image)
    setbackgroundlabel.place(relwidth=1, relheight=1)

    monthAFrame = tk.Frame(setbackground, bg='#9C5AFD')
    monthAFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    monthAQuestion = tk.Label(monthAFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 14 bold', bg='#9C5AFD')
    monthAQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    monthADates = tk.Label(monthAFrame,
                         text='\nJAN\tMAR\tMAY\n\n\nJUL\tSEP\tNOV\n',
                         font='Helvetica 17 bold')

    monthADates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    AYes = tk.Button(monthAFrame, text='YES', font='Helvetica 12 bold', command=lambda:monthYesA())
    AYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    ANo = tk.Button(monthAFrame, text='NO', font='Helvetica 12 bold', command=lambda:monthNoA())
    ANo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)

def monthYesA():
    global month
    month = month + 1
    monthB()
    return month

def monthNoA():
    global month
    month = month + 0
    monthB()
    return month


def monthB():
    monthBFrame = tk.Frame(root, bg='#FDB0FE')
    monthBFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    monthBQuestion = tk.Label(monthBFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 14 bold',
                              bg='#FDB0FE')
    monthBQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    monthADates = tk.Label(monthBFrame,
                           text='\nFEB\tMAR\tJUN\n\n\nJUL\tOCT\tNOV\n',
                           font='Helvetica 17 bold')

    monthADates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    BYes = tk.Button(monthBFrame, text='YES', font='Helvetica 12 bold', command=lambda: monthYesB())
    BYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    ANo = tk.Button(monthBFrame, text='NO', font='Helvetica 12 bold', command=lambda: monthNoB())
    ANo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)


def monthYesB():
    global month
    month = month + 2
    monthC()
    return month


def monthNoB():
    global month
    month = month + 0
    monthC()
    return month


def monthC():
    monthCFrame = tk.Frame(root, bg='#27DDFE')
    monthCFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    monthCQuestion = tk.Label(monthCFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 14 bold',
                              bg='#27DDFE')
    monthCQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    monthCDates = tk.Label(monthCFrame,
                           text='\nAPR\tMAY\tJUN\n\n\nJUL\tDEC\tXXX\n',
                           font='Helvetica 17 bold')

    monthCDates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    CYes = tk.Button(monthCFrame, text='YES', font='Helvetica 12 bold', command=lambda: monthYesC())
    CYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    CNo = tk.Button(monthCFrame, text='NO', font='Helvetica 12 bold', command=lambda: monthNoC())
    CNo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)


def monthYesC():
    global month
    month = month + 4
    monthD()
    return month


def monthNoC():
    global month
    month = month + 0
    monthD()
    return month


def monthD():
    monthDFrame = tk.Frame(root, bg='#02AD99')
    monthDFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    monthDQuestion = tk.Label(monthDFrame, text='Is Your Birth Date In This Set Of Dates?', font='Helvetica 14 bold',
                              bg='#02AD99')
    monthDQuestion.place(relx=0.5, rely=0.05, relwidth=0.65, relheight=0.1, anchor='n')

    monthDDates = tk.Label(monthDFrame,
                           text='\nAUG\tSEP\tOCT\n\n\nNOV\tDEC\tXXX\n',
                           font='Helvetica 17 bold')

    monthDDates.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.6, anchor='n')

    CYes = tk.Button(monthDFrame, text='YES', font='Helvetica 12 bold', command=lambda: monthYesD())
    CYes.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)

    CNo = tk.Button(monthDFrame, text='NO', font='Helvetica 12 bold', command=lambda: monthNoD())
    CNo.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)


def monthYesD():
    global month
    month = month + 8
    birthday()
    return month


def monthNoD():
    global month
    month = month + 0
    birthday()
    return month

def birthday():
    global month
    global finaldate
    datewithmonth = date
    if  finaldate == "":
        finalmonth = "You don't have a Birthday!\n Try Again"
    elif month == 0:
        finalmonth = "You don't have a Birthday!\n Try Again"
    elif finaldate == "" and month == 0:
        finalmonth = "You don't have a Birthday!\n Try Again"
    elif month == 1:
        finalmonth = "You were born on the\n" + finaldate + " of JANUARY!"
    elif month == 2:
        finalmonth = "You were born on the\n" + finaldate + " of FEBRUARY!"
    elif month == 3:
        finalmonth = "You were born on the\n" + finaldate + " of MARCH!"
    elif month == 4:
        finalmonth = "You were born on the\n" + finaldate + " of APRIL!"
    elif month == 5:
        finalmonth = "You were born on the\n" + finaldate + " of MAY!"
    elif month == 6:
        finalmonth = "You were born on the\n" + finaldate + " of JUNE!"
    elif month == 7:
        finalmonth = "You were born on the\n" + finaldate + " of JULY!"
    elif month == 8:
        finalmonth="You were born on the\n" + finaldate + " of AUGUST!"
    elif month == 9:
        finalmonth="You were born on the\n" + finaldate + " of SEPTEMBER!"
    elif month == 10:
        finalmonth="You were born on the\n" + finaldate + " of OCTOBER!"
    elif month == 11:
        finalmonth="You were born on the\n" + finaldate + " of NOVEMBER!"
    else :
        finalmonth="You were born on the\n" + finaldate + " of DECEMBER!"
    month = 0


    dateFrame = tk.Frame(root)
    dateFrame.place(relwidth=1, relheight=1)
    background_label = tk.Label(dateFrame, text=finalmonth + '\n', font='Helvetica 28 bold', fg='white', image=firebackground_image, compound='center')
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    againbutton = tk.Button(dateFrame, text='Try Again!', font='Helvetica 12 bold', command= lambda:openingPage() )
    againbutton.place(relx=0.1, rely=0.85,  relwidth=0.2, relheight=0.1)

    exitbutton = tk.Button(dateFrame, text='Exit', font='Helvetica 12 bold',command = lambda :quit())
    exitbutton.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1)


root.mainloop()