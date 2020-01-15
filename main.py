#!/usr/bin/python3

from tkinter import *

# from PIL import Image, ImageTk # Named Pillow on pip

import os

import json

import time


# ----- Parameters -------
n_problems = 10
username = ''
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
    problems_points = {0: 1, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 8, 8: 12, 9: 18}

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
        # self.message.set('Running tests')
        # time.sleep(1)

        try:
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
                if self.state != 'All tests passed': # para que sólo se sumen si estaba mal hecho
                    self.state = result
                self.message.set(result)
        except Exception as e:
            self.message.set(f'A {repr(e)} error ocurred') # for showing on the app which error occured

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

problems1 = LabelFrame(window, bd=0)
problems1.pack(fill=BOTH, side=TOP, expand=True)

canvas = Canvas(problems1)
problems = Frame(canvas, bd=0)
vbar = Scrollbar(problems1, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=vbar.set, width=500, height=700)

vbar.pack(side=RIGHT, fill=Y)
canvas.pack(side=LEFT,expand=True, fill=BOTH)
canvas.create_window((4,4), window=problems, anchor="nw", tags="frame")

# problems.pack(fill=BOTH, side=TOP)
problems.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all"))
)

#n = 2

for i in range(n_problems): # n es la cantidad de problemas
    NewProblem(i)

# load = Image.open("image.png").resize((20, 20))
# render = ImageTk.PhotoImage(load)
authors = Label(window, text='Made and supported with love by Korven48 and Dirox00', font=('Consolas', 9))#, image=render)
# authors.image = render
authors.pack(side=BOTTOM, padx=20)

window.mainloop()