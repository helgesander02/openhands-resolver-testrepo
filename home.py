#-*- coding: utf-8 -*-
import tkinter as tk
import customtkinter
import os

import sqlalchemy as sa
from Order.order import Order_Main_Frame
from Menber.menber import Menber_Main_Frame
from Goods.goods import Goods_Main_Frame
from Data.data import Data_Main_Frame
from tkcalendar import DateEntry
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine,Base
from PIL import Image
import datetime
from backup import backup_Frame
import tkinter.messagebox 
# https://steam.oxxostudio.tw/category/python/tkinter/grid.html
# .grid 詳細解釋
# https://vocus.cc/article/62577184fd89780001e55c39
# .pack, .place, .grid 詳細解釋
# https://steam.oxxostudio.tw/category/python/tkinter/index.html
# Tkinter 教學

# Select_Frame 選單按鈕
class Select_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        for i in range(6):
            self.rowconfigure(i,weight=1)
        
        homeimg = Image.open(f"{os.getcwd()}\\image\\home.png")
        Rehomeimg = customtkinter.CTkImage(homeimg,size=(70,100))
        self.btn_home = customtkinter.CTkButton(self ,image=Rehomeimg ,text="" ,fg_color = "#5b5a5a" ,corner_radius=0)
        self.btn_home.grid(row=0, column=0,sticky='nsew')

        orderimg = Image.open(f"{os.getcwd()}\\image\\order.png")
        Reorderimg = customtkinter.CTkImage(orderimg,size=(70,100))
        self.btn_order = customtkinter.CTkButton(self ,image=Reorderimg ,text="" ,fg_color = "#5b5a5a" ,corner_radius=0)
        self.btn_order.grid(row=1, column=0,sticky='nsew')

        menberimg = Image.open(f"{os.getcwd()}\\image\\menber.png")
        Remenberimg = customtkinter.CTkImage(menberimg,size=(70,100))
        self.btn_menber = customtkinter.CTkButton(self ,image=Remenberimg ,text="" ,fg_color = "#5b5a5a" ,corner_radius=0)
        self.btn_menber.grid(row=2, column=0,sticky='nsew')

        goodsimg = Image.open(f"{os.getcwd()}\\image\\goods.png")
        Regoodsimg = customtkinter.CTkImage(goodsimg,size=(70,100))
        self.btn_goods = customtkinter.CTkButton(self ,image=Regoodsimg ,text="" ,fg_color = "#5b5a5a" ,corner_radius=0)
        self.btn_goods.grid(row=3, column=0,sticky='nsew')

        dataimg = Image.open(f"{os.getcwd()}\\image\\data.png")
        Redataimg = customtkinter.CTkImage(dataimg,size=(70,100))
        self.btn_data = customtkinter.CTkButton(self ,image=Redataimg ,text="" ,fg_color = "#5b5a5a" ,corner_radius=0)
        self.btn_data.grid(row=4, column=0,sticky='nsew')
        
        self.backup = customtkinter.CTkButton(self,text='備份',fg_color = "#5b5a5a",corner_radius=0,width=70,height=100)
        self.backup.grid(row=5, column=0,sticky='nsew')
    def reset_(self):
        self.btn_home.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_order.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_menber.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_goods.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_data.configure(fg_color = "#5b5a5a",text_color='white')

# Home_Main_Frame (Search_Frame, Schedule_Frame) 主頁
class Search_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.toplevel_window = None
        #會員查詢
        # #relx/rely range[0.0, 1,0]
        MS_label = customtkinter.CTkLabel(self, text="會員查詢" ,font=("microsoft yahei", 35, 'bold'),text_color='black')
        MS_label.place(relx=0.1, rely=0.5, anchor=tk.CENTER)
        
        self.MS_entry = customtkinter.CTkEntry(self, width=250, height=40, 
                                                        border_width=3,
                                                        border_color=("#5b5a5a"), 
                                                        fg_color=("#DDDDDD"),
                                                        text_color='black',font=("microsoft yahei", 18, 'bold'))

        self.MS_entry.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        
        self.MS_button = customtkinter.CTkButton(self, text="Q", width=40, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'),command=lambda:self.confirm_user(self.MS_entry.get()))

        self.MS_button.place(relx=0.42, rely=0.5, anchor=tk.CENTER)

        #顯示是否有此會員
        self.tf_label = customtkinter.CTkLabel(self, text="",font=("microsoft yahei", 18, 'bold'))
        self.tf_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #2個按鈕
        self.order_button = customtkinter.CTkButton(self, text="新增訂單", width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'))

        self.order_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

        self.menber_button = customtkinter.CTkButton(self, text="新增會員", width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.open_add_toplevel)

        self.menber_button.place(relx=0.9, rely=0.5, anchor=tk.CENTER)
    def confirm_user(self,phone):
        yes_or_no='有此會員' if get_user(Session(engine),user_phone=phone.strip())!=None else '沒有此會員'
        self.tf_label.configure(text=yes_or_no)
    def open_add_toplevel(self):
        phone=''
        if  self.tf_label.cget('text')=='沒有此會員':
            phone=self.MS_entry.get()
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = add_ToplevelWindow(self,add_phone=phone)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
class add_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,add_phone='', **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x500")
        self.title('新增會員')
        try:
            self.title('新增會員')
            self.columnconfigure((0,1),weight=1)
            self.rowconfigure((3,4),weight=2)
            
            edit_n=customtkinter.CTkLabel(self,text='姓名',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n1=customtkinter.CTkLabel(self,text='電話',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n2=customtkinter.CTkLabel(self,text='地址',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n3=customtkinter.CTkLabel(self,text='備註',text_color='black',font=("microsoft yahei", 18, 'bold'))
            # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
            self.edit_entry_n=customtkinter.CTkEntry(self,font=("microsoft yahei", 18, 'bold'))
            self.edit_entry_n1=customtkinter.CTkEntry(self,font=("microsoft yahei", 18, 'bold'))
            self.edit_entry_n2=customtkinter.CTkTextbox(self,border_color='black',border_width=2,font=("microsoft yahei", 18, 'bold'))
            self.edit_entry_n3=customtkinter.CTkTextbox(self,border_color='black',border_width=2,font=("microsoft yahei", 18, 'bold'))
            self.edit_entry_n1.insert(customtkinter.END,add_phone)

            self.cancel_bt=customtkinter.CTkButton(self,text='取消',command=self.cancel_click,fg_color=("#5b5a5a"),font=("microsoft yahei", 18, 'bold'))
            confirm_bt=customtkinter.CTkButton(self,text='確定新增',command=self.confirm_edit,fg_color=("#5b5a5a"),font=("microsoft yahei", 18, 'bold'))
            self.cancel_bt.grid(row=5,column=0,sticky='e',padx=30,pady=10)
            confirm_bt.grid(row=5,column=1,sticky='e',padx=30,pady=10)
            # edit_n4.grid(row=0,column=0)
            edit_n.grid(row=1,column=0)#姓名
            edit_n1.grid(row=2,column=0)#電話
            edit_n2.grid(row=3,column=0)#地址
            edit_n3.grid(row=4,column=0)#備註
            
            self.edit_entry_n.grid(row=1,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n1.grid(row=2,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n2.grid(row=3,column=1,sticky='nsew',padx=10,pady=10)
            self.edit_entry_n3.grid(row=4,column=1,sticky='nsew',padx=10,pady=10)
            
        except:
            error_label=customtkinter.CTkLabel(self,text='查詢失敗，請回上層進行查詢',font=("microsoft yahei", 18, 'bold'))
            error_bt=customtkinter.CTkButton(self,text='回上層',command=self.cancel_click)
            error_label.pack(anchor='center',fill='y',pady=30)
            error_bt.pack(anchor='center',fill='y',pady=10)
    def cancel_click(self):
        self.destroy()
    def confirm_edit(self):
        try:
            add_data(Session(engine),name=self.edit_entry_n.get(),phone=self.edit_entry_n1.get(),address=self.edit_entry_n2.get(1.0,tk.END),remark=self.edit_entry_n3.get(1.0,tk.END))
            self.destroy()
            tkinter.messagebox.showinfo(title='新增成功', message="新增成功", )
        except:
            tkinter.messagebox.showinfo(title='新增失敗', message="新增失敗", )
class Schedule_Frame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,date_, **kwargs):
        super().__init__(master, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  size=(30, 30))
        self.info = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\information-button.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\information-button.png"),
                                  size=(30, 30))
        # b=customtkinter.CTkFrame(self,fg_color = ("#5b5a5a"))
        for i in range(7):
            self.columnconfigure(i,weight=1)
            # b.columnconfigure(i,weight=1)
        self.columnconfigure(4,weight=2)
        # b.columnconfigure(4,weight=2)
        
        a=customtkinter.CTkLabel(self,text='會員資訊',fg_color = ("#5b5a5a"),text_color='White',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=0,sticky='ew')
        a=customtkinter.CTkLabel(self,text='訂單資訊',fg_color = ("#5b5a5a"),text_color='White',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=1,sticky='ew')
        a=customtkinter.CTkLabel(self,text='取貨日期',fg_color = ("#5b5a5a"),text_color='White',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=2,sticky='ew') 
        a=customtkinter.CTkLabel(self,text='取貨方式',fg_color = ("#5b5a5a"),text_color='White',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=3,sticky='ew') 
        a=customtkinter.CTkLabel(self,text='訂單項目',fg_color = ("#5b5a5a"),text_color='White',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=4,sticky='ew')
        a=customtkinter.CTkLabel(self,text='是否取貨',fg_color = ("#5b5a5a"),text_color='White',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=5,sticky='ew')
        a=customtkinter.CTkLabel(self,text='金額',fg_color = ("#5b5a5a"),text_color='White',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=6,sticky='ew')
        # b.grid(row=0,column=0,columnspan=7,sticky='ew')
        self.toplevel_window = None
        def gen_cmd(i):return lambda:self.od_info(i)
        def get_user(i):return lambda:self.get_u(i)
        if date_!='':
            od_l={}
            order_list=home_search_date(db=Session(engine),date_=date_)
            for i in order_list:
                if f'{i.order_number}{i.M_ID}' in od_l:
                    od_l[f'{i.order_number}{i.M_ID}'][4]+=f',{i.p_ID_.product_Name}'
                    # od_l[f'{i.order_number}{i.M_ID}'][6]+=i.count*i.p_ID_.product_Price
                else:
                    od_l[f'{i.order_number}{i.M_ID}']=[i.M_ID_.Phone,i.od_id,i.pick_up_date,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.total]
            i=1
            for key,value in od_l.items():
                a=customtkinter.CTkButton(self,image=self.image,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_user(value[0]))
                a.grid(row=i,column=0)
                a=customtkinter.CTkButton(self,image=self.info,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd(value[1]))
                a.grid(row=i,column=1)
                a=customtkinter.CTkLabel(self,text=f'{value[2]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
                a.grid(row=i,column=2) 
                a=customtkinter.CTkLabel(self,text=f'{value[3]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
                a.grid(row=i,column=3)
                b=customtkinter.CTkScrollableFrame(self,orientation='horizontal',height=20) 
                a=customtkinter.CTkLabel(b,text=f'{value[4]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
                a.pack(side='left')
                b.grid(row=i,column=4,sticky='we')
                a=customtkinter.CTkLabel(self,text=f'{value[5]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
                a.grid(row=i,column=5)
                a=customtkinter.CTkLabel(self,text=f'{value[6]}',fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
                a.grid(row=i,column=6)
                i+=1
    def od_info(self,a):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = info_window(self,a=a)
            self.toplevel_window.attributes('-topmost','true')# create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
    def get_u(self,i):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = profile_ToplevelWindow(self,phone=i)  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()

class profile_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,phone, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  size=(100, 100))
        self.geometry("400x500")
        self.title('會員資訊')
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        user=get_user(db=Session(engine),user_phone=phone)    
        edit_n=customtkinter.CTkLabel(self,text='會員編號：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n1=customtkinter.CTkLabel(self,text='會員姓名：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n2=customtkinter.CTkLabel(self,text='地址：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n3=customtkinter.CTkLabel(self,text='備註：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        
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

class info_window(customtkinter.CTkToplevel):
    def __init__(self, *args,a, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\user.png"),
                                  size=(100, 100))
        self.title('訂單資訊')
        self.geometry("400x500")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        
        od_=get_od_info(Session(engine),od_nb=a)    
        edit_n=customtkinter.CTkLabel(self,text='訂單編號：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n1=customtkinter.CTkLabel(self,text='通路：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n2=customtkinter.CTkLabel(self,text='備註：',text_color='black',font=("microsoft yahei", 18, 'bold'))
        
        edit_nL=customtkinter.CTkLabel(self,text=f'{od_.order_number+od_.M_ID}',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n1L=customtkinter.CTkLabel(self,text=f'{od_.pick_up}',text_color='black',font=("microsoft yahei", 18, 'bold'))
        edit_n2L=customtkinter.CTkLabel(self,text=f'{od_.Remark}',text_color='black',font=("microsoft yahei", 18, 'bold'))
        
        bt.grid(row=0,column=0,columnspan=2,pady=20)
        edit_n.grid(row=1,column=0)#姓名
        edit_n1.grid(row=2,column=0)#電話
        edit_n2.grid(row=3,column=0)#地址
        
        
        edit_nL.grid(row=1,column=1)#姓名
        edit_n1L.grid(row=2,column=1)#電話
        edit_n2L.grid(row=3,column=1)#地址

class Home_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\search.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\search.png"),
                                  size=(30, 30))
        #Search_Frame
        self.Search_Frame_ = Search_Frame(self,  fg_color = ("#DDDDDD"))
        self.Search_Frame_.pack(pady=30,padx=30,fill='x')
        self.se_date=customtkinter.CTkFrame(self,  fg_color = ("#EEEEEE"))
        # DateEntry https://tkcalendar.readthedocs.io/en/stable/_modules/tkcalendar/dateentry.html#DateEntry.configure
        self.date_=DateEntry(self.se_date,selectmode='day', width=15,font=("microsoft yahei", 24, 'bold'),date_pattern='yyyy-mm-dd')
        self.date_MS_button = customtkinter.CTkButton(self.se_date ,text='',width=30,fg_color = "#EEEEEE",hover=False,image=self.image,command=self.search_date)
      
        self.date_.grid(row=0,column=0)
        self.date_MS_button.grid(row=0,column=1)
        self.se_date.pack(anchor='w',padx=30)
        #Schedule_Frame
        
        self.Schedule_Frame_ = Schedule_Frame(self,date_=datetime.date.today(),  fg_color = ("#DDDDDD"))
        self.Schedule_Frame_.pack(fill='both',expand=1,padx=30)
    def search_date(self):
        self.Schedule_Frame_.pack_forget()
        self.Schedule_Frame_.destroy()
        self.Schedule_Frame_=Schedule_Frame(self,date_=self.date_.get_date(),  fg_color = ("#DDDDDD"))
        self.Schedule_Frame_.pack(fill='both',expand=1,padx=30) 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Define System  
        self.title("美而香管理系統")
        customtkinter.set_appearance_mode("light")
        if not sa.inspect(engine).has_table('Member'):
            Base.metadata.create_all(engine)
        #Define Home
        #Select_Frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
        self.Select_Frame = Select_Frame(self,  fg_color = ("#5b5a5a"))
        self.Select_Frame.pack(fill='both',side='left')
        #Main_Frame
        self.Main_Frame = Home_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
        self.Main_Frame1 = Order_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0)
        self.Main_Frame2 = Menber_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
        self.Main_Frame3 = Goods_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
        self.Main_Frame4 = Data_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
        self.Main_Frame5 = backup_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
        self.Main_Frame.Search_Frame_.order_button.configure(command=self.open_order_)
        # self.Main_Frame.grid(row=0, column=1,sticky='nsew')
        self.Main_Frame.pack(fill='both',expand=1)
        #關掉主要的Frame開啟對應btn的Frame
        #隱藏的方法 https://www.delftstack.com/zh-tw/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/

        def open_home (event):
            self.forget_()
            self.Main_Frame.search_date()
            self.Main_Frame.pack(fill='both',expand=1)   
            # self.Main_Frame.pack_forget()

            # self.Main_Frame = Home_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            # self.Main_Frame.Search_Frame_.order_button.configure(command=self.open_order_)
            # self.Main_Frame.pack(fill='both',expand=1)

        def open_order (event):
            self.forget_()
            self.Main_Frame1.input_order_.update_product()
            self.Main_Frame1.pack(fill='both',expand=1)            
            # self.Main_Frame.pack_forget()
  
            # self.Main_Frame = Order_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0)
            # self.Main_Frame.pack(fill='both',expand=1)

        def open_menber (event):
            self.forget_()
            self.Main_Frame2.pack(fill='both',expand=1)
            self.Main_Frame2.choose_bt.configure(command=self.member_open_order_)
            # self.Main_Frame.pack_forget()
   
            # self.Main_Frame = Menber_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            # self.Main_Frame.pack(fill='both',expand=1)

        def open_goods (event):
            self.forget_()
            self.Main_Frame3.goods_F1.product_.update_product( )
            self.Main_Frame3.pack(fill='both',expand=1)
            # self.Main_Frame.pack_forget()

            # self.Main_Frame = Goods_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            # self.Main_Frame.pack(fill='both',expand=1)

        def open_data (event):
            self.forget_()
            self.Main_Frame4.pack(fill='both',expand=1)
            # self.Main_Frame.pack_forget()

            # self.Main_Frame = Data_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            # self.Main_Frame.pack(fill='both',expand=1)

        def open_back (event):
            self.forget_()
            self.Main_Frame5.pack(fill='both',expand=1)

        #切換功能
        #btn事件教學 https://ithelp.ithome.com.tw/articles/10275712?sc=iThomeR
        self.Select_Frame.btn_home.bind("<Button-1>", open_home)
        self.Select_Frame.btn_order.bind("<Button-1>", open_order)
        self.Select_Frame.btn_menber.bind("<Button-1>", open_menber)
        self.Select_Frame.btn_goods.bind("<Button-1>", open_goods)
        self.Select_Frame.btn_data.bind("<Button-1>", open_data)
        self.Select_Frame.backup.bind("<Button-1>",open_back)
        
    def open_order_(self):
        phone=''
        if self.Main_Frame.Search_Frame_.tf_label.cget('text')=='有此會員':
            phone=self.Main_Frame.Search_Frame_.MS_entry.get()
        self.forget_()
        self.Main_Frame1.pack(fill='both',expand=1)
        # self.Main_Frame.pack_forget()
        # self.Main_Frame = Order_Main_Frame(self,fg_color = ("#EEEEEE"), corner_radius=0)
        self.Main_Frame1.input_order_.phone.delete(0,customtkinter.END)
        self.Main_Frame1.input_order_.phone.insert(customtkinter.END,phone)
        self.Main_Frame1.forget_()
        self.Main_Frame1.bt_frame.reset_color()
        self.Main_Frame1.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
        self.Main_Frame1.input_order_.pack(fill='both',expand=1,padx=40,pady=40,anchor='nw')
        # self.Main_Frame.pack(fill='both',expand=1)
    def member_open_order_(self):
        self.forget_()
        self.Main_Frame1.pack(fill='both',expand=1)
        # self.Main_Frame.pack_forget()
        # self.Main_Frame = Order_Main_Frame(self,fg_color = ("#EEEEEE"), corner_radius=0)
        self.Main_Frame1.input_order_.phone.delete(0,customtkinter.END)
        self.Main_Frame1.input_order_.phone.insert(customtkinter.END,self.Main_Frame2.choose_label.cget('text'))
        self.Main_Frame1.forget_()
        self.Main_Frame1.bt_frame.reset_color()
        self.Main_Frame1.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
        self.Main_Frame1.input_order_.pack(fill='both',expand=1,padx=40,pady=40,anchor='nw')
    def forget_(self):
        self.Main_Frame.pack_forget()
        self.Main_Frame1.pack_forget()
        self.Main_Frame2.pack_forget()
        self.Main_Frame3.pack_forget()
        self.Main_Frame4.pack_forget()
        self.Main_Frame5.pack_forget()
if __name__ == "__main__":
    app = App()
    app.after(0, lambda: app.wm_state('zoomed'))
    app.mainloop()
