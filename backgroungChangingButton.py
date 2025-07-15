import tkinter as Tk
import random as ran
import sys
root = Tk.Tk()
root.geometry("400x400")

#button widgets definitions
redButton = Tk.Button(text= "Red",background= "red", command =lambda: root.config(background="red"))
greenButton = Tk.Button(text= "Green",background="green", command = lambda: root.config(background="green"))
blueButton = Tk.Button(text="Blue",background="blue", command= lambda:root.config(background="blue"))
randomButton = Tk.Button(text= "Random", background="pink", command=lambda: root.config(background= randomColor()))


#button packing
redButton.pack()
greenButton.pack()
blueButton.pack()
randomButton.pack()

#funtion def
def randomColor():
    rand = ran.randint(1,10)
    if rand == 1:
        return "red"
    elif rand == 2:
        return "green"
    elif rand == 3:
        return "blue"
    elif rand == 4:
        return "gold"
    elif rand == 5:
        return "purple"
    elif rand == 6:
        return "snow"
    elif rand == 7:
        return "honeydew4"
    elif rand == 8:
        return "hot pink"
    elif rand == 9:
        return "gray4"
    elif rand == 10:
        return "maroon"

#This function to to make sure the VScode fully end all processes when the x it's clicked so I don't have to do it manually
def exitApp():
    root.destroy()
    sys.exit()

#Making the clicking x run exitApp
root.protocol("WM_DELETE_WINDOW",exitApp)


Tk.mainloop()