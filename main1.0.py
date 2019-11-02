import os

from tkinter import *

username = 'Pedro' 

points = 0

#program1 = False

def check(problem):
    state0.set(f'Running test {problem}')
    os.system('./test.sh try.py correct.py')
    with open('result', 'r') as f:
        result = f.read()

    state0.set(result)
#    if result == 'All tests passed' and not program1:
        #message2.set(str(10))

window = Tk()

#-----------------------PROBLEMS-------------------------------
label0 = LabelFrame(window)
label0.grid(row=0, column=0)

l0 = Label(label0, text=f'Problema 0', width=10)
l0.grid(row=0, column=0, pady=10)

b0 = Button(label0, text=f'Check', command= lambda: check(0))
b0.grid(row=0, column=1, padx=10, pady=10)

state0 = StringVar()
l00 = Label(label0, textvariable=state0)
l00.grid(row=1, column=0, pady=10, columnspan=2) 
state0.set('No tests passed yet')

#-----------------------RESULTS-------------------------------
label1 = LabelFrame(window)
label1.grid(row=0, column=1)

l1 = Label(label1, text=f'Username: {username}', width=20)
l1.grid(row=0, column=0, pady=10, columnspan=2)

l11 = Label(label1, text='Points', width=10)
l11.grid(row=1, column=0, pady=10)

message2 = StringVar()
l12 = Label(label1, textvariable=message2, width=10)
l12.grid(row=1, column=1, pady=10)
message2.set(points)

window.mainloop()

