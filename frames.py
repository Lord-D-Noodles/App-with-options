import tkinter as tk
import sys

root = tk.Tk()
root.geometry("400x400")
frame1 = tk.Frame(background="red",width=10)
frame2 = tk.Frame(background = "green",width=10)
button = tk.Button(frame1)
text = tk.Text(frame2,height=20, width=20)
frame1.pack()
frame2.pack()
button.pack()
text.pack()

#This function to to make sure the VScode fully end all processes when the x it's clicked so I don't have to do it manually
def exitApp():
    root.destroy()
    sys.exit()

#Making the clicking x run exitApp
root.protocol("WM_DELETE_WINDOW",exitApp)

tk.mainloop()