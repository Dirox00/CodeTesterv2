#!/usr/bin/python3

from tkinter import *
import os
import json

CURRENT_DIR = os.getcwd()
problems_path = CURRENT_DIR + '/Problems/' #Dirección de carpeta con problemas
attempts_path = CURRENT_DIR + '/Attempts/'
generators_path = CURRENT_DIR + '/Generators/'
username = 'Pepe Palotes'
points_ = 0

class NewProblem():
    def __init__(self, num):
        self.num = num
        self.state = 'Test results'
        self.message = StringVar()
        self.solution = problems_path + f'solution_{self.num}.py'
        self.generator = generators_path + f'generator_{self.num}.py'

        problem = LabelFrame(problems, text=f'Problem {self.num}', font=('Consolas', 15),height=90, bd=0)
        problem.pack(fill=X, side=TOP, padx=20, pady=10)

        button = Button(problem, text='Submit', command=self.check, width=15, font='Consolas', relief=RAISED)
        button.pack(side=LEFT, padx=10, pady=10)

        resultLabel =  Label(problem, textvariable=self.message, font=('Consolas', 10), width=100, bg='grey80', height=2, anchor=W, padx=10)
        resultLabel.pack(side=LEFT, padx=30)
        self.message.set(self.state)
    
    def check(self):
        global points_

        #self.message.set('Running tests') # {self.num}
        self.attempt = attempts_path + f'problema_{self.num}.py'

        os.system(f'./test.sh {self.attempt} {self.solution} {self.generator}')
        with open('result', 'r') as f:
            result = f.read().replace('\n', '')

        if result == 'All tests passed' and self.state != 'All tests passed':
            points_ += 10
            self.state = 'All tests passed'
            self.message.set('All tests passed')
            points.set(points_)
        else:
            self.state = result
            self.message.set(result)


window = Tk()
window.geometry('700x500')

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
points.set(points_)

#-------------------------------PROBLEMS-------------------------------------

problems = LabelFrame(window, bd=0)
problems.pack(fill=BOTH, side=TOP)

n = 2

for i in range(1, n + 1): # n es la cantidad de problemas
    NewProblem(i)

window.mainloop()