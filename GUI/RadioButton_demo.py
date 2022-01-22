from tkinter import *
import sys

class MyButton:    

    def __init__(self, btn_text):
        self.button = Button(text="My custom button")


def course_selector():
    v = choice.get()
    dsp_text = None    
    lb= None

    if v==1:
        dsp_text="You have selected Core Python Programming"
    elif v == 2:
        dsp_text="You have selected Masterclass in C"
    elif v == 3:
        dsp_text="You have selected Data Structures and Algorithms"

    if lb:
        lb.destroy()

    lb = Label(root_window, text=dsp_text)
    lb.grid(row=3, column=1, sticky=W)

def main():
    global root_window, choice 
    root_window = Tk()
    root_window.title("Course Selector")

    choice = IntVar()
    option_1 = Radiobutton(root_window, text="CPA 106", variable=choice, value=1, command=course_selector, anchor=W)
    option_2 = Radiobutton(root_window, text="CPA 102", variable=choice, value=2, command=course_selector, anchor=W)
    option_3 = Radiobutton(root_window, text="CPA 101", variable=choice, value=3, command=course_selector, anchor=W)

    option_1.grid(row=0, column=1, sticky=W)
    option_2.grid(row=1, column=1, sticky=W)
    option_3.grid(row=2, column=1, sticky=W)

    root_window.mainloop()

main()

