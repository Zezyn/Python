#!usr/bin/python

#File Name: 
#Developer: Martin Hernandez
#Date: 
#E-mail: 7607920511m.h@gmail.com
#Description: 

import tkinter

#def main():

class Telephone_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Long Distance Call App')
        self.label.pack()
        tkinter.mainloop()

TG = Telephone_GUI()

#main()
