from tkinter import *

class MyButton:
    def __init__(self, window, btn_text):
        self.button = Button(window, text=btn_text) 
       
    def grid(self, input_row:int, input_column: int):
        self.button.grid(row=input_row, column=input_column)

def main():
    root_window = Tk()

    btn1 = MyButton(root_window, "Rahul's Button")
    btn1.grid(0, 0)

    root_window.mainloop()

main()