import tkinter as tk

root = tk.Tk()
root.option_add("*Font", "consolas 20")
root.title("I love tkinter very much")
label = tk.Label(text='Hello Pan').grid()
b1 = tk.Button(text="Click me!")
for i in range(10):
    tk.Label(root, text="hello world").grid() # Label -> widget
root.mainloop()