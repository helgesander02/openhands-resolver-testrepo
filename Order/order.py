#-*- coding: utf-8 -*-
import customtkinter
from tkinter import *
from .orderedit import *
from .orderfinish import *
from .orderinput import *
from .account import *
# Order () 訂單
import tkinter.messagebox 
class Order_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.bt_frame=button_Frame(self,  fg_color = ("#EEEEEE") ,)
        self.bt_frame.pack(pady=40,padx=40,anchor='nw')
        self.input_order_=input_order(self,  fg_color = ("#DDDDDD"))
        self.input_order_1=edit_order(self,  fg_color = ("#DDDDDD") )
        self.input_order_2=finish_frame(self,  fg_color = ("#DDDDDD"))
        self.input_order_.pack(fill='both',expand=1,padx=40,pady=40,anchor='nw')
        self.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
        def input_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.forget_()
            self.input_order_.update_product()
            self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
            # self.input_order_.pack_forget()
            # self.input_order_=input_order(self,  fg_color = ("#DDDDDD"))
            # self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        def edit_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.edit_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.forget_()
            self.input_order_1.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
            # self.input_order_.pack_forget()
            # self.input_order_=edit_order(self,  fg_color = ("#DDDDDD") )
            # self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        def finish_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.finish_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.forget_()
            self.input_order_2.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
            self.input_order_2.search.refresh()
            self.input_order_2.ac.pack_forget()
            self.input_order_2.search.pack(fill='both',side='left',expand=1,padx=15,pady=5)
            # self.input_order_.pack_forget()
            # self.input_order_=finish_frame(self,  fg_color = ("#DDDDDD"))
            # self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        self.bt_frame.input_button.bind("<Button-1>", input_button_click)
        self.bt_frame.edit_button.bind("<Button-1>", edit_button_click)
        self.bt_frame.finish_button.bind("<Button-1>", finish_button_click)
    def forget_(self):
        self.input_order_.pack_forget()
        self.input_order_1.pack_forget()
        self.input_order_2.pack_forget()



class finish_frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.search=finish_search_fame(self,fg_color = ("#DDDDDD"))
        self.search.pack(fill='both',side='left',expand=1,padx=15,pady=5)
        self.search.ac.configure(command=lambda:self.test('123'))
        self.ac=acount(self,selected={1:1},fg_color = ("#DDDDDD"))
    def test(self,a):
        if len(self.search.selected_pd)!=0:
            selected=self.search.selected_pd
            self.search.pack_forget()
            self.ac.destroy()
            self.ac=acount(self,selected=selected,fg_color = ("#DDDDDD"))
            self.ac.pack(fill='both',side='left',expand=1,padx=15,pady=5)
            # self.search=acount(self,selected=selected,fg_color = ("#DDDDDD"))
            # self.search.pack(fill='both',side='left',expand=1,padx=15,pady=5)
        else:
            tkinter.messagebox.showinfo(title='失敗', message="請勾選想要入帳的訂單", )


class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #5b5a5a
        self.input_button = customtkinter.CTkButton(self, text="輸入訂單", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.input_button.grid(row=0, column=5,padx=30)
        self.edit_button = customtkinter.CTkButton(self, text="編輯與查詢", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.edit_button.grid(row=0, column=6,padx=30)

        self.finish_button = customtkinter.CTkButton(self, text="完成訂單", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.finish_button.grid(row=0, column=7,padx=30)
    def reset_color(self):
        self.input_button.configure(fg_color = ("#EEEEEE"),text_color='black')
        self.edit_button.configure(fg_color = ("#EEEEEE"),text_color='black')
        self.finish_button.configure(fg_color = ("#EEEEEE"),text_color='black')