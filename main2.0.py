#!/usr/bin/python3

from tkinter import *

import os

import json


username = 'Pepe Palotes'

with open('data.json', 'r') as f:
    file = f.read()
data = json.loads(file)

with open('problems.json', 'r') as f:
    file = f.read()
problems_dict = json.loads(file)

def check(n):
    actual_problem = problems_dict[str(n)]
    probs = {1: result1, 2: result2}
    probs[n].set(f'Running test {n}')
    os.system(f'./test.sh try.py {actual_problem["solucion"]} {actual_problem["generador"]}')
    with open('result', 'r') as f:
        result = f.read().replace('\n', '')

    if result == 'All tests passed' and data[str(n)] != 'All tests passed':
        data['points'] += 10
        data[str(n)] = 'All tests passed'
        points.set(data['points'])
    else:
        data[str(n)] = result
        probs[n].set(result)
    
    with open('data.json', 'w') as f:
        json.dump(data, f)


window = Tk()
window.geometry('1000x500')

#-------------------------------HEADER-------------------------------------

header = LabelFrame(window, height=80, bd=0)#bd=5
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
points.set(data['points'])

#-------------------------------PROBLEMS-------------------------------------

problems = LabelFrame(window, height=900, bd=0)
problems.pack(fill=BOTH, side=TOP)

problem1 = LabelFrame(problems, text='Problem 1', font=('Consolas', 15),height=90, bd=0)#bd=5
problem1.pack(fill=X, side=TOP, padx=20, pady=10)

p1Button = Button(problem1, text='Submit', command=lambda: check(1), width=15, font='Consolas', relief=RAISED)
p1Button.pack(side=LEFT, padx=10, pady=10)

#...........................Problem2................................................ 

problem2 = LabelFrame(problems, text='Problem 2', font=('Consolas', 15),height=90, bd=0)#bd=5
problem2.pack(fill=X, side=TOP, padx=20, pady=10)

p2Button = Button(problem2, text='Submit', command=lambda: check(2), width=15, font='Consolas', relief=RAISED)
p2Button.pack(side=LEFT, padx=10, pady=10)


result1 = StringVar()
result1.set('Test results')
result1Label =  Label(problem1, textvariable=result1, font=('Consolas', 10), width=100, bg='grey80', height=2, anchor=W, padx=10)
result1Label.pack(side=LEFT, padx=30)

result2 = StringVar()
result2.set('Test results')
result2Label =  Label(problem2, textvariable=result2, font=('Consolas', 10), width=100, bg='grey80', height=2, anchor=W, padx=10)
result2Label.pack(side=LEFT, padx=30)

window.mainloop()
