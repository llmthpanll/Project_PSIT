from tkinter import *

app = Tk()
app["bg"] = "#6022f5"
app.title("Stock Income")
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



input_frame = Frame(app, bg="#6022f5")
input_frame.pack()
#จำนวนสินค้าที่ต้องการสต็อค
label1 = Label(input_frame, text="จำนวนสินค้าที่ต้องการสต็อค",fg="white",bg="#6022f5",font=18).pack(pady=10)
txt1 = StringVar()
textbox1 = Entry(input_frame, textvariable=txt1,font=18).pack()

#จำนวนสินค้าที่จะขาย
label2 = Label(input_frame, text="จำนวนสินค้าที่จะขาย",fg="white",bg="#6022f5",font=18).pack(pady=10)
txt2 = StringVar()
textbox2 = Entry(input_frame, textvariable=txt2,font=18).pack()

#ราคาสินค้าต้นทุน
label3 = Label(input_frame, text="ราคาต้นทุนสินค้า",fg="white",bg="#6022f5",font=18).pack(pady=10)
txt3 = StringVar()
textbox3 = Entry(input_frame, textvariable=txt3,font=18).pack()

#ราคาสินค้าที่ขาย
label4 = Label(input_frame, text="ราคาขายสินค้า",fg="white",bg="#6022f5",font=18).pack(pady=10)
txt4 = StringVar()
textbox4 = Entry(input_frame, textvariable=txt4,font=18).pack()

def calculation():
    price = int(txt4.get())
    amount = int(txt2.get())
    show = amount*price
    en1.insert(0, show)
#ปุ่ม
btn = Button(input_frame, text="คำนวณ",font=18, command=calculation).pack(pady=10)




#แสดงผล
output_frame = Frame(app)
output_frame.pack()
Label(output_frame, text="รายได้",fg="white",bg="#6022f5",font=18).grid(row=0,column=0)
en1 = Entry(output_frame,font=18)
en1.grid(row=0,column=1)
app.mainloop()