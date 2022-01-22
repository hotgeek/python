from tkinter import *
from tkinter import simpledialog
from tkinter.simpledialog import *
import sys

ans_lb = None

def main():
    global ans_lb
    root_window = Tk()
    root_window.title("QSolver dialog")
    a = askfloat("Input", "Enter CF of x**2")
    b= askfloat("Input", "Enter CF of x")
    c = askfloat("Input", "Enter the constant")

    if b**2 - 4*a*c < 0:
        text_ans = "This equation does not have roots in real"
    else:
        root_1 = (-b + (b ** 2 - 4 * a * c) * 0.5) / (2*a)
        root_2 = (-b - (b ** 2 - 4 * a * c) * 0.5) / (2*a)
        text_ans = "Root 1 = %.2f, Root 2 = %.2f" % (root_1, root_2)

    if ans_lb:
        ans_lb.destroy()

    ans_lb = Label(root_window, text=text_ans)
    ans_lb.grid(row=0, column=1, sticky=E)

    root_window.mainloop()

main()