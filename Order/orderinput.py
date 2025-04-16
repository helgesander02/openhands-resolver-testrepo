import customtkinter
from PIL import Image
from tkcalendar import DateEntry
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine
from .floatspinbox import FloatSpinbox,sum_Frame
import datetime
import tkinter.messagebox 
import os
class input_order(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.buy_photo = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\cart.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\cart.png"),
                                  size=(30, 30))
        self.columnconfigure((0,1),weight=1)
        self.input_top_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        # self.input_top_.columnconfigure(5,weight=5)
        for i in range(3):
            self.input_top_.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.input_top_, text="電話",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.phone=customtkinter.CTkEntry(self.input_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.input_top_, text="通路",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path=customtkinter.CTkComboBox(self.input_top_,values=["現場", "網站"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.input_top_, text="取貨方式",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up=customtkinter.CTkComboBox(self.input_top_,values=["現場", "宅配"],fg_color = ("#DDDDDD"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.pick_up_label.grid(row=1,column=2,padx=30,pady=5)
        self.pick_up.grid(row=1,column=3,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.input_top_, text="取貨日期",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.date_=DateEntry(self.input_top_,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 18, 'bold'))
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)

        self.Remark_label=customtkinter.CTkLabel(self.input_top_, text="備註",text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.Remark_label.grid(row=0,column=4,padx=30,pady=5)
        self.Remark_textbox = customtkinter.CTkTextbox(self.input_top_, corner_radius=0,fg_color='white',border_color='black',text_color='black',border_width=1,font=("microsoft yahei", 18, 'bold'),height=100)
        self.Remark_textbox.grid(row=0, column=5,padx=30,pady=5)        
        # self.input_top_=input_top(self, fg_color = ("#DDDDDD")) 
        
        
        
        self.product_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        prodcuts=get_all_products(Session(engine))
        self.toplevel_window = None
        self.bt_group={}
        self.buy_list={}
        self.a_frame=customtkinter.CTkScrollableFrame(self.product_,fg_color = ("#DDDDDD"))
        
        for i in range(5):
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
            # self.bt_group[prodcuts[i].product_Name]=[spinbox_1,prodcuts[i].product_Price]
            spinbox_1.grid(row=i,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,fg_color = ("#DDDDDD"), text="",command=gen_cmd(prodcuts[i].product_Name,[spinbox_1,prodcuts[i].product_Price]))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
        self.sum_frame_Fake=customtkinter.CTkFrame(self)
        self.sum_frame_Fake.pack(anchor='n',side='right',fill='both')
        self.sum_frame_=sum_Frame(self.sum_frame_Fake,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"),width=400)
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack_propagate(0)
        # title.pack(anchor='w',side='top',fill='both')

        self.sum_frame_.pack(anchor='n',side='right',fill='both')  

        self.input_top_.pack(anchor='w',padx=30,pady=5)    
        self.a_frame.pack(fill='both',anchor='n',expand=1)

              
        # self.product_=product_Frame(self, fg_color = ("#DDDDDD"))
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
    def update_product(self):
        self.a_frame.pack_forget()
        self.a_frame.destroy()
        self.a_frame=customtkinter.CTkScrollableFrame(self.product_,fg_color = ("#DDDDDD"))
        prodcuts=get_all_products(Session(engine))
        for i in range(5):
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

                # self.bt_group[prodcuts[i].product_Name]=[spinbox_1,prodcuts[i].product_Price]
            spinbox_1.grid(row=i,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,fg_color = ("#DDDDDD"), text="",command=gen_cmd(prodcuts[i].product_Name,[spinbox_1,prodcuts[i].product_Price]))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
            
        self.a_frame.pack(fill='both',anchor='n',expand=1)        
    def add_od(self):
        try:
            add_order(db=Session(engine),phone=self.phone.get(),Pick_up=self.pick_up.get(),remark=self.Remark_textbox.get(1.0,'end'),product_=self.buy_list,m_id='1',date_=self.date_.get_date(),path=self.path.get(),discount=0 if self.sum_frame_.discount_entry.get()=='' else self.sum_frame_.discount_entry.get())
            self.phone.delete(0,customtkinter.END)
            self.path.set('現場')
            self.pick_up.set('現場')
            self.date_.set_date(datetime.datetime.today())
            self.Remark_textbox.delete('0.0',customtkinter.END)
            self.sum_frame_.pack_forget()
            self.a_frame.pack_forget()
            self.sum_frame_.destroy()
            self.a_frame.destroy()
            self.a_frame=customtkinter.CTkScrollableFrame(self.product_,fg_color = ("#DDDDDD"))
            self.bt_group={}
            self.buy_list={}
            prodcuts=get_all_products(Session(engine))
            for i in range(5):
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

                # self.bt_group[prodcuts[i].product_Name]=[spinbox_1,prodcuts[i].product_Price]
                spinbox_1.grid(row=i,column=4,pady=0)
                buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,fg_color = ("#DDDDDD"), text="",command=gen_cmd(prodcuts[i].product_Name,[spinbox_1,prodcuts[i].product_Price]))
                buy_button.grid(row=i,column=5, padx=30, pady=0)
            
            self.a_frame.pack(fill='both',anchor='n',expand=1)
            self.sum_frame_=sum_Frame(self.sum_frame_Fake,a='',buy_list={},bt_group={},  fg_color = ("#EEEEEE"),width=400)
            self.sum_frame_.reset_bt.configure(command=self.reset_)
            self.sum_frame_.confirm_bt.configure(command=self.add_od)
            self.sum_frame_.pack_propagate(0)
            self.sum_frame_.pack(side='right',anchor='n',fill='both')
            
            tkinter.messagebox.showinfo(title='新增成功', message="新增成功", )            
        except Exception as e:
            print(e)
            tkinter.messagebox.showinfo(title='新增失敗', message="新增失敗", )
    def buy_bt_click(self,a,b):
        self.bt_group[a]=b
        self.sum_frame_.a=a
        self.sum_frame_.buy_list=self.buy_list
        self.sum_frame_.bt_group=self.bt_group
        self.sum_frame_.pd_update_()
        self.sum_frame_.update_money()
        self.buy_list=self.sum_frame_.buy_list
        self.bt_group=self.sum_frame_.bt_group       
    def reset_(self):
        self.buy_list={}
        self.sum_frame_.pack_forget()
        self.sum_frame_.destroy()
        self.sum_frame_=sum_Frame(self.sum_frame_Fake,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"),width=400)
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack_propagate(0)
        self.sum_frame_.pack(anchor='n',side='right',fill='both')
        

