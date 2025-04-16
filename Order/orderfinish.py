import customtkinter
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine
from tkcalendar import DateEntry
import datetime
import tkinter.messagebox 
class finish_search_fame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.toplevel_window = None
        self.selected_pd={}
        # 搜尋
        search_f=customtkinter.CTkFrame(self,fg_color=("#EEEEEE"))
       
        self.reset_btn = customtkinter.CTkButton(search_f, width=150, height=40, text="重設查詢",
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.refresh
                                                    )        

        self.search=customtkinter.CTkEntry(search_f,fg_color = ("#DDDDDD"),text_color='black',placeholder_text="客戶電話",font=("microsoft yahei", 18, 'bold'))
        self.search_bt=customtkinter.CTkButton(search_f, text="確認查詢", width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        command=self.search_A)
        self.search.pack(side='top',pady=40,padx=30,fill='x')
        self.reset_btn.pack(side='bottom',pady=20,padx=30)        
        self.search_bt.pack(side='bottom',pady=20,padx=30)
        search_f.pack(anchor='n',fill='both',side='left',padx=30,pady=5)

        # 客戶資訊
        top=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        top.columnconfigure((0,1),weight=1)
        self.customer_name = customtkinter.CTkLabel(top,text="客戶名稱：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.address = customtkinter.CTkLabel(top,text="地址：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.phone = customtkinter.CTkLabel(top,text="　　手機：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.remark = customtkinter.CTkLabel(top,text="備註：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.customer_name.grid(row=0,column=0,sticky='w')
        self.address.grid(row=0,column=1,sticky='w')
        self.phone.grid(row=1,column=0,sticky='w')
        self.remark.grid(row=1,column=1,sticky='w')
        top.pack(fill='x')

        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='日期',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n1=customtkinter.CTkLabel(self.history_frame,text='訂單內容',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n2=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n3=customtkinter.CTkLabel(self.history_frame,text='已收金額',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n4=customtkinter.CTkLabel(self.history_frame,text='餘額',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n5=customtkinter.CTkLabel(self.history_frame,text='',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        order_n5.grid(row=0,column=5)
        # self.history_frame.pack(fill='both',anchor='n',pady=40,padx=30,expand=1)

        self.ac_fame=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.ac_fame.pack(fill='both',side='bottom',pady=40,padx=30)
        self.ac=customtkinter.CTkButton(self.ac_fame, width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),text='入賬')
        self.one_time_ac=customtkinter.CTkButton(self.ac_fame, width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),text='一次入賬多筆',command=self.once_ac)
        self.ac.pack(side='right',padx=20)
        self.one_time_ac.pack(side='right',padx=20)
    def refresh(self):
        self.search.delete(0,tk.END)
        self.selected_pd={}
        self.search_A()
    def search_A(self):
        try:
            self.od_l={}
            user=get_user(Session(engine),user_phone=self.search.get().strip())
            self.customer_name.configure(text=f'客戶名稱：{user.Name}')
            self.address.configure(text=f'地址：：{user.Address}')
            self.phone.configure(text=f'　　手機：{user.Phone}')
            self.remark.configure(text=f'備註：{user.Remark}')
            for i in user.orders:
                if i.order_number in self.od_l:
                    self.od_l[i.order_number][1]+=f',{i.p_ID_.product_Name}'
                    if i.discount!=None:self.od_l[i.order_number][3]=i.discount
                else:
                    self.od_l[i.order_number]=[i.M_ID_.ID,i.p_ID_.product_Name,i.money,i.discount,i.pick_up_date]
        except Exception as e:
            
            self.od_l={}
            self.customer_name.configure(text=f'客戶名稱：')
            self.address.configure(text=f'地址：')
            self.phone.configure(text=f'　　手機：')
            self.remark.configure(text=f'備註：')
        self.history_frame.pack_forget() 
        self.history_frame.destroy()
        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.history_frame.columnconfigure((0,1,3,4,5),weight=1)
        self.history_frame.columnconfigure(2,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='日期',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n1=customtkinter.CTkLabel(self.history_frame,text='訂單內容',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n2=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n3=customtkinter.CTkLabel(self.history_frame,text='已收金額',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n4=customtkinter.CTkLabel(self.history_frame,text='餘額',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n5=customtkinter.CTkLabel(self.history_frame,text='',text_color='black')
        order_n.grid(row=0,column=1,sticky='w')
        order_n1.grid(row=0,column=2,sticky='w')
        order_n2.grid(row=0,column=3)
        order_n3.grid(row=0,column=4)
        order_n4.grid(row=0,column=5)
        order_n5.grid(row=0,column=0)
        
        l=1
        def gen_cmd(i,l):return lambda:self.update_(i,l)
        for key,value in self.od_l.items():
            sum_,sum_1=sum_receipt_money(db=Session(engine),o_id=key,m_id=value[0])
            order_n=customtkinter.CTkLabel(self.history_frame,text=f'{value[-1]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            b=customtkinter.CTkScrollableFrame(self.history_frame,orientation='horizontal',height=20)
            order_n1=customtkinter.CTkLabel(b,text=f'{value[1]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            order_n2=customtkinter.CTkLabel(self.history_frame,text=f'{0 if sum_1==None else sum_1}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            order_n3=customtkinter.CTkLabel(self.history_frame,text=f'{0 if sum_==None else sum_}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            order_n4=customtkinter.CTkLabel(self.history_frame,text=f'{sum_1-(0 if sum_==None else sum_)}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            if sum_1-(0 if sum_==None else sum_)!=0:
                order_n5=customtkinter.CTkCheckBox(self.history_frame,text='', command=gen_cmd(key,value[0]), onvalue="on", offvalue="off")
                order_n5.grid(row=l,column=0)
            order_n.grid(row=l,column=1,sticky='w')
            order_n1.pack(side='left')
            b.grid(row=l,column=2,sticky='ew')
            order_n2.grid(row=l,column=3)
            order_n3.grid(row=l,column=4)
            order_n4.grid(row=l,column=5)
            
            l+=1
        self.history_frame.pack(fill='both',anchor='n',pady=40,padx=30,expand=1)
    def update_(self,key,m_id):
        if key in self.selected_pd:
            del self.selected_pd[key]
            
        else:
            self.selected_pd[key]=m_id
    def once_ac(self):
        if len(self.selected_pd)!=0:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = cm_ToplevelWindow(self,selected=self.selected_pd)   
                self.toplevel_window.attributes('-topmost','true')   
            else:
                self.toplevel_window.focus()
        else:
            tkinter.messagebox.showinfo(title='失敗', message="請勾選想要入帳的訂單", )
class cm_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,selected, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.selected_pd=selected
        self.title('一次入賬多筆')
        self.ac_now_=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.ac_now_.columnconfigure((0,1,2,3,4),weight=1)
        self.ac_now_.pack(fill='x')
        ac_now_title_1=customtkinter.CTkLabel(self.ac_now_,text='收款日期',font=("microsoft yahei", 18, 'bold'))
        ac_now_title_2=customtkinter.CTkLabel(self.ac_now_,text='收款方式',font=("microsoft yahei", 18, 'bold'))
        ac_now_title_3=customtkinter.CTkLabel(self.ac_now_,text='收款金額',font=("microsoft yahei", 18, 'bold'))
        ac_now_title_4=customtkinter.CTkLabel(self.ac_now_,text='折讓',font=("microsoft yahei", 18, 'bold'))
        ac_now_title_5=customtkinter.CTkLabel(self.ac_now_,text='收款備註',font=("microsoft yahei", 18, 'bold'))
        ac_now_title_1.grid(row=0,column=0)
        ac_now_title_2.grid(row=0,column=1)
        ac_now_title_3.grid(row=0,column=2)
        ac_now_title_4.grid(row=0,column=3)
        ac_now_title_5.grid(row=0,column=4)
        check_var = customtkinter.StringVar(value=datetime.date.today())
        self.ac_now=customtkinter.CTkScrollableFrame(self,fg_color = ("#EEEEEE"))
        self.ac_now.columnconfigure((0,1,2,3,4),weight=1)
        self.ac_now.pack(fill='both',expand=1)
        self.ac_now_input_1=customtkinter.CTkEntry(self.ac_now,textvariable=check_var,state='disabled',font=("microsoft yahei", 18, 'bold'))
        self.ac_now_input_2=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
        self.ac_now_input_3=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
        self.ac_now_input_4=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
        self.ac_now_input_5=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
        self.ac_now_input_3.insert(customtkinter.END,0)
        self.ac_now_input_4.insert(customtkinter.END,0)
        self.ac_now_input_1.grid(row=0,column=0,sticky='ew')
        self.ac_now_input_2.grid(row=0,column=1,sticky='ew')
        self.ac_now_input_3.grid(row=0,column=2,sticky='ew')
        self.ac_now_input_4.grid(row=0,column=3,sticky='ew')
        self.ac_now_input_5.grid(row=0,column=4,sticky='ew')

        bt=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.cancel_bt=customtkinter.CTkButton(bt,text='取消',fg_color=("#5b5a5a"),command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
        confirm_bt=customtkinter.CTkButton(bt,text='確定入賬',fg_color=("#5b5a5a"),command=self.confirm_edit,font=("microsoft yahei", 18, 'bold'))
        self.cancel_bt.grid(row=0,column=0,sticky='e',padx=30,pady=10)
        confirm_bt.grid(row=0,column=1,sticky='e',padx=30,pady=10)
        bt.pack(side='bottom')
    def cancel_click(self):
        self.destroy()
    def confirm_edit(self):
        try:
            update_balance(db=Session(engine),selected=self.selected_pd,cm=self.ac_now_input_3.get(),m_way=self.ac_now_input_2.get(),remark=self.ac_now_input_5.get(),discount=self.ac_now_input_4.get())
            tkinter.messagebox.showinfo(title='入賬成功', message="入賬成功", )
            self.destroy()
        except:
            tkinter.messagebox.showinfo(title='入賬失敗', message="入賬失敗", )