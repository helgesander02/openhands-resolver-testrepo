import customtkinter
from typing import Union
from typing import Callable
class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("#DDDDDD", "#DDDDDD"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-",fg_color=("#5b5a5a"), width=height-6, height=height-6,text_color='white',
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+",fg_color=("#5b5a5a"), width=height-6, height=height-6,text_color='white',
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0")

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
                self.entry.insert(0, 0)
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
           self.entry.insert(0, str(0))
        else: 
            self.entry.insert(0, str(int(value)))
class sum_Frame(customtkinter.CTkFrame):
    def __init__(self, master,a,buy_list,bt_group,discount_=0, **kwargs):
        super().__init__(master, **kwargs)
        self.a=a
        self.buy_list=buy_list
        self.bt_group=bt_group
        title=customtkinter.CTkLabel(self,text='訂單項目',fg_color=("#5b5a5a"),text_color='white',font=("microsoft yahei", 18, 'bold'))
        title.pack(fill='x')
        self.c=customtkinter.CTkFrame(self,  fg_color = ("#EEEEEE"))
        self.contents_=customtkinter.CTkFrame(self.c,  fg_color = ("#EEEEEE"))
        # for i in range(len(self.buy_list)):
        #     self.contents_.rowconfigure(i,weight=1)
        
        self.discount_1=0 if discount_==None else discount_
        self.pd_update_()
        self.c.pack(fill='both',expand=1)

        self.discount_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.discount_frame.columnconfigure((0,1),weight=1)
        self.discount_label=customtkinter.CTkLabel(self.discount_frame,text='自訂優惠',font=("microsoft yahei", 18, 'bold'))
        
        self.discount_entry=customtkinter.CTkEntry(self.discount_frame,font=("microsoft yahei", 18, 'bold'))
        self.discount_entry.insert(customtkinter.END,self.discount_1)
        self.sum_label=customtkinter.CTkLabel(self.discount_frame,text='總計',font=("microsoft yahei", 18, 'bold'))
        self.money_label_=customtkinter.CTkLabel(self.discount_frame,text=f'{self.s-int(self.discount_1)}元',font=("microsoft yahei", 18, 'bold'))
        self.sum_label.grid(row=2,column=0,sticky='w')
        self.money_label_.grid(row=2,column=1,sticky='e')
        self.discount_label.grid(row=0,column=0,sticky='w')
        self.discount_entry.grid(row=0,column=1)
        self.discount_frame.pack(anchor='s')
        self.confirm_bt=customtkinter.CTkButton(self,text='確定下單',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 16, 'bold'), width=180)
        self.reset_bt=customtkinter.CTkButton(self,text='重設訂單',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 16, 'bold'), width=180)
        self.confirm_bt.pack(pady=10)
        self.reset_bt.pack()
        
        def discount_change(event):
            self.money_label_.configure(text=f'{self.s-int(self.discount_entry.get())}元')
        self.discount_entry.bind("<Return>",discount_change)
    def update_money(self):
        self.money_label_.configure(text=f'{self.s-int(self.discount_entry.get())}元')
    def pd_update_(self):
        self.contents_.destroy()
        self.contents_=customtkinter.CTkFrame(self.c,  fg_color = ("#EEEEEE"))
        # self.contents_.rowconfigure(len(self.buy_list),weight=1)
        self.contents_.columnconfigure((0,1,2),weight=1)
        if self.a!='':
            self.buy_list[self.a]=[self.bt_group[self.a][0].get(),self.bt_group[self.a][1]*self.bt_group[self.a][0].get()]
            if self.buy_list[self.a][0]==0:
                del self.buy_list[self.a]
                del self.bt_group[self.a]
        i=1
        self.s=0
        
        for key,value in self.buy_list.items():
            name_=customtkinter.CTkLabel(self.contents_,text=f'{key}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            number_=customtkinter.CTkLabel(self.contents_,text=f'X{value[0]:5}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            price_=customtkinter.CTkLabel(self.contents_,text=f'{value[1]}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            self.s+=value[1]
            name_.grid(row=i,column=0, padx=20, pady=3,sticky='nw')
            number_.grid(row=i,column=1, padx=20, pady=3,sticky='n')
            price_.grid(row=i,column=2, padx=20, pady=3,sticky='n')
            i+=1
        
        self.contents_.pack(fill='both',expand=1,side='top')       