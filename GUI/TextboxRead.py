from tkinter import *

def read_box():
    print(text_box_string)

def main():
    global text_box_string
    root_window = Tk()
    root_window.title("Entry widget demo")
    text_box_string = StringVar()
    h_text_box = Entry(root_window, textvariable=text_box_string)

    hbutton = Button(root_window)
    hbutton.configure(text="Submit", command=read_box)

    h_text_box.grid(row=0, column=1)
    hbutton.grid(row=1, column=1)

    root_window.mainloop()

main()