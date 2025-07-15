import tkinter as Tk
import sys
root = Tk.Tk()
root.geometry("400x400")
box = Tk.Entry(text="Type what you want")
box.pack()


def printFromTextBox(Event):
    print(box.get())
    box.delete(0,"end")

#This function to to make sure the VScode fully end all processes when the x it's clicked so I don't have to do it manually
def exitApp():
    root.destroy()
    sys.exit()

#Making the clicking x run exitApp
root.protocol("WM_DELETE_WINDOW",exitApp)


box.bind("<Return>", lambda e: printFromTextBox(e))

Tk.mainloop()