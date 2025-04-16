import tkinter as tk
import customtkinter
from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.crud import get_user,save_change,add_data
from sql_app.crud import *
from tkinter import *
from PIL import Image
import pandas as pd
import os
from typing import Union
from typing import Callable
import tkinter.messagebox 
# Menber () 會員
class Menber_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.edit_photo = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\pencil.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\pencil.png"),
                                  size=(30, 30))
        self.delete_photo = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\close.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\close.png"),
                                  size=(30, 30))
        self.image = customtkinter.CTkImage(light_image=Image.open(f"{os.getcwd()}\\image\\search.png"),
                                  dark_image=Image.open(f"{os.getcwd()}\\image\\search.png"),
                                  size=(30, 30))           
        self.user_id=''
        # self.columnconfigure((0,1,2,3),weight=1)
        search_=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"),height=150)
        # search_.columnconfigure((1),weight=1)
        # search_label=customtkinter.CTkLabel(search_,text='會員查詢',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        # search_label.pack(side='left')
        self.search=customtkinter.CTkEntry(search_,fg_color = ("#EEEEEE"),width=300,placeholder_text='電話查詢',text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.search_bt=customtkinter.CTkButton(search_, text="", width=40,
                                                        hover=False,image=self.image,fg_color = "#DDDDDD",
                                                        command=self.member_search_click)
        
        self.search.pack(side='left',padx=40)
        self.search_bt.pack(side='left')
        import_bt=customtkinter.CTkButton(search_,text='匯入資料',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.import_date)
        # ,command=self.open_edit_toplevel
        export_bt=customtkinter.CTkButton(search_,text='匯出資料',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.export_date)       
        add_bt=customtkinter.CTkButton(search_,text='新增',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.open_add_toplevel)
        self.page_=FloatSpinbox(self)
        
        export_bt.pack(side='right',padx=10)
        import_bt.pack(side='right',padx=10)
        add_bt.pack(side='right',padx=10)
        search_.pack_propagate(0)
        search_.pack(anchor='n',fill='both',padx=50,pady=50)
        self.choose_frame=customtkinter.CTkFrame(self)
        self.choose_label=customtkinter.CTkLabel(self.choose_frame,text='未選擇',width=100)
        self.choose_label.pack(side='left',padx=10)
        self.choose_label2=customtkinter.CTkLabel(self.choose_frame,text='',width=100)
        self.choose_label2.pack(side='left',padx=10)
        self.choose_bt=customtkinter.CTkButton(self.choose_frame,text='訂購',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'))
        self.choose_bt.pack(side='left')
        self.choose_frame.pack(anchor='w',padx=50)

        self.fake=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.history_frame=customtkinter.CTkScrollableFrame(self.fake,fg_color = ("#DDDDDD"))
        self.fake.pack(fill='both',expand=1)
        # self.history_frame.pack(fill='both',expand=1,padx=100)
        self.page_.pack(pady=20)
        self.member_search_click()
        
        
        self.toplevel_window = None
        def page_search(event):
            self.member_search_click()
        self.page_.add_button.bind("<Button-1>", page_search)
        self.page_.subtract_button.bind("<Button-1>", page_search)
        self.page_.entry.bind('<Return>',page_search)
    def import_date(self):
        try:
            file_path = customtkinter.filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
            df=pd.read_excel(file_path)
            for index,row in df.iterrows():
                add_data(db=Session(engine),name=row['Name'],address=row['Address'],remark=row['Remark'],phone=row['Phone'])
            self.member_search_click()
            tkinter.messagebox.showinfo(title='新增成功', message="新增成功", )
            
        except Exception as e:
            print(e)
            tkinter.messagebox.showinfo(title='新增成功', message="新增失敗", )
    def export_date(self):
        try:
            fill_path=customtkinter.filedialog.asksaveasfilename(defaultextension='.xlsx',filetypes=[('Excel活頁簿','.xlsx')],initialfile='成員')
            query = 'SELECT * FROM Member'
            df = pd.read_sql_query(query, engine)
            df.to_excel(fill_path, index=False)
            # current_directory = os.getcwd()
            tkinter.messagebox.showinfo(title='匯出成功', message=f"匯出成功\n檔案位置：{fill_path}", )              
        except Exception as e:
            tkinter.messagebox.showinfo(title='匯出失敗', message=f"匯出失敗{e}", )
    def member_search_click(self):
        self.history_frame.pack_forget()
        self.history_frame.destroy()
        self.history_frame=customtkinter.CTkScrollableFrame(self.fake,fg_color = ("#DDDDDD"))
        self.history_frame.columnconfigure((2),weight=4)
        self.history_frame.columnconfigure((0,1,3,4,5,6),weight=1)
        
        member,page_max_=member_search(db=Session(engine),search=self.search.get(),page=1 if self.page_.get()==None else self.page_.get())
        self.page_.page_max.configure(text=f'/{page_max_//20+1}')
        order_n=customtkinter.CTkLabel(self.history_frame,text='會員姓名',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n1=customtkinter.CTkLabel(self.history_frame,text='手機',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n2=customtkinter.CTkLabel(self.history_frame,text='地址',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n3=customtkinter.CTkLabel(self.history_frame,text='備註',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n4=customtkinter.CTkLabel(self.history_frame,text='編輯',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n5=customtkinter.CTkLabel(self.history_frame,text='刪除',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n6=customtkinter.CTkLabel(self.history_frame,text='訂購',text_color='black',font=("microsoft yahei", 18, 'bold'))
        # a=customtkinter.CTkFrame(self.history_frame_title,width=20,height=5,fg_color= ("#EEEEEE"))
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2,sticky='w')
        order_n3.grid(row=0,column=3,sticky='w')
        order_n4.grid(row=0,column=4,sticky='w')
        order_n5.grid(row=0,column=5,sticky='w')
        order_n6.grid(row=0,column=6,sticky='w')
        def gen_cmd1(i):return lambda:self.edit_(i)
        def gen_cmd(i):return lambda:self.delete(i)
        def go_order(i,l):return lambda:self.go_order_(i,l)
        
        i=1
        for k in member:
            a1=customtkinter.CTkLabel(self.history_frame,text=f'{k.Name.strip()}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            a2=customtkinter.CTkLabel(self.history_frame,text=f'{k.Phone.strip()}',text_color='black',font=("microsoft yahei", 18, 'bold'))
            a3=customtkinter.CTkLabel(self.history_frame,text=f'{k.Address.strip()}',text_color='black',font=("microsoft yahei", 18, 'bold'))         
            a4=customtkinter.CTkLabel(self.history_frame,text=' ' if k.Remark==None or k.Remark=='NaN' else f'{k.Remark.strip()}',text_color='black',font=("microsoft yahei", 18, 'bold'))            
            a5=customtkinter.CTkButton(self.history_frame,width=30,image=self.edit_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd1(k.Phone))
            a6=customtkinter.CTkButton(self.history_frame,width=30,image=self.delete_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd(k.ID))
            a7=customtkinter.CTkButton(self.history_frame,width=30,text='選擇',fg_color=("#5b5a5a"),text_color='white',command=go_order(k.Phone,k.Name))
            a1.grid(row=i,column=0,sticky='w')
            a2.grid(row=i,column=1,sticky='w')
            a3.grid(row=i,column=2,sticky='w')
            a4.grid(row=i,column=3,sticky='w')
            a5.grid(row=i,column=4,sticky='w')
            a6.grid(row=i,column=5,sticky='w')
            a7.grid(row=i,column=6,sticky='w')
            i+=1
        self.history_frame.pack(fill='both',expand=1,padx=50)
    def go_order_(self,i,l):
        self.choose_label.configure(text=f'{i}')
        self.choose_label2.configure(text=f'{l}')
    def open_add_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = add_ToplevelWindow(self)
            self.toplevel_window.confirm_bt.configure(command=self.confirm_add)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def edit_(self,i):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = edit_ToplevelWindow(self,user_id=i)
            self.toplevel_window.confirm_bt.configure(command=self.confirm_edit)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def delete(self,i):
        del_member(db=Session(engine),id_=i)
        self.member_search_click()
    def confirm_edit(self):
        save_change(Session(engine),name=self.toplevel_window.edit_entry_n.get(),phone=self.toplevel_window.edit_entry_n1.get(),address=self.toplevel_window.edit_entry_n2.get(1.0,END),remark=self.toplevel_window.edit_entry_n3.get(1.0,END),user_id=self.toplevel_window.user_id)
        self.member_search_click()
        self.toplevel_window.destroy()
    def confirm_add(self):
        try:
            add_data(Session(engine),name=self.toplevel_window.edit_entry_n.get(),phone=self.toplevel_window.edit_entry_n1.get(),address=self.toplevel_window.edit_entry_n2.get(1.0,END),remark=self.toplevel_window.edit_entry_n3.get(1.0,END))
            self.toplevel_window.destroy()
            self.member_search_click()
            tkinter.messagebox.showinfo(title='新增成功', message="新增成功", )
        except:
            tkinter.messagebox.showinfo(title='新增失敗', message="新增失敗", )        
class edit_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,user_id:str, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x500")
        
        try:
            self.title('編輯會員')
            self.user_id=user_id
            self.columnconfigure((0,1),weight=1)
            self.rowconfigure((2,3),weight=2)
            user=get_user(Session(engine),self.user_id)
            edit_n=customtkinter.CTkLabel(self,text='姓名',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n1=customtkinter.CTkLabel(self,text='電話',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n2=customtkinter.CTkLabel(self,text='地址',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n3=customtkinter.CTkLabel(self,text='備註',text_color='black',font=("microsoft yahei", 18, 'bold'))
            self.edit_entry_n=customtkinter.CTkEntry(self)
            self.edit_entry_n1=customtkinter.CTkEntry(self)
            self.edit_entry_n2=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            self.edit_entry_n3=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            
            self.edit_entry_n.insert(END,f'{user.Name}')
            self.edit_entry_n1.insert(END,f'{user.Phone}')
            self.edit_entry_n2.insert(END,f'{user.Address}')
            self.edit_entry_n3.insert(END,f'{user.Remark}')
            self.cancel_bt=customtkinter.CTkButton(self,text='取消',fg_color=("#5b5a5a"),command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
            self.confirm_bt=customtkinter.CTkButton(self,text='確定更改',fg_color=("#5b5a5a"),font=("microsoft yahei", 18, 'bold'))
            self.cancel_bt.grid(row=4,column=0,sticky='e',padx=30,pady=10)
            self.confirm_bt.grid(row=4,column=1,sticky='e',padx=30,pady=10)

            edit_n.grid(row=0,column=0)
            edit_n1.grid(row=1,column=0)
            edit_n2.grid(row=2,column=0)
            edit_n3.grid(row=3,column=0)
            self.edit_entry_n.grid(row=0,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n1.grid(row=1,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n2.grid(row=2,column=1,sticky='nsew',padx=10,pady=10)
            self.edit_entry_n3.grid(row=3,column=1,sticky='nsew',padx=10,pady=10)
        except Exception as e:
            print(e)
            self.title('錯誤')
            error_label=customtkinter.CTkLabel(self,text='查詢失敗，請回上層進行查詢',font=("microsoft yahei", 18, 'bold'))
            error_bt=customtkinter.CTkButton(self,text='回上層',command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
            error_label.pack(anchor='center',fill='y',pady=30)
            error_bt.pack(anchor='center',fill='y',pady=10)
    def cancel_click(self):
        self.destroy()
class add_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x500")
        try:
            self.title('新增會員')
            self.columnconfigure((0,1),weight=1)
            self.rowconfigure((3,4),weight=2)
            
            edit_n=customtkinter.CTkLabel(self,text='姓名',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n1=customtkinter.CTkLabel(self,text='電話',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n2=customtkinter.CTkLabel(self,text='地址',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n3=customtkinter.CTkLabel(self,text='備註',text_color='black',font=("microsoft yahei", 18, 'bold'))
            self.edit_entry_n=customtkinter.CTkEntry(self)
            self.edit_entry_n1=customtkinter.CTkEntry(self)
            self.edit_entry_n2=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            self.edit_entry_n3=customtkinter.CTkTextbox(self,border_color='black',border_width=2)

            self.cancel_bt=customtkinter.CTkButton(self,text='取消',command=self.cancel_click,fg_color=("#5b5a5a"),font=("microsoft yahei", 18, 'bold'))
            self.confirm_bt=customtkinter.CTkButton(self,text='確定新增',fg_color=("#5b5a5a"),font=("microsoft yahei", 18, 'bold'))
            self.cancel_bt.grid(row=5,column=0,sticky='e',padx=30,pady=10)
            self.confirm_bt.grid(row=5,column=1,sticky='e',padx=30,pady=10)
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
            error_bt=customtkinter.CTkButton(self,text='回上層',command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
            error_label.pack(anchor='center',fill='y',pady=30)
            error_bt.pack(anchor='center',fill='y',pady=10)
    def cancel_click(self):
        self.destroy()


class FloatSpinbox(customtkinter.CTkFrame):
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