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

class NewProblem:
    def __init__(self, num):
        self.num = num
        self.message = StringVar()

        problem = LabelFrame(problems, text=f'Problem {self.num}', font=('Consolas', 15),height=90, bd=0)
        problem.pack(fill=X, side=TOP, padx=20, pady=10)

        button = Button(problem, text='Submit', command=check, width=15, font='Consolas', relief=RAISED)
        button.pack(side=LEFT, padx=10, pady=10)

        resultLabel =  Label(problem, textvariable=self.message, font=('Consolas', 10), width=100, bg='grey80', height=2, anchor=W, padx=10)
        resultLabel.pack(side=LEFT, padx=30)
        self.message.set('Tests results')
    
    def check(self):
        my_file = input()
        actual_problem = problems_dict[str(self.num)]
        probs = {1: result1, 2: result2}
        self.message.set(f'Running test {self.num}')
        os.system(f'./test.sh {my_file} {actual_problem["solucion"]} {actual_problem["generador"]}')
        with open('result', 'r') as f:
            result = f.read().replace('\self.num', '')

        if result == 'All tests passed' and data[str(self.num)] != 'All tests passed':
            data['points'] += 10
            data[str(self.num)] = 'All tests passed'
            self.message.set('All tests passed')
            points.set(data['points'])
        else:
            data[str(self.num)] = result
            self.message.set(result)
        
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

problems = LabelFrame(window, height=900)
problems.pack(fill=BOTH, side=TOP)

for i in range(5):
    NewProblem(i)

window.mainloop()