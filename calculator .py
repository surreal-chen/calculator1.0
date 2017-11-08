from tkinter import *

window = Tk()
window.title("计算器")
#textEntry.set('0')
frame1 = Frame(window)
frame1.pack(expand=YES,fill=BOTH)
#frame2 = Frame(frame1).grid(row = 1, column = 0, sticky = N+S+W+E)
textEntry = StringVar()
ent = Entry(frame1, textvariable=textEntry, justify = RIGHT)
ent.grid(row = 0, column = 0,columnspan = 4)

def printPlus():
    ent.insert(INSERT,'+')
def printMinus():
    ent.insert(INSERT, '-')
def printMulti():
    ent.insert(INSERT, '*')
def printDivide():
    ent.insert(INSERT,'/')
def printPoint():
    ent.insert(INSERT,'.')
def printOne():
    ent.insert(INSERT, '1')
def printTwo():
    ent.insert(INSERT, '2')
def printThree():
    ent.insert(INSERT, '3')
def printFour():
    ent.insert(INSERT, '4')
def printFive():
    ent.insert(INSERT, '5')
def printSix():
    ent.insert(INSERT, '6')
def printSeven():
    ent.insert(INSERT, '7')
def printEight():
    ent.insert(INSERT, '8')
def printNine():
    ent.insert(INSERT, '9')
def printZero():
    ent.insert(INSERT, '0')
def isClear():
    ent.delete(0,END)
def printEqual():
    textEntry.set(eval(textEntry.get()))

btnBackspace = Button(frame1, text = '←').grid(row = 1, column = 0, sticky = N+S+W+E,)
btnClear = Button(frame1, text = 'C',command = isClear).grid(row = 1, column = 1, sticky = N+S+W+E)
btnSqrt = Button(frame1, text = 'Sqrt').grid(row = 1, column = 2, sticky = N+S+W+E)
btnPlus = Button(frame1, text = '+',command = printPlus).grid(row = 1, column = 3, sticky = N+S+W+E)
btn7 = Button(frame1, text = '7', command = printSeven).grid(row = 2, column = 0, sticky = N+S+W+E)
btn8 = Button(frame1, text = '8', command = printEight).grid(row = 2, column = 1, sticky = N+S+W+E)
btn9 = Button(frame1, text = '9', command = printNine).grid(row = 2, column = 2, sticky = N+S+W+E)
btnMinus = Button(frame1, text = '-',  command = printMinus).grid(row = 2, column = 3, sticky = N+S+W+E)
btn4 = Button(frame1, text = '4', command = printFour).grid(row = 3, column = 0, sticky = N+S+W+E)
btn5 = Button(frame1, text = '5', command = printFive).grid(row = 3, column = 1, sticky = N+S+W+E)
btn6 = Button(frame1, text = '6', command = printSix).grid(row = 3, column = 2, sticky = N+S+W+E)
btnMulti= Button(frame1, text = '*', command = printMulti).grid(row = 3, column = 3, sticky = N+S+W+E)
btn1 = Button(frame1, text = '1', command = printOne).grid(row = 4, column = 0, sticky = N+S+W+E)
btn2 = Button(frame1, text = '2', command = printTwo).grid(row = 4, column = 1, sticky = N+S+W+E)
btn3 = Button(frame1, text = '3', command = printThree).grid(row = 4, column = 2, sticky = N+S+W+E)
btnDivide = Button(frame1, text = '/', command = printDivide).grid(row = 4, column = 3, sticky = N+S+W+E)
btn0 = Button(frame1, text = '0', command = printZero).grid(row = 5, column = 0, sticky = N+S+W+E)
btnPoint = Button(frame1, text = '.', command = printPoint).grid(row = 5, column = 1, sticky = N+S+W+E)
btnEqual = Button(frame1, text = '=',command = printEqual).grid(row = 5, column = 2, columnspan = 2, sticky = N+S+W+E)



window.mainloop()