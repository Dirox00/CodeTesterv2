#!/usr/bin/python3

from tkinter import *

# from PIL import Image, ImageTk # Named Pillow on pip

import os

import json

# ----- Parameters -------
n_problems = 8
username = 'Pepe Palotes'
points_ = 0
#-------------------------

CURRENT_DIR = os.getcwd()
problems_path = CURRENT_DIR + '/Problems/' #Dirección de carpeta con problemas
attempts_path = CURRENT_DIR + '/Attempts/'
generators_path = CURRENT_DIR + '/Generators/'


os.system('chmod 744 -R .') 
# Da permisos de ejecucción, lectura y escritura a
# todos los programas y carpetas contenidos en el directorio local
 
class NewProblem():
    problems_points = {1: 10, 2: 20, 3:30, 4:40, 5:50}

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

        self.attempt = attempts_path + f'problema_{self.num}.py'

        # Compara el programa del usuario y la solución
        os.system(f'./test.sh {self.attempt} {self.solution} {self.generator}')
        
        # Comprueba el resultado
        with open('result', 'r') as f:
            result = f.read().replace('\n', '')

        # Actualiza la app según el resultado
        if result == 'All tests passed' and self.state != 'All tests passed':
            points_ += self.problems_points[self.num]
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
points.set(0)

#-------------------------------PROBLEMS-------------------------------------

problems = LabelFrame(window, bd=0)
problems.pack(fill=BOTH, side=TOP)

#n = 2

for i in range(1, n_problems + 1): # n es la cantidad de problemas
    NewProblem(i)

# load = Image.open("image.png").resize((20, 20))
# render = ImageTk.PhotoImage(load)
authors = Label(window, text='Made and supported with love by Korven48 and Dirox00', font=('Consolas', 9))#, image=render)
# authors.image = render
authors.pack(side=BOTTOM, padx=20)

window.mainloop()