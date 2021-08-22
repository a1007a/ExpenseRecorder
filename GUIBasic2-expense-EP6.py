from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย A')
GUI.geometry('600x700+500+50')

 #B1 = Button(GUI,text='Hello')
 #B1.pack(ipadx=50,ipady=20)

####Menu######

menubar=Menu(GUI)
GUI.config(menu=menubar)
#file menu
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

def About():
    messagebox.showinfo('About','สวัสดีครับนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจาคเราไหม? ขอ 1 BTC ก็พอแล้ว\nBTC Adress:abc')


helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

donatemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)



Tab = ttk.Notebook(GUI)
T1=Frame(Tab)
T2=Frame(Tab)
Tab.pack(fill=BOTH,expand=1)
#T1=Frame(Tab,width=400,hight=400)
#T2=Frame(Tab,width=400)

icon_t1 = PhotoImage(file='t1_expense.png')
icon_t2 = PhotoImage(file='t2_expenselist.png')

Tab.add(T1,text=f'{"เพิ่มค่าใช้จ่าย":^{30}}',image=icon_t1,compound='left')
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')




F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()

days = {'Mon':'จันทร์',
       'Tue':'อังคาร',
       'Wed':'พุธ',
       'Thu':'พฤหัสบดี',
       'Fri':'ศุกร์',
       'Sat':'เสาร์',
       'Sun':'อาทิตย์'}
def Save(even=None) :
    expense = v_expense.get()
    price = v_price.get()
    quantity=v_quantity.get()
    if expense=='': # or price =='' or quantity =='':
        print('No Data')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
        return
    elif price =='':
        messagebox.showwarning('Error','กรุณากรอกราคา')
        return
    elif quantity =='':
        messagebox.showwarning('Error','กรุณากรอกจำนวน')
        return
    total=float(price)*float(quantity)
    try:
        total=float(price)*float(quantity)
        print('รายการ: {} ราคา: {}'.format (expense,price))
        print('จำนวน:{} รวมทั้งหมด:{}บาท'.format(quantity,total))
        text='รายการ: {} ราคา: {}\n'.format (expense,price)
        text=text + 'จำนวน:{} รวมทั้งหมด:{}บาท'.format(quantity,total)
        v_result.set(text)
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

        today = datetime.now().strftime('%a')
        print(today)
        dt = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        dt = days[today] + '-' + dt
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
            fw = csv.writer(f)
            data = [dt,expense,price,quantity,total]
            fw.writerow(data)
        E1.focus()
        update_table()
    except Exception as e:
        print('ERROR:',e)   
        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')  
        #messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        #messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
GUI.bind('<Return>',Save)    
    
FONT1 = (None,20)


main_icon=PhotoImage(file='icon_money.png')
Mainicon=Label(F1,image=main_icon)
Mainicon.pack()
L = ttk.Label(F1,text='รายการาค่าใช้จ่าย' ,font=FONT1) .pack()
v_expense = StringVar()
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()

L = ttk.Label(F1,text='ราคา (บาท)' ,font=FONT1) .pack()
v_price = StringVar()
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()

L = ttk.Label(F1,text='จำนวน (ชิ้น)' ,font=FONT1) .pack()
v_quantity = StringVar()
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()    
icon_b1=PhotoImage(file='b_save.png')

B2 = ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_result=StringVar()
v_result.set('--------ผลลัพธ์---------')
result=ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='blue')
result.pack(pady=20)



#########################################


def read_csv():
    #global rs
    with open('savedata.csv',newline='',encoding='utf-8')as f:
        fr=csv.reader(f)
        data=list(fr)
        #rs=data
        # print(rs)
    return data
        # print(data)
        # print('.......')
        # print(data[0][0])
        # for a,b,c,d,e in data:
        #     print(e)
#table

L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด' ,font=FONT1) .pack(pady=20)


header=['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable=ttk.Treeview(T2,columns=header,show='headings',height=20)
resulttable.pack()

# for i in ragne(len(header)):
#     resulttable.heading(header[i],text=header[i])
for h in header:
    resulttable.heading(h,text=h)

headerwidth=[150,170,80,80,80]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)
#resulttable.column('วัน-เวลา'width=10)
# resulttable.heading(header[0],text=header[0])

# resulttable.insert('','end',value=['จันทร์','น้ำดื่ม',30,5,150])
# resulttable.insert('','end',value=['จันทร์','น้ำดื่ม',30,5,150])



def update_table():
    resulttable.delete(*resulttable.get_children())
    # for c in resulttable.get_children():
    #     resulttable.delete(c)

    data=read_csv()
    for d in data:
        resulttable.insert('',0,value=d)

update_table()
print('GET CHILD:',resulttable.get_children())


    #f=open('savedata.csv',newline='',encoding='utf-8')
    #fr=csv.reader(f)
    #f.close() ใช้ with open แทน ป้องกันลืมปิดไฟล์


#GUI.bind('<Tab>',Lambda x: E2.focus())

GUI.mainloop()
