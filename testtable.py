from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd



#ตั้งค่าหน้าจอสำหรับแสดงผล
root = Tk()
root.title("Table form")
root.config(bg='#D2E8D2')
root.geometry('800x700+250+50')
root.iconbitmap('../sap asset/material-management.ico')
font2 = ('Cordia New (Body CS)', 12)

#สร้าง Frame
tableframe = Frame(root)
tableframe.pack(pady=10)
butFrame = Frame(root)
butFrame.pack(pady=10)
textFrame = Frame(root,background='#D2E8D2')
textFrame.pack()

#สร้างหัวข้อ
Label(tableframe,text="ระบบบันทึกข้อมูลลงสินค้าคงคลัง",font=('FreesiaUPC', 18)).pack(padx=5,pady=5)

#ตั้งค่าตาราง
my_table = ttk.Treeview(tableframe)
my_table.pack(ipadx=60)
style = ttk.Style()
style.configure("Treeview.Heading", font=('FreesiaUPC', 16))

#สร้าง column ของตาราง
# Defining headings, other option is tree
my_table['columns'] = ('บาร์โค้ด','ขนาด','รสชาติ','จำนวนที่ผลิต','ราคา/ลัง','ราคาขาย')
my_table['show'] = 'tree'
my_table.column("#0", width=0,  stretch=NO)
my_table.column("บาร์โค้ด",anchor=CENTER,width=100)
my_table.column("ขนาด",anchor=CENTER,width=100)
my_table.column("รสชาติ",anchor=CENTER,width=100)
my_table.column("จำนวนที่ผลิต",anchor=CENTER,width=100)
my_table.column("ราคา/ลัง",anchor=CENTER,width=100)
my_table.column("ราคาขาย",anchor=CENTER,width=100)

#สร้าง heading ในตาราง
my_table.heading("#0",text="",anchor=CENTER)
my_table.heading("บาร์โค้ด",text="บาร์โค้ด",anchor=CENTER)
my_table.heading("ขนาด",text="ขนาด",anchor=CENTER)
my_table.heading("รสชาติ",text="รสชาติ",anchor=CENTER)
my_table.heading("จำนวนที่ผลิต",text="จำนวนที่ผลิต",anchor=CENTER)
my_table.heading("ราคา/ลัง",text="ราคา/ลัง",anchor=CENTER)
my_table.heading("ราคาขาย",text="ราคาขาย",anchor=CENTER)

#ประกาศตัวแปร
barcodeNum = StringVar() #บาร์โค้ด
choice = StringVar() #ขนาด
flavorite = StringVar() #รสชาติ
productNumber = StringVar() #จำนวนผลิต
sellUnit = IntVar() #ราคาต่อลัง
sellprice = IntVar() #ราคาขาย

#ประกาศฟังก์ชัน
def ShowPrice(): #รับค่าราคาต่อหน่วย
    unit.delete(0,END)
    sellProduct.delete(0,END)
    global a,b,c
    
    a = choice.get()
    b = flavorite.get()
    c = productNumber.get()
    
    if a == '600ml':
        if b == 'ชาเขียว':
            if c =="" : #มี  a b ไม่มี d
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ") #กรอก a,b, ไม่กรอก c
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                sellUnit = 60
                sellprice = int(c) * sellUnit
                unit.insert(INSERT,sellUnit)
                sellProduct.insert(INSERT,sellprice)
        elif b == 'ชาไทย':
            if c =="" : #มี  a b ไม่มี d
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ") #กรอก a,b, ไม่กรอก c
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                sellUnit= 65
                sellprice = int(c) * sellUnit
                unit.insert(INSERT,sellUnit)
                sellProduct.insert(INSERT,sellprice)
        elif b == 'นมเย็น':
            if c =="" : #มี  a b ไม่มี d
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ") #กรอก a,b, ไม่กรอก c
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                sellUnit= 55
                sellprice = int(c) * sellUnit
                unit.insert(INSERT,sellUnit)
                sellProduct.insert(INSERT,sellprice)
        elif b == "": #มี a ไม่มี b
            if c == "":
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
                unit.delete(0,END)
                sellProduct.delete(0,END)
            
            
    elif a == '1500ml':
        if b == 'ชาเขียว':
            if c =="" : 
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ") #กรอก a,b, ไม่กรอก c
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                sellUnit= 90
                sellprice = int(c) * sellUnit
                unit.insert(INSERT,sellUnit)
                sellProduct.insert(INSERT,sellprice)
        elif b == 'ชาไทย':
            if c =="" : 
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ") #กรอก a,b, ไม่กรอก c
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                sellUnit= 95
                sellprice = int(c) * sellUnit
                unit.insert(INSERT,sellUnit)
                sellProduct.insert(INSERT,sellprice) 
        elif b == 'นมเย็น':
            if c =="" : 
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ") #กรอก a,b, ไม่กรอก c
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                sellUnit= 85
                sellprice = int(c) * sellUnit
                unit.insert(INSERT,sellUnit)
                sellProduct.insert(INSERT,sellprice)
        elif b == "":
            if c == "":
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
                unit.delete(0,END)
                sellProduct.delete(0,END)
            else:
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
                unit.delete(0,END)
                sellProduct.delete(0,END)
                
    elif a =="": #ไม่มี a b d
        if b == "":
            if c =="":
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
                unit.delete(0,END)
                sellProduct.delete(0,END)
    else:
        pass
    
    if c == 0: #กรอก c ผิด (ติดลบ)
        messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
        unit.delete(0,END)
        sellProduct.delete(0,END)
    else: 
        if a == "":
            messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
            unit.delete(0,END)
            sellProduct.delete(0,END)
        else:
            if b == "":
                messagebox.showwarning("การกรอกข้อมูลผิดพลาด" , "กรุณากดปุ่มย้อนกลับ")
                unit.delete(0,END)
                sellProduct.delete(0,END)
            
def undo_but():
    unit.config(state="normal")
    sellProduct.config(state="normal")
    barcode.delete(0,END)
    production.delete(0,END)
    unit.delete(0,END)
    sellProduct.delete(0,END)
    size.set('')
    flavor.set('')
     
def add_data():
    get_barcode = barcodeNum.get() #อ่าน barcode
    get_choice = choice.get() #อ่านขนาด
    get_flavor = flavorite.get() #อ่านรสชาติ
    get_product = productNumber.get() #อ่านจำนวนที่ผลิต
    get_sellunit = sellUnit.get() #อ่านราคาต่อลัง
    get_sellproce = sellprice.get() #อ่านราคาขาย
    my_table.insert("",'end',
                    values=(get_barcode,get_choice,get_flavor,get_product,get_sellunit,get_sellproce))
    #reset
    unit.config(state="normal")
    sellProduct.config(state="normal")
    barcode.delete(0,END)
    production.delete(0,END)
    unit.delete(0,END)
    sellProduct.delete(0,END)
    size.set('')
    flavor.set('')
    
def remove_item():
    selected_items = my_table.selection()        
    for selected_item in selected_items:          
        my_table.delete(selected_item)
    
def edit_item():
    print("edit")
    #คลิกแถว
    #ข้อมูลเด้งกลับไปที่ฟอร์ม
    #เซฟทับ
    
def exportexcel():
    excelwriter = pd.ExcelWriter('./database.xlsx')
    df.to_excel(excelwriter,sheet_name="Analysis")
    excelwriter.save()
    excelwriter.close()
            
#input data
i= 1234
my_table.insert("",'end',
    values=(i,'-','-',0,0,0)) #dummy data @start

adddata = Label(butFrame, text='สำหรับกรอกข้อมูล',font=('Cordia New (Body CS)', 16),anchor=CENTER) 
adddata.grid(row=0,column=2,columnspan=2,pady=5,sticky=N)

barcodeLabel = Label(butFrame,text='กรอกบาร์โค้ด',font=font2)
barcodeLabel.grid(row=1,column=0,padx=5)
barcode = Entry(butFrame,width=8,textvariable=barcodeNum,font=font2) 
barcode.grid(row=1,column=1,padx=5)

sizelabel = Label(butFrame,text="ขนาด",font=font2)
sizelabel.grid(row=1,column=2,padx=5)
size = ttk.Combobox(butFrame,textvariable=choice,font=font2,width=10)
size['values'] = ['600ml','1500ml']
size.grid(row=1,column=3,padx=5)

flavorlabel = Label(butFrame,text="รสชาติ",font=font2)
flavorlabel.grid(row=1,column=4,padx=5)
flavor = ttk.Combobox(butFrame,textvariable=flavorite,font=font2,width=10)
flavor['values'] = ['ชาเขียว','ชาไทย','นมเย็น']
flavor.grid(row=1,column=5,padx=5)

productionLabel = Label(butFrame,text="จำนวนที่ผลิต(ลัง)",font=font2)
productionLabel.grid(row=2,column=0,padx=5,pady=5)
production = Entry(butFrame,font=font2,textvariable=productNumber,width=8)
production.grid(row=2,column=1,padx=5,pady=5)

unitLabel = Label(butFrame,text="ราคา/ลัง",font=font2)
unitLabel.grid(row=2,column=2,padx=5,pady=5)
unit = Entry(butFrame,font=font2,textvariable=sellUnit,width=8)
unit.grid(row=2,column=3,padx=5,pady=5)

sellLabe = Label(butFrame,text="ราคาขาย",font=font2)
sellLabe.grid(row=2,column=4,padx=5,pady=5)
sellProduct = Entry(butFrame,textvariable=sellprice,width=8,font=font2) 
sellProduct.grid(row=2,column=5,padx=5,pady=5)

bathbut = Button(butFrame,text='฿',font=font2,bg="#e1ecf4",command=ShowPrice)
bathbut.grid(row=2,column=6,padx=5,pady=5)

undoBut= Button(butFrame,text='ย้อนกลับ',font=font2,bg="#98d9ff",width=10,command=undo_but)
undoBut.grid(row=3,column=1,padx=5,pady=5)

editbut = Button(butFrame,text='แก้ไข',font=font2,bg="#8C95BD",width=10,command=edit_item)
editbut.grid(row=3,column=2,padx=5,pady=5)

delbut = Button(butFrame,text='ลบ',font=font2,bg="#ff6f69",width=10,command=remove_item)
delbut.grid(row=3,column=3,padx=5,pady=5)

addPrice = Button(butFrame,text='เพิ่มข้อมูล',font=font2,bg="#a9d295",width=10,command=add_data)
addPrice.grid(row=3,column=4,padx=5,pady=5)

savebut = Button(butFrame,text='บันทึกข้อมูล',font=font2,bg="#f3cc64",width=10,command=exportexcel)
savebut.grid(row=4,column=2,columnspan=2,padx=5,pady=10)

copyRight = Label(textFrame,text = "©ระบบบันทึกสินค้าคงคลังนี้เป็นลิขสิทธิ์ของผู้จัดทำเท่านั้น ห้ามนำไปทำซ้ำหรือดัดแปลงเพื่อนำไปเผยแพร่ต่อหรือขายต่อ",font=('TH SarabunPSK',10),background='#D2E8D2',fg="red")
copyRight.grid(sticky=E,pady=50)

#create data frame
df = pd.DataFrame(my_table,columns=['#0','บาร์โค้ด','ขนาด','รสชาติ','จำนวนที่ผลิต','ราคา/ลัง','ราคาขาย'])
f = open("./database.xlsx",'r')
file_contents = f.read()

root.mainloop()