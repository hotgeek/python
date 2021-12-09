
import tkinter
import sys

def main():
    root_window = tkinter.Tk()
    root_window.title("Concept Demo")

    label = tkinter.Label(root_window)
    label.configure(text="test label")
    label.pack(side=tkinter.LEFT, expand=tkinter.YES, anchor=tkinter.E)

    button = tkinter.Button(root_window)
    button.configure(text="asas")
    button.pack(side=tkinter.RIGHT)
    root_window.mainloop()
main()