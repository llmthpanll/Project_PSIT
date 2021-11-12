import tkinter as tk

app = tk.Tk()
app["bg"] = "#6022f5"
#กำหนดขนาดโปรแกรม
app.resizable(False, False)
app_width = 320
app_height = 568
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
mid_screen_width = int((screen_width/2)-(app_width/2))
mid_screen_height = int((screen_height/2)-(app_height/2))
#ตั้งให้โปรแกรมอยู่กลางหน้าจอ
app.geometry("%sx%s+%s+%s" %(app_width,app_height,mid_screen_width,mid_screen_height))

#ข้อความ
app.option_add("*Font", "FCHomeThin 14")
tk.Label(app, text="ใส่ตัวเลข",fg="white",bg="#6022f5").pack(pady=10)
tk.Label(app, text="ใส่ตัวเลข2",fg="white",bg="#6022f5").pack(pady=10)
app.title("Stock Income")

#ปุ่ม
btn = tk.Button(app, text="คำนวณ ").pack()

app.mainloop()