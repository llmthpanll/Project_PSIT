from tkinter import *
app = Tk()
app.title('Stock Income')  #ชื่อโปรแกรม
app.resizable(False, False)
app_width = 320
app_height = 568
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
mid_screen_width = int((screen_width/2)-(app_width/2))
mid_screen_height = int((screen_height/2)-(app_height/2))
#ตั้งให้โปรแกรมอยู่กลางหน้าจอ
app.geometry("%sx%s+%s+%s" %(app_width,app_height,mid_screen_width,mid_screen_height))
app.mainloop()