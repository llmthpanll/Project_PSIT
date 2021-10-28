import tkinter as tk
def print_something(txt):
        print(txt)
        tk.Label(text='confuse').pack()
app = tk.Tk()
app.title('Hello world')
e1 = tk.Entry()
e1.pack()
button = tk.Button(text='click me!', command=print_something(e1)).pack()
tk.Button(text='Looo').pack()
app.mainloop()