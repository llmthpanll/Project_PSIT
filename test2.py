import tkinter as tk
def print_something():
    print("txt")
    tk.Label(text='confuse').pack()
app = tk.Tk()
app.title('Hello world')
e1 = tk.Entry()
e1.pack()
button = tk.Button(text='click me!', command=print_something).pack()
tk.Button(text='Looo').pack()
app.mainloop()