import customtkinter
import datetime
from sql_app.crud import Search_receipt,add_receipt,sum_receipt_money,get_edit_od,ac_get_od,ac_us
from sqlalchemy.orm import Session
from sql_app.database import engine
import tkinter as tk
class acount(customtkinter.CTkFrame):
    def __init__(self, master,selected, **kwargs):
        super().__init__(master, **kwargs)
        try:
            self.selected=selected
            self.key_=list(selected.keys())
            self.i=0
            self.toplevel_window = None
            
            recipit_=Search_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            u=ac_us(Session(engine),self.selected[self.key_[self.i]])
            
            
            self.name=u.Name
            self.left=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
            self.o_id_=customtkinter.CTkLabel(self.left,text=f'訂單編號：{self.key_[self.i]}',font=("microsoft yahei", 18, 'bold'))
            self.m_id_=customtkinter.CTkLabel(self.left,text=f'會員名稱：{self.name}',font=("microsoft yahei", 18, 'bold'))
            o_bt=customtkinter.CTkButton(self.left,text='查看訂單細節',command=self.od_info)
            self.index_info=customtkinter.CTkLabel(self.left,text=f'{self.i+1}/{len(self.selected)}',font=("microsoft yahei", 18, 'bold'))
            
            self.bt=customtkinter.CTkFrame(self.left)
            next_bt=customtkinter.CTkButton(self.bt,text='下一筆',command=self.next_)
            previous_bt=customtkinter.CTkButton(self.bt,text='上一筆',command=self.previous_)
            self.o_id_.pack(anchor='n',padx=15,pady=5)
            self.m_id_.pack(anchor='n',padx=15,pady=5)
            o_bt.pack(anchor='n',padx=15,pady=5)
            previous_bt.grid(row=0,column=0,padx=15,pady=5)
            next_bt.grid(row=0,column=1,padx=15,pady=5)
            self.bt.pack(side='bottom',padx=15,pady=5)
            self.index_info.pack(side='bottom')
            self.left.pack(side='left',anchor='n',fill='both',padx=10,pady=10)



            self.ac_now_=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
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
            self.ac_now=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
            self.ac_now.columnconfigure((0,1,2,3,4),weight=1)
            self.ac_now.pack(fill='both',expand=1)
            self.ac_now_input_1=customtkinter.CTkEntry(self.ac_now,textvariable=check_var,state='disabled',font=("microsoft yahei", 18, 'bold'))
            self.ac_now_input_2=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
            self.ac_now_input_3=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
            self.ac_now_input_4=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
            self.ac_now_input_3.insert(customtkinter.END,0)
            self.ac_now_input_4.insert(customtkinter.END,0)
            self.ac_now_input_5=customtkinter.CTkEntry(self.ac_now,font=("microsoft yahei", 18, 'bold'))
            self.ac_now_input_1.grid(row=0,column=0,sticky='ew')
            self.ac_now_input_2.grid(row=0,column=1,sticky='ew')
            self.ac_now_input_3.grid(row=0,column=2,sticky='ew')
            self.ac_now_input_4.grid(row=0,column=3,sticky='ew')
            self.ac_now_input_5.grid(row=0,column=4,sticky='ew')

            self.ac_history_=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
            self.ac_history_.columnconfigure((0,1,2,3,4),weight=1)
            ac_title_1=customtkinter.CTkLabel(self.ac_history_,text='收款日期',font=("microsoft yahei", 18, 'bold'))
            ac_title_2=customtkinter.CTkLabel(self.ac_history_,text='收款方式',font=("microsoft yahei", 18, 'bold'))
            ac_title_3=customtkinter.CTkLabel(self.ac_history_,text='收款金額',font=("microsoft yahei", 18, 'bold'))
            ac_title_4=customtkinter.CTkLabel(self.ac_history_,text='折讓',font=("microsoft yahei", 18, 'bold'))
            ac_title_5=customtkinter.CTkLabel(self.ac_history_,text='收款備註',font=("microsoft yahei", 18, 'bold'))
            ac_title_1.grid(row=0,column=0)
            ac_title_2.grid(row=0,column=1)
            ac_title_3.grid(row=0,column=2)
            ac_title_4.grid(row=0,column=3)
            ac_title_5.grid(row=0,column=4)
            self.ac_history_.pack(fill='x')

            sum_,sum_1=sum_receipt_money(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            self.a=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
            self.a.pack(fill='both',expand=1)
            self.ac_history=customtkinter.CTkScrollableFrame(self.a,fg_color = ("#DDDDDD"))
            self.ac_history.columnconfigure((0,1,2,3,4),weight=1)
            l=0
            for i in recipit_:
                ac_title_1=customtkinter.CTkLabel(self.ac_history,text=f'{i.date}',font=("microsoft yahei", 18, 'bold'))
                ac_title_2=customtkinter.CTkLabel(self.ac_history,text=f'{i.m_way}',font=("microsoft yahei", 18, 'bold'))
                ac_title_3=customtkinter.CTkLabel(self.ac_history,text=f'{i.money}',font=("microsoft yahei", 18, 'bold'))
                ac_title_4=customtkinter.CTkLabel(self.ac_history,text=f'{i.discount}',font=("microsoft yahei", 18, 'bold'))
                ac_title_5=customtkinter.CTkLabel(self.ac_history,text=f'{i.remark}',font=("microsoft yahei", 18, 'bold'))
                ac_title_1.grid(row=l,column=0)
                ac_title_2.grid(row=l,column=1)
                ac_title_3.grid(row=l,column=2)
                ac_title_4.grid(row=l,column=3)
                ac_title_5.grid(row=l,column=4)
                l+=1

            self.ac_history.pack(fill='both',expand=1)


            self.sum_=customtkinter.CTkLabel(self,text=f'總計：{0 if sum_==None else sum_}         餘額：{sum_1-(0 if sum_==None else sum_)}',font=("microsoft yahei", 18, 'bold'))
            self.sum_.pack()
            self.bt=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))

            self.ac_bt=customtkinter.CTkButton(self.bt,text='確認入賬',command=lambda:self.add_rc_(m_way=self.ac_now_input_2.get(),money=self.ac_now_input_3.get(),discount=self.ac_now_input_4.get(),remark=self.ac_now_input_5.get()))
            self.reset_ac_bt=customtkinter.CTkButton(self.bt,text='重設入帳',command=self.reset)
            self.ac_bt.pack(side='right',padx=10)
            self.reset_ac_bt.pack(side='right',padx=10)
            self.bt.pack(side='bottom',anchor='e')
        except:
            print('a')
    def reset(self):
        self.ac_now_input_2.delete(0,customtkinter.END)
        self.ac_now_input_3.delete(0,customtkinter.END)
        self.ac_now_input_4.delete(0,customtkinter.END)
        self.ac_now_input_3.insert(customtkinter.END,0)
        self.ac_now_input_4.insert(customtkinter.END,0)
        self.ac_now_input_5.delete(0,customtkinter.END)
    def next_(self):
        if self.i<len(self.selected)-1:
            self.i+=1
            self.index_info.configure(text=f'{self.i+1}/{len(self.selected)}')
            sum_,sum_1=sum_receipt_money(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            self.sum_.configure(text=f'總計：{0 if sum_==None else sum_}         餘額：{sum_1-(0 if sum_==None else sum_)}')
            self.o_id_.configure(text=f'訂單編號：{self.key_[self.i]}')
            self.m_id_.configure(text=f'會員名稱：{self.name}')
            self.ac_history.pack_forget()
            self.ac_history.destroy()
            self.ac_history=customtkinter.CTkScrollableFrame(self.a,fg_color = ("#DDDDDD"))
            self.ac_history.columnconfigure((0,1,2,3,4),weight=1)
            recipit_=Search_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            l=0
            for i in recipit_:
                ac_title_1=customtkinter.CTkLabel(self.ac_history,text=f'{i.date}',font=("microsoft yahei", 18, 'bold'))
                ac_title_2=customtkinter.CTkLabel(self.ac_history,text=f'{i.m_way}',font=("microsoft yahei", 18, 'bold'))
                ac_title_3=customtkinter.CTkLabel(self.ac_history,text=f'{i.money}',font=("microsoft yahei", 18, 'bold'))
                ac_title_4=customtkinter.CTkLabel(self.ac_history,text=f'{i.discount}',font=("microsoft yahei", 18, 'bold'))
                ac_title_5=customtkinter.CTkLabel(self.ac_history,text=f'{i.remark}',font=("microsoft yahei", 18, 'bold'))
                ac_title_1.grid(row=l,column=0)
                ac_title_2.grid(row=l,column=1)
                ac_title_3.grid(row=l,column=2)
                ac_title_4.grid(row=l,column=3)
                ac_title_5.grid(row=l,column=4)
                l+=1
            self.ac_history.pack(fill='both',expand=1)        
    def previous_(self):
        if self.i>0:
            self.i-=1
            self.index_info.configure(text=f'{self.i+1}/{len(self.selected)}')
            sum_,sum_1=sum_receipt_money(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            self.sum_.configure(text=f'總計：{0 if sum_==None else sum_}         餘額：{sum_1-(0 if sum_==None else sum_)}')
            self.o_id_.configure(text=f'訂單編號：{self.key_[self.i]}')
            self.m_id_.configure(text=f'會員名稱：{self.name}')
            self.ac_history.pack_forget()
            self.ac_history.destroy()
            self.ac_history=customtkinter.CTkScrollableFrame(self.a,fg_color = ("#DDDDDD"))
            self.ac_history.columnconfigure((0,1,2,3,4),weight=1)
            recipit_=Search_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            l=0
            for i in recipit_:
                ac_title_1=customtkinter.CTkLabel(self.ac_history,text=f'{i.date}',font=("microsoft yahei", 18, 'bold'))
                ac_title_2=customtkinter.CTkLabel(self.ac_history,text=f'{i.m_way}',font=("microsoft yahei", 18, 'bold'))
                ac_title_3=customtkinter.CTkLabel(self.ac_history,text=f'{i.money}',font=("microsoft yahei", 18, 'bold'))
                ac_title_4=customtkinter.CTkLabel(self.ac_history,text=f'{i.discount}',font=("microsoft yahei", 18, 'bold'))
                ac_title_5=customtkinter.CTkLabel(self.ac_history,text=f'{i.remark}',font=("microsoft yahei", 18, 'bold'))
                ac_title_1.grid(row=l,column=0)
                ac_title_2.grid(row=l,column=1)
                ac_title_3.grid(row=l,column=2)
                ac_title_4.grid(row=l,column=3)
                ac_title_5.grid(row=l,column=4)
                l+=1
            self.ac_history.pack(fill='both',expand=1)
    def add_rc_(self,m_way,money,discount,remark):
        try:           
            add_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]],m_way=m_way,money=money,discount=discount,remark=remark)
            tk.messagebox.showinfo(title='入賬成功', message="入賬成功", )
            sum_,sum_1=sum_receipt_money(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            self.sum_.configure(text=f'總計：{0 if sum_==None else sum_}         餘額：{sum_1-(0 if sum_==None else sum_)}')
            self.o_id_.configure(text=f'訂單編號：{self.key_[self.i]}')
            self.m_id_.configure(text=f'會員名稱：{self.name}')
            self.ac_history.pack_forget()
            self.ac_history.destroy()
            self.ac_history=customtkinter.CTkScrollableFrame(self.a,fg_color = ("#DDDDDD"))
            self.ac_history.columnconfigure((0,1,2,3,4),weight=1)
            recipit_=Search_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
            l=0
            for i in recipit_:
                ac_title_1=customtkinter.CTkLabel(self.ac_history,text=f'{i.date}',font=("microsoft yahei", 18, 'bold'))
                ac_title_2=customtkinter.CTkLabel(self.ac_history,text=f'{i.m_way}',font=("microsoft yahei", 18, 'bold'))
                ac_title_3=customtkinter.CTkLabel(self.ac_history,text=f'{i.money}',font=("microsoft yahei", 18, 'bold'))
                ac_title_4=customtkinter.CTkLabel(self.ac_history,text=f'{i.discount}',font=("microsoft yahei", 18, 'bold'))
                ac_title_5=customtkinter.CTkLabel(self.ac_history,text=f'{i.remark}',font=("microsoft yahei", 18, 'bold'))
                ac_title_1.grid(row=l,column=0)
                ac_title_2.grid(row=l,column=1)
                ac_title_3.grid(row=l,column=2)
                ac_title_4.grid(row=l,column=3)
                ac_title_5.grid(row=l,column=4)
                l+=1
            self.ac_history.pack(fill='both',expand=1)
        except:
            tk.messagebox.showinfo(title='入賬失敗', message="入賬失敗", )
    def od_info(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = od_info_ToplevelWindow(self,o_nb=self.key_[self.i],m_id=self.selected[self.key_[self.i]])  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
class od_info_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,o_nb,m_id ,**kwargs):
        super().__init__(*args, **kwargs)
        self.title('訂單資訊')
        self.geometry('1000x600')

        for i in range(4):
            self.columnconfigure(i,weight=1)
        self.columnconfigure(4,weight=2)

        a=customtkinter.CTkLabel(self,text='取貨日期',text_color='black',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=0) 
        a=customtkinter.CTkLabel(self,text='取貨方式',text_color='black',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=1) 
        a=customtkinter.CTkLabel(self,text='訂單項目',text_color='black',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=2)
        a=customtkinter.CTkLabel(self,text='是否取貨',text_color='black',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=3)
        a=customtkinter.CTkLabel(self,text='金額',text_color='black',font=("microsoft yahei", 16, 'bold'))
        a.grid(row=0,column=4)
        self.toplevel_window = None
        def gen_cmd(i):return lambda:self.od_info(i)
        def get_user(i):return lambda:self.get_u(i)
        od_l={}
        order_list=ac_get_od(Session(engine),o_nb=o_nb,m_id=m_id)
        for i in order_list:
            if i.order_number in od_l:
                od_l[i.order_number][4]+=f',{i.p_ID_.product_Name}'
                od_l[i.order_number][6]+=i.count*i.p_ID_.product_Price
            else:
                od_l[i.order_number]=[i.M_ID_.Phone,i.od_id,i.pick_up_date,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.count*i.p_ID_.product_Price]
            i=1
        for key,value in od_l.items():

            a=customtkinter.CTkLabel(self,text=f'{value[2]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=0) 
            a=customtkinter.CTkLabel(self,text=f'{value[3]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=1) 
            a=customtkinter.CTkLabel(self,text=f'{value[4]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=2,sticky='w')
            a=customtkinter.CTkLabel(self,text=f'{value[5]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=3)
            a=customtkinter.CTkLabel(self,text=f'{value[6]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=4)
            i+=1    