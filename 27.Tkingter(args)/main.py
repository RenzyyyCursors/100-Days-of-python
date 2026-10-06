import tkinter as tk

window = tk.Tk()
window.title("Gui")
window.minsize(width=500,height=300)

my_label = tk.Label(text='Im a label',font=('Arial',20,'bold'))
my_label.config(text = 'New Text')
my_label.pack()

def button_clicked():
    # my_label.config(text=entered)
    my_label.config(text= input.get())

button = tk.Button(text='Click Me',command=button_clicked)
button.pack()

input = tk.Entry(width=15)
input.pack()







window.mainloop()