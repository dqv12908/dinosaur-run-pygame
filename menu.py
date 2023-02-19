from tkinter import *

win = Tk()
win.geometry("500x500")
win.title("dinosaur game by Vinh")

def play():
    win.destroy()
    import basic

def quit():
    win.destroy()

h1=Label(win,text="Dinosaur game",font=("Arial",30,"bold")).pack(pady=30)
playbtn = Button(win,text="PLAY",font=("Arial",20,"bold"),command=play).pack(pady=30)
quitbtn = Button(win,text="QUIT",font=("Arial",20,"bold"),command=quit).pack(pady=30)

win.mainloop()