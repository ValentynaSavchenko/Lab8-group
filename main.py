from tkinter import *
from tkinter import ttk
from view import *
from tkinter import messagebox

co0 = '#ffffff'
co1 = '#000000'
co2 = '#4456F0'

window = Tk()
window.title('')
window.geometry('485x450')
window.configure(background=co0)
window.resizable(width=False, height=False)

frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co0, relief='flat')
frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NE) 

app_name = Label(frame_up, text="Phonebook", height=1, font=('Verdana 17 bold'), bg=co2, fg=co0)
app_name.place(x=5, y=5)
window.mainloop()
