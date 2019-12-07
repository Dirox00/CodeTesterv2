#!/usr/bin/python3

from tkinter import *
import os

CURRENT_DIR = os.getcwd()
problems_path = CURRENT_DIR + '/Problems/' #Dirección de carpeta con problemas
attempts_path = CURRENT_DIR + '/Attempts/'
generators_path = CURRENT_DIR + '/Generators/'

class NewProblem():
    def __init__(self, num):
        global problems
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
