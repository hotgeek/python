import sys
import time
import tkinter

def wrapper_to_time():
    print_time(time.time())

def print_time(timestamp):
    print("time is--- ", timestamp)

def print_platform():
    print("Platform is--- ", sys.platform)

def main():
    root_window = tkinter.Tk()
    root_window.title("Button handler program")

    button1 = tkinter.Button(root_window)
    button1.configure(text="Time", command=wrapper_to_time)
    button1.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X)

    button2 = tkinter.Button(root_window)
    button2.configure(text="Platform", command=print_platform)
    button2.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)

    button3 = tkinter.Button(root_window)
    button3.configure(text="Exit", command=sys.exit)
    button3.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X)

    root_window.mainloop()

main()