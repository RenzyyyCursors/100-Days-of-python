from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Kilometer to Miles")
window.minsize(width=100, height=200)
window.config(padx=40,pady=80)

entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
entry.grid(row=0,column=1)

def action():
    miles = entry.get()
    miles_str = str(round(float(miles)*1.60934,2)) + "     Miles"
    label2 = Label(text=miles_str)
    label2.grid(row=1,column=1)

button = Button(text="Convert", command=action)
button.grid(row=2,column=1)

label1 = Label(text="is equal to")
label1.grid(row=1,column=0)

label3 = Label(text="Kilometers")
label3.grid(row=1,column=2)


window.mainloop()