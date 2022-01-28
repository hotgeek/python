import time
from tkinter import *

class TimedLabel(Label):
    def __init__(self, root_window, init_text, time):
        self.L = Label(root_window, text=init_text)
        self.time = time
        self.root_window = root_window
        

    def __enter__(self):
        self.L.configure( fg='white', bg='dark green', font = ("helvetica", 20, 'underline italic'), cursor='hand2')
        self.L.pack(side=TOP, expand=YES, fill=BOTH)
        self.root_window.update()
        return self
    
    def timed_use(self):
        time.sleep(self.time)

    def __exit__(self, p1, p2, p3):
        self.L.destroy()
        return True


def main():
    root_window = Tk()
    
    with TimedLabel(root_window, "I am going to disappear soon!", 5) as tb:       
        tb.timed_use()

    root_window.mainloop()

        
    
   

main()