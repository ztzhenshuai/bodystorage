__author__ = 'freedom'
import tkinter.messagebox
from tkinter import *
class Reg (Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.lab1 = Label(frame,text = "caixukun:")
        self.lab1.grid(row = 0,column = 0,sticky = W)
        self.ent1 = Entry(frame)
        self.ent1.grid(row = 0,column = 1,sticky = W)
        self.lab2 = Label(frame,text = "nmsl:")
        self.lab2.grid(row = 1,column = 0)
        self.ent2 = Entry(frame,show = "*")
        self.ent2.grid(row = 1,column = 1,sticky = W)
        self.button = Button(frame,text = "Submit",command = self.Submit)
        self.button.grid(row = 2,column = 0,sticky =W)
        self.button3 = Button(frame,text = "Hello")
        self.button3.grid(row = 2,column = 2,sticky = W)
        self.button2 = Button(frame,text = "Quit",command = frame.quit)
        self.button2.grid(row = 2,column = 3,sticky =W)
    def Submit(self):
        s1 = self.ent1.get()
        s2 = self.ent2.get()
        if s1 == 'freedom' and s2 == '123':
            tkinter.messagebox.showinfo('hhh', 'sss')
        else:
            tkinter.messagebox.showinfo('hhhss', 'ssqqqss')
        self.ent1.delete(0,len(s1))
        self.ent2.delete(0,len(s2))


def my():
    root = Tk()
    root.title("welcome")
    app = Reg(root)
    root.mainloop()
a=1
