import builtins
import sys
import tkinter

def my_handler():
    second_window = tkinter.Tk()
    second_window.title("this is test")

    second_window.mainloop()

def main():
    root_window = tkinter.Tk()
    root_window.title("Hello This is second window")

    label_widget = tkinter.Label(root_window)
    label_widget.configure(text="020_Rahul_Borkar")
    label_widget.pack(side=tkinter.TOP,  expand=tkinter.YES)

    button_widget = tkinter.Button(root_window)
    button_widget.configure(text="OK", command = my_handler)
    button_widget.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=tkinter.YES)

    root_window.mainloop()

main()