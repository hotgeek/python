from tkinter import Tk
import tkinter
from tkinter import *

def calculate_gravitational_force():
    m1 = float(m1_string.get())
    m2 = float(m2_string.get())
    d = float(d_string.get())

    G = 6.67 * (10 ** -11)
    F = (G * m1 * m2) / (d ** 2)

    result_label.configure(text=str(F))


def main():
    global m1_string
    global m2_string
    global d_string
    global result
    global result_label

    root_window = Tk()
    root_window.title("Gravitational Force")

    m1_lable = Label(root_window)
    m1_lable.configure(text="Enter m1")
    m1_string = StringVar()
    m1_text_box = Entry(root_window, textvariable=m1_string)

    m2_lable = Label(root_window)
    m2_lable.configure(text="Enter m2")
    m2_string = StringVar()
    m2_text_box = Entry(root_window, textvariable=m2_string)

    d_lable = Label(root_window)
    d_lable.configure(text="Enter distance between 2 masses")
    d_string = StringVar()
    d_text_box = Entry(root_window, textvariable=d_string)

    result_string_label = Label(root_window)
    result_string_label.configure(text="Gravitational Force is: ")

    result_label = Label(root_window)
    

    calculate_button = Button(root_window)
    calculate_button.configure(text="Calculate Gravitatonal Force", command=calculate_gravitational_force)

    m1_lable.grid(row=0, column=0,)
    m1_text_box.grid(row=0, column=1)

    m2_lable.grid(row=1, column=0)
    m2_text_box.grid(row=1, column=1)

    d_lable.grid(row=2, column=0)
    d_text_box.grid(row=2, column=1)

    calculate_button.grid(row=4, column=1)

    result_string_label.grid(row=5, column=0)
    result_label.grid(row=5, column=1)

    root_window.mainloop()

main()