import sys
import tkinter


err_label = None

def copy_source_to_dest():
    global err_label
    if err_label is not None:
        err_label.destroy()
        err_label = None


    try:
        f_src = open(source_file_text_box_string.get(), "r")
        f_dest = open(dest_file_text_box_string.get(), "w")

        for line in f_src:
            print(line, file=f_dest, end='')

        f_src.close()
        f_dest.close()

    except:
        exc_name, exc_data, exc_tb = sys.exc_info()
        print("Exception name:", exc_name)
        err_msg = exc_name.__name__+":"+ str(exc_data)

        err_label = tkinter.Label(root_window)
        err_label.configure(text=err_msg)
        err_label.grid(row=3, column=1, sticky=tkinter.W)


def main():
    global dest_file_text_box_string, root_window
    global source_file_text_box_string
    root_window = tkinter.Tk()
    root_window.title("Demo SF to DF")

    label_widget = tkinter.Label(root_window)
    label_widget.configure(text="Source File")
    label_widget.grid(row=0, column=0)

    source_file_text_box_string = tkinter.StringVar()
    source_file_text_box = tkinter.Entry(root_window, textvariable=source_file_text_box_string)
    source_file_text_box.grid(row=0, column=1)


    label_widget_dest = tkinter.Label(root_window)
    label_widget_dest.configure(text="Destination File")
    label_widget_dest.grid(row=1, column=0)

    dest_file_text_box_string = tkinter.StringVar()
    dest_file_text_box = tkinter.Entry(root_window, textvariable=dest_file_text_box_string)
    dest_file_text_box.grid(row=1, column=1)

    button = tkinter.Button(root_window)
    button.configure(text="Copy", command=copy_source_to_dest)
    button.grid(row=2, column=1)

    root_window.mainloop()

main()