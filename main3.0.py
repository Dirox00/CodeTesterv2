from tkinter import *


class NewProblem:
    def __init__(self, num):
        self.num = num
        self.result = StringVar()

        problem = LabelFrame(problems, text=f'Problem {self.num}', font=('Consolas', 15),height=90, bd=0)
        problem.pack(fill=X, side=TOP, padx=20, pady=10)

        button = Button(problem, text='Submit', command=self.change, width=15, font='Consolas', relief=RAISED)
        button.pack(side=LEFT, padx=10, pady=10)

        resultLabel =  Label(problem, textvariable=self.result, font=('Consolas', 10), width=100, bg='grey80', height=2, anchor=W, padx=10)
        resultLabel.pack(side=LEFT, padx=30)
        self.result.set('Tests results')

    def change(self):
        self.result.set('hi')
        

window = Tk()
window.geometry('1000x500')

problems = LabelFrame(window, height=900)
problems.pack(fill=BOTH, side=TOP)

for i in range(5):
    NewProblem(i)

window.mainloop()