from tkinter import *

username = 'Pedro Rodríguez Díaz'

def print_result(n):
    probs = {1: result1}
    probs[1].set('Hi')

window = Tk()
window.geometry('1000x500')

#-------------------------------HEADER-------------------------------------

header = LabelFrame(window, height=80, bd=5)
header.pack(fill=X, side=TOP)

appName = Label(header, text='CodeTester', font=('Consolas', 40))
appName.pack(side=LEFT, padx=20)

name = Label(header, text=username, bd=5, font=('Consolas', 14), anchor=E)
name.pack(side=BOTTOM, fill=BOTH, padx= 20)

pointsWord =  Label(header, text='points', font=('Consolas', 20))
pointsWord.pack(side=RIGHT, padx=20)

points = StringVar()
counter =  Label(header, textvariable=points, font=('Consolas', 40))
counter.pack(side=RIGHT)
points.set('0')

#-------------------------------PROBLEMS-------------------------------------

problems = LabelFrame(window, height=900, bd=5)
problems.pack(fill=BOTH, side=TOP)

problem1 = LabelFrame(problems, text='Problem 1', font=('Consolas', 15),height=90, bd=5)
problem1.pack(fill=X, side=TOP, padx=20, pady=10)

p1Button = Button(problem1, text='Submit', command=lambda: print_result(1), width=15, font='Consolas', relief=RAISED)
p1Button.pack(side=LEFT, padx=10, pady=10)

result1 = StringVar()
result1Label =  Label(problem1, textvariable=result1, font=('Consolas', 10), width=100, bg='grey80', height=2, anchor=W, padx=10)
result1Label.pack(side=LEFT, padx=30)
result1.set('Tests results')

window.mainloop()