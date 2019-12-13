#TD1_2CP gui
#Main idea for app is from Matthew Lewis
#Coding done by Matthew Lewis and Geoffrey Birch
#Warning for app use: This is a prototype and not medically liscensed to be used without consulting a doctor or refering to the chart giving to your doctor first !ALWAYS! double check with information from doctor before consulting this app.
import tkinter
from tkinter import *
from tkinter.messagebox import *
import time, os, json 
import io
from contextlib import redirect_stdout
# defines correction function for calculations behind insuline needed per weight and carbs intake
def cor():
    weight = weight_entry.get()
    weight_text = int(weight)
    car = car_entry.get()
    car_text = int(car)
    tdi = (int(weight_text) / 4)
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)
    current_time = current_time.replace(':', '')
    if int(current_time) >= 83000 and int(current_time) <= 103000:
        carbs = int(car_entry.get())
        ins = carbs / 40
    elif int(current_time) >= 113000 and int(current_time) <= 133000:
        carbs = int(car_entry.get())
        ins = carbs / 70               
    elif int(current_time) >= 173000 and int(current_time) <= 203000:
        carbs = int(car_entry.get())
        ins = carbs / 30
    print('You have eaten', car, 'carbs and will need ', ins.get(), 'for correction.') 
#Saves the Tk() function into variable for easy use within the code.
app = Tk()

#Weight - defines the weight label+entry box for user input
weight_label = Label(app, text='Weight', font=('bold', 14), pady=20)
weight_label.grid(row=0, column=0, sticky=W)
weight_entry = Entry(app) 
weight_entry.grid(row=0, column=1)

#car- defines the carbs label+entry box for user input
car_label = Label(app, text='Carbs', font=('bold', 14))
car_label.grid(row=0, column=2, sticky=W)
car_entry = Entry(app)
car_entry.grid(row=0, column=3)
#output box

#buttons
add_btn = Button(app, text='Calculate', width=12, command=cor)
add_btn.grid (row=2, column=0, pady=20)

#creates main window and defines name + dimensions of the gui window.
app.title('Insuline Calc')
app.geometry('700x500')

#start program
app.mainloop()
