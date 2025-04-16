import customtkinter
from tkcalendar import DateEntry
from PIL import Image
from sqlalchemy.orm import Session
import datetime
from sql_app.database import engine
from sql_app.crud import *
import tkinter as tk
from .floatspinbox import FloatSpinbox,sum_Frame
import os
from typing import Union
from typing import Callable
class edit_order(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
        self.edit_top_=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(7):
            self.edit_top_.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.edit_top_, text="電話",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.phone=customtkinter.CTkEntry(self.edit_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.edit_top_, text="通路",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path=customtkinter.CTkComboBox(self.edit_top_,values=["","現場", "網站"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.edit_top_, text="取貨方式",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up=customtkinter.CTkComboBox(self.edit_top_,values=["","現場", "宅配"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.edit_top_, text="日期",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.date_=DateEntry(self.edit_top_,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 18, 'bold'))
        self.date_1=DateEntry(self.edit_top_,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 18, 'bold'))
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.set_date('2000-01-01')
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.date_1.grid(row=1,column=3,padx=30,pady=5)
        self.money_label=customtkinter.CTkLabel(self.edit_top_, text="金額",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.money=customtkinter.CTkEntry(self.edit_top_, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.money2=customtkinter.CTkEntry(self.edit_top_, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.money.insert(customtkinter.END,0)
        self.money2.insert(customtkinter.END,99999)
        self.money_label.grid(row=0,column=4,padx=30,pady=5)
        self.money.grid(row=0,column=5,padx=30,pady=5)
        self.money2.grid(row=1,column=5,padx=30,pady=5)
        reset_bt=customtkinter.CTkButton(self.edit_top_,text='重新設定', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.reset_
                                                        )
        reset_bt.grid(row=0,column=6,padx=30,pady=5)
        search=customtkinter.CTkButton(self.edit_top_,text='確定查詢', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        command=lambda: self.search_od_list(phone=self.phone.get(),pick_up=self.pick_up.get(),date_=self.date_.get_date(),date_1=self.date_1.get_date(),money1=self.money.get(),money2=self.money2.get(),path=self.path.get()))
        search.grid(row=1,column=6,padx=30,pady=5)  
     
        self.edit_top_.pack(fill='x',padx=30,pady=5)
        self.ol=order_List(self,phone='',path='',pick_up='',date_='2000-01-01',date_1=datetime.datetime.today(),money1='0',money2='999999',page=1,fg_color = ("#DDDDDD"))
        self.ol.pack(fill='both',expand=1,padx=30,pady=5)
        self.page_=FloatSpinbox123(self)
        self.page_.pack(pady=20,side='bottom')
        max_p1=max_p(db=Session(engine),phone='',path='',pick_up='',date_='2000-01-01',date_1=datetime.datetime.today(),money1='0',money2='999999')
        self.page_.page_max.configure(text=f'/{max_p1//20+1}')
        def page_search(event):
            
            self.search_od_list(phone=self.phone.get(),pick_up=self.pick_up.get(),date_=self.date_.get_date(),date_1=self.date_1.get_date(),money1=self.money.get(),money2=self.money2.get(),path=self.path.get(),page=1 if self.page_.get()==None else self.page_.get())
        self.page_.add_button.bind("<Button-1>", page_search)
        self.page_.subtract_button.bind("<Button-1>", page_search)
        self.page_.entry.bind('<Return>',page_search)
    def search_od_list(self,phone,path,pick_up,date_,date_1,money1,money2,page=1):
        self.ol.pack_forget()
        self.ol.destroy()
        max_p1=max_p(db=Session(engine),phone=phone,path=path,pick_up=pick_up,date_=date_,date_1=date_1,money1=money1,money2=money2)
        self.page_.page_max.configure(text=f'/{max_p1//20+1}')
        self.ol=order_List(self,phone=phone,path=path,pick_up=pick_up,date_=date_,date_1=date_1,money1=money1,money2=money2,page=page,fg_color = ("#DDDDDD"))
        self.ol.pack(fill='both',expand=1,padx=30,pady=5)
    def reset_(self):
        self.phone.delete(0,customtkinter.END)
        self.path.set('')
        self.pick_up.set('')
        self.date_.set_date('2000-01-01')
        self.date_1.set_date(datetime.datetime.today())
        self.money.delete(0,customtkinter.END)
        self.money2.delete(0,customtkinter.END)
        self.money.insert(customtkinter.END,0)
        self.money2.insert(customtkinter.END,99999)
class order_List(customtkinter.CTkFrame):
    def __init__(self, master,phone,path,pick_up,date_,date_1,money1,money2,page, **kwargs):
        super().__init__(master, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  size=(30, 30))
        self.info = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\information-button.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\information-button.png"),
                                  size=(30, 30))
        self.edit_photo = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\pencil.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\pencil.png"),
                                  size=(30, 30))
        self.delete_photo = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\close.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\close.png"),
                                  size=(30, 30))        
        self.od_l={}
        self.phone=phone
        self.pick_up=pick_up
        self.path=path
        self.date_=date_
        self.date_1=date_1
        self.money1=money1
        self.money2=money2
        self.page=page
        self.c=customtkinter.CTkScrollableFrame(self,fg_color = ("#DDDDDD"))
        # self.c.pack(fill='both',expand=1)
        self.search()
        self.toplevel_window = None
    # 取得訂單訊息
    def search(self):
        self.c.pack_forget()
        self.c.destroy()
        try:
            self.od_l={}
            order_list=search_od_(db=Session(engine),path=self.path,phone=self.phone,pick_up=self.pick_up,date_=self.date_,date_1=self.date_1,money1=self.money1,money2=self.money2,page=self.page)
            for i in order_list:
                if f'{i.order_number}{i.M_ID}' in self.od_l:
                    self.od_l[f'{i.order_number}{i.M_ID}'][4]+=f',{i.p_ID_.product_Name}'
                    # self.od_l[f'{i.order_number}{i.M_ID}'][6]+=i.count*i.p_ID_.product_Price
                else:
                    self.od_l[f'{i.order_number}{i.M_ID}']=[i.M_ID_.Phone,i.od_id,i.pick_up_date,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.total,i.M_ID,i.order_number]
        except Exception as e:
            print(e)
            self.od_l={}
        self.c=customtkinter.CTkScrollableFrame(self,fg_color = ("#DDDDDD"))
        for i in range(10):
            self.c.columnconfigure(i,weight=1)
        self.c.columnconfigure(4,weight=2)
        a=customtkinter.CTkLabel(self.c,text='會員資訊',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=0)
        a=customtkinter.CTkLabel(self.c,text='訂單資訊',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=1)
        a=customtkinter.CTkLabel(self.c,text='取貨日期',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=2) 
        a=customtkinter.CTkLabel(self.c,text='取貨方式',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=3) 
        a=customtkinter.CTkLabel(self.c,text='訂單項目',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=4)
        a=customtkinter.CTkLabel(self.c,text='是否取貨',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=5)
        a=customtkinter.CTkLabel(self.c,text='金額',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=6)
        a=customtkinter.CTkLabel(self.c,text='編輯',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=7)
        a=customtkinter.CTkLabel(self.c,text='拆單',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=8)
        a=customtkinter.CTkLabel(self.c,text='刪除',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=9)
        
        i=1
        def split_bill(i,l):return lambda:self.split_bill_(i,l)
        def gen_cmd1(i,l):return lambda:self.edit_(i,l)
        def gen_cmd(i,l):return lambda:self.delete(i,l)
        def get_user(i):return lambda:self.get_u(i)
        def get_od_(i):return lambda:self.get_o(i)
        for key,value in self.od_l.items():
            a=customtkinter.CTkButton(self.c,width=30,image=self.image,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_user(value[0]))#電話
            a.grid(row=i,column=0)
            a=customtkinter.CTkButton(self.c,width=30,image=self.info,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_od_(value[1]))#訂單
            a.grid(row=i,column=1)
            a=customtkinter.CTkLabel(self.c,text=f'{value[2]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=2) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[3]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=3) 
            b=customtkinter.CTkScrollableFrame(self.c,orientation='horizontal',height=20)
            a=customtkinter.CTkLabel(b,text=f'{value[4]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.pack(side='left')
            b.grid(row=i,column=4,sticky='ew')
            a=customtkinter.CTkLabel(self.c,text=f'{value[5]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=5)
            a=customtkinter.CTkLabel(self.c,text=f'{value[6]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=6)
            a=customtkinter.CTkButton(self.c,width=30,image=self.edit_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd1(value[-1],value[0]))
            a.grid(row=i,column=7)
            a=customtkinter.CTkButton(self.c,width=30,image=self.edit_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=split_bill(value[-1],value[0]))
            a.grid(row=i,column=8)
            a=customtkinter.CTkButton(self.c,width=30,image=self.delete_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd(value[-1],value[-2]))#訂單號碼,ID
            a.grid(row=i,column=9)
            i+=1
        self.c.pack(fill='both',expand=1)
        self.toplevel_window = None
    def get_o(self,i):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = info_ToplevelWindow(self,od=i)  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    # 取得廠商訊息
    def get_u(self,i):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = profile_ToplevelWindow(self,phone=i)  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def split_bill_(self,i,l):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = split_bill_ToplevelWindow(self,key=i,M_Name=l)
            self.toplevel_window.sum_frame_.confirm_bt.configure(command=self.spilt_od)             
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def spilt_od(self):
        try:
            spilt_bill_add(db=Session(engine),phone=self.toplevel_window.phone.get(),path=self.toplevel_window.path.get(),Pick_up=self.toplevel_window.pick_up.get(),remark=self.toplevel_window.Remark_textbox.get(1.0,'end'),product_=self.toplevel_window.buy_list,date_=self.toplevel_window.date_.get_date(),key=self.toplevel_window.key,M_name=self.toplevel_window.M_Name,discount=0 if self.toplevel_window.sum_frame_.discount_entry.get()=='' else self.toplevel_window.sum_frame_.discount_entry.get())
            self.toplevel_window.destroy()
            self.search()  
            tk.messagebox.showinfo(title='修改成功', message="修改成功", )
        except:
            tk.messagebox.showinfo(title='修改失敗', message="修改失敗", )
           
    def edit_(self,i,l):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = edit_ToplevelWindow(self,key=i,M_Name=l)
            self.toplevel_window.sum_frame_.confirm_bt.configure(command=self.edit_od)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def edit_od(self):
        try:
            edit_order_(db=Session(engine),phone=self.toplevel_window.phone.get(),path=self.toplevel_window.path.get(),Pick_up=self.toplevel_window.pick_up.get(),remark=self.toplevel_window.Remark_textbox.get(1.0,'end'),product_=self.toplevel_window.buy_list,date_=self.toplevel_window.date_.get_date(),key=self.toplevel_window.key,M_name=self.toplevel_window.M_Name,discount=0 if self.toplevel_window.sum_frame_.discount_entry.get()=='' else self.toplevel_window.sum_frame_.discount_entry.get())
            self.toplevel_window.destroy()
            self.search()
            tk.messagebox.showinfo(title='修改成功', message="修改成功", )
        except:
            tk.messagebox.showinfo(title='修改失敗', message="修改失敗", )        
    def delete(self,i,l):
        delete_od(Session(engine),i,l)
        # del self.od_l[f'{i}{l}']
        self.search()
class info_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,od, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('訂單資訊')
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  size=(100, 100))
        self.geometry("400x500")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        
        od_=get_od_info(Session(engine),od_nb=od)    
        edit_n=customtkinter.CTkLabel(self,text='訂單編號：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n1=customtkinter.CTkLabel(self,text='通路：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n2=customtkinter.CTkLabel(self,text='備註：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        
        # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
        edit_nL=customtkinter.CTkLabel(self,text=f'{od_.od_id}',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n1L=customtkinter.CTkLabel(self,text=f'{od_.pick_up}',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n2L=customtkinter.CTkLabel(self,text=f'{od_.Remark}',text_color='black',font=("microsoft yahei", 18, 'bold'))
        
        bt.grid(row=0,column=0,columnspan=2,pady=20)
        edit_n.grid(row=1,column=0)#姓名
        edit_n1.grid(row=2,column=0)#電話
        edit_n2.grid(row=3,column=0)#地址
        
        
        edit_nL.grid(row=1,column=1)#姓名
        edit_n1L.grid(row=2,column=1)#電話
        edit_n2L.grid(row=3,column=1)#地址
class profile_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,phone, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('會員資訊')
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  size=(100, 100))
        self.geometry("400x500")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        user=get_user(db=Session(engine),user_phone=phone)    
        edit_n=customtkinter.CTkLabel(self,text='會員編號：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n1=customtkinter.CTkLabel(self,text='會員姓名：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n2=customtkinter.CTkLabel(self,text='地址：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n3=customtkinter.CTkLabel(self,text='備註：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
        edit_nL=customtkinter.CTkEntry(self,text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n1L=customtkinter.CTkEntry(self,text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n2L=customtkinter.CTkEntry(self,text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n3L=customtkinter.CTkEntry(self,text_color='black',font=("microsoft yahei", 18, 'bold'))

        edit_nL.insert(customtkinter.END,f'{user.ID}')
        edit_n1L.insert(customtkinter.END,f"{user.Name}")
        edit_n2L.insert(customtkinter.END,f"{user.Address}")
        edit_n3L.insert(customtkinter.END,f"{user.Remark}")

        bt.grid(row=0,column=0,columnspan=2,pady=20)
        edit_n.grid(row=1,column=0)#姓名
        edit_n1.grid(row=2,column=0)#電話
        edit_n2.grid(row=3,column=0)#地址
        edit_n3.grid(row=4,column=0)#備註
        
        edit_nL.grid(row=1,column=1)#姓名
        edit_n1L.grid(row=2,column=1)#電話
        edit_n2L.grid(row=3,column=1)#地址
        edit_n3L.grid(row=4,column=1)#備註
class edit_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self,master, *args,key,M_Name, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('編輯訂單')
        self.master=master
        self.buy_photo = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\cart.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\cart.png"),
                                  size=(30, 30))        
        od=get_edit_od(Session(engine),key,M_Name)
        self.key=key
        self.M_Name=M_Name
        self.geometry("1600x900")
        self.columnconfigure((0,1),weight=1)
        self.input_top_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        self.input_top_.columnconfigure(5,weight=5)
        for i in range(6):
            self.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.input_top_, text="電話",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.phone=customtkinter.CTkEntry(self.input_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.phone.insert(tk.END,od[0].M_ID_.Phone)
        self.phone.configure(state='disabled')
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.input_top_, text="通路",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path=customtkinter.CTkComboBox(self.input_top_,values=["現場", "網站"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path.set(od[0].path)
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.input_top_, text="取貨方式",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up=customtkinter.CTkComboBox(self.input_top_,values=["現場", "宅配"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up.set(od[0].pick_up)
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.input_top_, text="取貨日期",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.date_=DateEntry(self.input_top_,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 18, 'bold'))
        self.date_.set_date(od[0].pick_up_date)
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.Remark_label=customtkinter.CTkLabel(self.input_top_, text="備註",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.Remark_label.grid(row=0,column=4,padx=30,pady=5)
        self.Remark_textbox = customtkinter.CTkTextbox(self.input_top_, corner_radius=0,fg_color='white',border_color='black',text_color='black',border_width=1,font=("microsoft yahei", 18, 'bold'))
        self.Remark_textbox.insert(tk.END,'' if od[0].Remark==None else od[0].Remark)
        self.Remark_textbox.grid(row=0, column=5,rowspan=3,padx=30,pady=5,sticky='we')        
        # self.input_top_=input_top(self, fg_color = ("#DDDDDD")) 
        self.input_top_.pack(fill='x',padx=30,pady=5)
        
        self.product_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        prodcuts=get_all_products(Session(engine))
        self.toplevel_window = None
        self.bt_group={}
        self.buy_list={}
        self.original_buy_list={}
        for i in od:
            self.buy_list[i.p_ID_.product_Name]=[i.count,i.money]
            self.original_buy_list[i.p_ID_.product_Name]=[i.count,i.money]
        self.a_frame=customtkinter.CTkScrollableFrame(self.product_,fg_color = ("#DDDDDD"))
        for i in range(6):
            self.a_frame.columnconfigure(i,weight=1)
        def gen_cmd(i,l):return lambda:self.buy_bt_click(i,l)
        for i in range(len(prodcuts)):
            label_Name=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Name,text_color='black',font=("microsoft yahei", 18, 'bold'))
            label_Name.grid(row=i,column=0,padx=30,sticky='w')
            label_Weight=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Weight,text_color='black',font=("microsoft yahei", 18, 'bold'))
            label_Weight.grid(row=i,column=1,padx=30)
            label_price=customtkinter.CTkLabel(self.a_frame,text=f'{prodcuts[i].product_Price}元',text_color='black',font=("microsoft yahei", 18, 'bold'))
            label_price.grid(row=i,column=2,padx=30)
            
            spinbox_1 = FloatSpinbox(self.a_frame, width=150, step_size=1)
            try:
                spinbox_1.set(self.buy_list[prodcuts[i].product_Name][0])
            except:
                spinbox_1.set(0)
            spinbox_1.grid(row=i,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,  fg_color = ("#DDDDDD"), text="",command=gen_cmd(prodcuts[i].product_Name,[spinbox_1,prodcuts[i].product_Price]))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
            
        self.a_frame.pack(side='left',anchor='n',fill='both',expand=1)
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,discount_=od[0].discount,  fg_color = ("#EEEEEE"),width=400)
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        # self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack_propagate(0)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')        
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
    def add_od(self):

        try:
            edit_order_(db=Session(engine),phone=self.phone.get(),path=self.path.get(),Pick_up=self.pick_up.get(),remark=self.Remark_textbox.get(1.0,'end'),product_=self.buy_list,date_=self.date_.get_date(),key=self.key,M_name=self.M_Name,discount=0 if self.sum_frame_.discount_entry.get()=="" else self.sum_frame_.discount_entry.get())

            self.destroy()
            tk.messagebox.showinfo(title='修改成功', message="修改成功", )
        except:
            tk.messagebox.showinfo(title='修改失敗', message="修改失敗", )

    def buy_bt_click(self,a,b):
        # discount=self.sum_frame_.discount_entry.get()
        
        self.bt_group[a]=b
        self.sum_frame_.a=a
        self.sum_frame_.buy_list=self.buy_list
        self.sum_frame_.bt_group=self.bt_group
        self.sum_frame_.pd_update_()
        self.sum_frame_.update_money()
        self.buy_list=self.sum_frame_.buy_list
        self.bt_group=self.sum_frame_.bt_group 
    def reset_(self):
        discount=self.sum_frame_.discount_entry.get()
        self.buy_list=self.original_buy_list
        self.sum_frame_.destroy()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.original_buy_list,bt_group=self.bt_group,discount_=discount,  fg_color = ("#EEEEEE"),width=400)
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack_propagate(0)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
class split_bill_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self,master, *args,key,M_Name, **kwargs):#M_Name==Phone
        super().__init__(*args, **kwargs)
        self.title('拆單')
        self.master=master
        self.buy_photo = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\cart.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\cart.png"),
                                  size=(30, 30))        
        od=get_edit_od(Session(engine),key,M_Name)
        self.key=key
        self.M_Name=M_Name
        self.geometry("1600x900")
        self.columnconfigure((0,1),weight=1)
        self.input_top_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        self.input_top_.columnconfigure(5,weight=5)
        for i in range(6):
            self.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.input_top_, text="電話",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.phone=customtkinter.CTkEntry(self.input_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.phone.insert(tk.END,od[0].M_ID_.Phone)
        self.phone.configure(state='disabled')
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.input_top_, text="通路",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path=customtkinter.CTkComboBox(self.input_top_,values=["現場", "網站"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path.set(od[0].path)
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.input_top_, text="取貨方式",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up=customtkinter.CTkComboBox(self.input_top_,values=["現場", "宅配"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up.set(od[0].pick_up)
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.input_top_, text="取貨日期",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.date_=DateEntry(self.input_top_,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 18, 'bold'))
        self.date_.set_date(od[0].pick_up_date)
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.Remark_label=customtkinter.CTkLabel(self.input_top_, text="備註",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.Remark_label.grid(row=0,column=4,padx=30,pady=5)
        self.Remark_textbox = customtkinter.CTkTextbox(self.input_top_, corner_radius=0,fg_color='white',border_color='black',text_color='black',border_width=1,font=("microsoft yahei", 18, 'bold'))
        self.Remark_textbox.insert(tk.END,'' if od[0].Remark==None else od[0].Remark)
        self.Remark_textbox.grid(row=0, column=5,rowspan=3,padx=30,pady=5,sticky='we')        
        # self.input_top_=input_top(self, fg_color = ("#DDDDDD")) 
        self.input_top_.pack(fill='x',padx=30,pady=5)
        
        self.product_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        prodcuts=spilt_bill_pd(Session(engine),self.key,self.M_Name)
        self.toplevel_window = None
        self.bt_group={}
        self.buy_list={}
        self.original_buy_list={}
        for i in od:
            self.buy_list[i.p_ID_.product_Name]=[i.count,i.money]
            self.original_buy_list[i.p_ID_.product_Name]=[i.count,i.money]
        self.a_frame=customtkinter.CTkScrollableFrame(self.product_,fg_color = ("#DDDDDD"))
        for i in range(6):
            self.a_frame.columnconfigure(i,weight=1)
        def gen_cmd(i,l):return lambda:self.buy_bt_click(i,l)
        l=0
        for i in prodcuts:
            label_Name=customtkinter.CTkLabel(self.a_frame,text=i.p_ID_.product_Name,text_color='black',font=("microsoft yahei", 18, 'bold'))
            label_Name.grid(row=l,column=0,padx=30,sticky='w')
            label_Weight=customtkinter.CTkLabel(self.a_frame,text=i.p_ID_.product_Weight,text_color='black',font=("microsoft yahei", 18, 'bold'))
            label_Weight.grid(row=l,column=1,padx=30)
            label_price=customtkinter.CTkLabel(self.a_frame,text=f'{i.p_ID_.product_Price}元',text_color='black',font=("microsoft yahei", 18, 'bold'))
            label_price.grid(row=l,column=2,padx=30)
            
            spinbox_1 = FloatSpinbox(self.a_frame, width=150, step_size=1)
            try:
                spinbox_1.set(self.buy_list[i.p_ID_.product_Name][0])
            except:
                spinbox_1.set(0)
            spinbox_1.grid(row=l,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,  fg_color = ("#DDDDDD"), text="",command=gen_cmd(i.p_ID_.product_Name,[spinbox_1,i.p_ID_.product_Price]))
            buy_button.grid(row=l,column=5, padx=30, pady=0)
            l+=1
            
        self.a_frame.pack(side='left',anchor='n',fill='both',expand=1)
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,discount_=0,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')        
        # self.product_=product_Frame(self, fg_color = ("#DDDDDD"))
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
    def add_od(self):
        try:
            spilt_bill_add(db=Session(engine),phone=self.phone.get(),path=self.path.get(),Pick_up=self.pick_up.get(),remark=self.Remark_textbox.get(1.0,'end'),product_=self.buy_list,date_=self.date_.get_date(),key=self.key,M_name=self.M_Name,discount=0 if self.sum_frame_.discount_entry.get()=="" else self.sum_frame_.discount_entry.get())

            self.destroy()
            tk.messagebox.showinfo(title='修改成功', message="修改成功", )
        except Exception as e:
            print(e)
            tk.messagebox.showinfo(title='修改失敗', message="修改失敗", )

    def buy_bt_click(self,a,b):
        # discount=self.sum_frame_.discount_entry.get()
        
        self.bt_group[a]=b
        self.sum_frame_.a=a
        self.sum_frame_.buy_list=self.buy_list
        self.sum_frame_.bt_group=self.bt_group
        self.sum_frame_.pd_update_()
        self.sum_frame_.update_money()
        self.buy_list=self.sum_frame_.buy_list
        self.bt_group=self.sum_frame_.bt_group
        # self.sum_frame_=sum_Frame(self.product_,a=a,buy_list=self.buy_list,bt_group=self.bt_group,discount_=discount,  fg_color = ("#EEEEEE"))
        # self.sum_frame_.reset_bt.configure(command=self.reset_)
        # self.sum_frame_.confirm_bt.configure(command=self.add_od)
        # self.sum_frame_.pack(side='right',anchor='n',fill='both') 
    def reset_(self):
        discount=self.sum_frame_.discount_entry.get()
        self.buy_list=self.original_buy_list
        self.sum_frame_.destroy()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.original_buy_list,bt_group=self.bt_group,discount_=discount,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
class FloatSpinbox123(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 200,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("#DDDDDD", "#DDDDDD"))  # set frame color

        self.grid_columnconfigure((0, 3), weight=0)  # buttons don't expand
        self.grid_columnconfigure((1, 2), weight=0)  # entry expands
       
        self.subtract_button = customtkinter.CTkButton(self, text="上一頁",fg_color=("#5b5a5a"), width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, padx=3, pady=3)
        self.page_max=customtkinter.CTkLabel(self)
        self.page_max.grid(row=0, column=2, padx=3, pady=3)
        self.add_button = customtkinter.CTkButton(self, text="下一頁",fg_color=("#5b5a5a"), width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=3, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "1")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            if value<=0:
                self.entry.insert(0, 1)
            else:
                self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        if value<=0:
           self.entry.insert(0, str(1))
        else: 
            self.entry.insert(0, str(int(value)))   