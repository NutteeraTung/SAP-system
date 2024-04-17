from tkinter import *
from tkinter import messagebox
from datetime import datetime

root=Tk()
root.title("Sap Program Inventory control")
# root.geometry("800x800+200+0")
root.config(bg="#B4DFFD")
font = ("arial",14)

#setting frame
inputFrame = Frame(root,bg="#9BBDD4")
inputFrame.pack(padx=5,pady=5)

buttonFrame = Frame(root,bg="#9BBDD4")
buttonFrame.pack(padx=5,pady=5)

#variable 
dateTime = StringVar()
ThisTime = StringVar

#def
def show_date_time():
    now = datetime.now()
    now_format = now.strftime("%d/%M/%Y")
    # print(f'{now_format =}')
    form2.insert(0,now_format)

def show_this_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)
    form3.insert(0,current_time)

#components in inputFrame 
text1 = Label(inputFrame,text="ระบบบันทึกข้อมูลเข้าคลังสินค้า (Sap System)",fg="black",font=font)
text1.grid(row=0,column=0,sticky="N",pady=5,padx=5,columnspan=6,ipadx=400)

text2 = Label(inputFrame,text="ที่ตั้งของคลังสินค้า",fg="black",font=font)
text2.grid(row=1,column=0,sticky="WE",padx=2,pady=2)

form1 = Entry(inputFrame,bg="#4F616C",font=font,fg="white")
form1.grid(row=1,column=1,sticky="WE",padx=2,pady=2)

text3 = Button(inputFrame,text="วันที่บันทึกข้อมูล",font=font,bg="#FFF98B",fg="black",command=show_date_time)
text3.grid(row=1,column=2,sticky="WE",padx=2,pady=2)

form2 = Entry(inputFrame,bg="#4F616C",width=20,font=font,fg="white")
form2.grid(row=1,column=3,sticky="WE",padx=2,pady=2)

text4 = Button(inputFrame,text="เวลาที่บันทึกข้อมูล",font=font,bg="#FFF98B",fg="black",command=show_this_time)
text4.grid(row=1,column=4,sticky="WE",padx=2,pady=2)

# text4 = Label(inputFrame,text="เวลาที่บันทึกข้อมูล",fg="black",font=font)
# text4.grid(row=1,column=4,sticky="WE",padx=2,pady=2)

form3 = Entry(inputFrame,bg="#4F616C",font=font,fg="white")
form3.grid(row=1,column=5,sticky="WE",padx=2,pady=2)

text5 = Label(inputFrame,text="หมายเลขคลัง",fg="black",font=font)
text5.grid(row=2,column=0,sticky="WE",padx=2,pady=2)

form4 = Entry(inputFrame,bg="#4F616C",font=font,fg="white")
form4.grid(row=2,column=1,sticky="WE",padx=2,pady=2)

text6 = Label(inputFrame,text="ชื่อผู้บันทึกข้อมูล",fg="black",font=font)
text6.grid(row=2,column=2,sticky="WE",padx=2,pady=2)

form5 = Entry(inputFrame,bg="#4F616C",font=font,fg="white")
form5.grid(row=2,column=3,sticky="WE",padx=2,pady=2)

text7 = Label(inputFrame,text="Lot Order",fg="black",font=font)
text7.grid(row=2,column=4,sticky="WE",padx=2,pady=2)

form6 = Entry(inputFrame,bg="#4F616C",font=font,fg="white")
form6.grid(row=2,column=5,sticky="WE",padx=2,pady=2)


#input form



root.mainloop()