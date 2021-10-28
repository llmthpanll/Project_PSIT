import tkinter as tk

root = tk.Tk()
root["bg"] = "#6022f5"
#เปิดแอพตรงกลาง
root.resizable(False, False)  # This code helps to disable windows from resizing
window_height = 568
window_width = 320
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#photo = tk.PhotoImage(file="icon.png")
#ข้อความ
root.option_add("*Font", "FCHomeThin 15")
tk.Label(root, text="ใส่ตัวเลข",fg="white",bg="#6022f5").pack(pady=10)
tk.Label(root, text="ใส่ตัวเลข2",fg="white",bg="#6022f5").pack(pady=10)
root.title("Stock Income")

#ปุ่ม
btn = tk.Button(root, text="คำนวณ ").pack()

root.mainloop()