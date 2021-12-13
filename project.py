from pathlib import Path
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./GUI_PIC")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

app = Tk()
app.title("Stock Income")
app["bg"] = "#6022f5"
app.iconbitmap(relative_to_assets("icon.ico"))
app.resizable(False, False)
app_width = 580
app_height = 360
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
mid_screen_width = int((screen_width/2)-(app_width/2))
mid_screen_height = int((screen_height/2)-(app_height/2))
#ตั้งให้โปรแกรมอยู่กลางหน้าจอ
app.geometry("%sx%s+%s+%s" %(app_width,app_height,mid_screen_width,mid_screen_height))

canvas = Canvas(app,bg = "#6022f5",height = 360,width = 580,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)


#text กล่องใส่ราคาสินค้าที่ขาย
canvas.create_text(69.0,81.0,anchor="nw",text="ราคาสินค้าที่ขาย",fill="#FFFFFF",font=("FCHomeRegular", 12 * -1))
entry_image_1 = PhotoImage(file=relative_to_assets("bg_entry.png"))
input_price = StringVar()
entry_bg_1 = canvas.create_image(168.0,110.0,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=input_price)
entry_1.place(x=82.0,y=100.0,width=172.0,height=18.0)

#text กล่องใส่ราคาสินค้าต้นทุน
canvas.create_text(69.0,133.0,anchor="nw",text="ราคาสินค้าต้นทุน",fill="#FFFFFF",font=("FCHomeRegular", 12 * -1))
entry_image_2 = PhotoImage(file=relative_to_assets("bg_entry.png"))
input_buy = StringVar()
entry_bg_2 = canvas.create_image(168.0,162.0,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=input_buy)
entry_2.place(x=82.0,y=152.0,width=172.0,height=18.0)

#text กล่องใส่จำนวนสินค้าที่ขายได้
canvas.create_text(69.0,184.0,anchor="nw",text="จำนวนสินค้าที่ขายได้",fill="#FFFFFF",font=("FCHomeRegular", 12 * -1))
entry_image_3 = PhotoImage(file=relative_to_assets("bg_entry.png"))
input_amount = StringVar()
entry_bg_3 = canvas.create_image(168.0,213.0,image=entry_image_3)
entry_3 = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=input_amount)
entry_3.place(x=82.0,y=203.0,width=172.0,height=18.0)

#text กล่องใส่จำนวนสินค้าที่ต้องการจะสต็อค
canvas.create_text(69.0,235.0,anchor="nw",text="จำนวนสินค้าที่ต้องการจะสต็อค",fill="#FFFFFF",font=("FCHomeRegular", 12 * -1))
entry_image_4 = PhotoImage(file=relative_to_assets("bg_entry.png"))
input_stock = StringVar()
entry_bg_4 = canvas.create_image(168.0,264.0,image=entry_image_4)
entry_4 = Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=input_stock)
entry_4.place(x=82.0,y=254.0,width=172.0,height=18.0)



#แสดงผลรายรับ
canvas.create_text(343.0,108.0,anchor="nw",text="รายรับ",fill="#FFFFFF",font=("FCHomeRegular", 12 * -1))
entry_image_5 = PhotoImage(file=relative_to_assets("bg_entry.png"))
entry_bg_5 = canvas.create_image(441.5,136.5,image=entry_image_5)
entry_5 = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
entry_5.place(x=358.0,y=127.0,width=167.0,height=18.0)

#แสดงผลรายจ่าย
canvas.create_text(343.0,159.0,anchor="nw",text="รายจ่าย",fill="#FFFFFF",font=("FCHomeRegular", 12 * -1))
entry_image_6 = PhotoImage(file=relative_to_assets("bg_entry.png"))
entry_bg_6 = canvas.create_image(441.5,187.5,image=entry_image_6)
entry_6 = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
entry_6.place(x=358.0,y=178.0,width=167.0,height=18.0)

#แสดงผลกำไร
canvas.create_text(343.0,210.0,anchor="nw",text="กำไร",fill="#FFFFFF",font=("FCHomeRegular", 12 * -1))
entry_image_7 = PhotoImage(file=relative_to_assets("bg_entry.png"))
entry_bg_7 = canvas.create_image(441.5,237.5,image=entry_image_7)
entry_7 = Entry(bd=0,bg="#FFFFFF",highlightthickness=0)
entry_7.place(x=358.0,y=229.0,width=167.0,height=18.0)

#แสดงเส้นแบ่งครึ่ง
image_image_2 = PhotoImage(file=relative_to_assets("center_line.png"))
image_2 = canvas.create_image(305.0,187.0,image=image_image_2)

#แสดงหน้า welcome
image_image_3 = PhotoImage(file=relative_to_assets("welcome.png"))
image_3 = canvas.create_image(15.0,180.0,image=image_image_3)

#แสดงโล้โก้แบบเต็ม
image_image_4 = PhotoImage(file=relative_to_assets("full_icon.png"))
image_4 = canvas.create_image(305.0,38.0,image=image_image_4)

#แสดงกล่องกลมสีขาว
image_image_5 = PhotoImage(file=relative_to_assets("all_entry.png"))
image_5 = canvas.create_image(305.0,187.0,image=image_image_5)

#แสดง version program
canvas.create_text(550.0,341.0,anchor="nw",text="V 1.1.1",fill="#FFFFFF",font=("BigNoodleTitling Oblique", 12 * -1))

def caculation():
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    price = int(input_price.get())
    buy = int(input_buy.get())
    amount = int(input_amount.get())
    stock = int(input_stock.get())
    income = price*amount
    expenses = stock*buy
    profit =  income - expenses
    entry_5.insert(0, income)
    entry_6.insert(0, expenses)
    entry_7.insert(0, profit)

button_image_1 = PhotoImage(file=relative_to_assets("button.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=caculation,relief="flat")
button_1.place(x=263.0,y=299.0,width=85.0,height=26.0)

app.mainloop()