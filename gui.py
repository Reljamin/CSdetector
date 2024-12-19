import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Minion Tracker")
root.geometry("600x400")


csGoals = Label(root, text='Target C/S Per Minute: ').grid(row=0)
csGoalsEntry = Entry(root)
csGoalsEntry.grid(row=0, column=1)

mp3ToPlay = Label(root, text='MP3 to Play: ').grid(row=1)

displayMinionsMissed = Label(root, text='Display Minions Missed: ').grid(row=2)
var1 = IntVar()
Checkbutton(root, text='', variable=var1).grid(row=2, column=1, sticky=W)

root.mainloop()