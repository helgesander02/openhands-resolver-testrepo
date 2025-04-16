import customtkinter
from tkcalendar import DateEntry
from sql_app.crud import date_search,pd_Analysis
from sqlalchemy.orm import Session
from sql_app.database import engine
import pandas as pd
import tkinter.messagebox
# Data () 數據
class Data_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bt_=button_Frame(self,fg_color=("#EEEEEE"))
        self.bt_.pack(pady=40,padx=40,fill='x')
        self.Main=Main_Frame(self)
        self.Main1=Main2_Frame(self)
        self.Main.pack(pady=40,padx=40,fill='both',expand=1)
        def open_pd_analyze (event):
            self.bt_.reset_color()
            self.bt_.pd_analyze_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.forget_()
            # self.Main.pack_forget()
            # self.Main=Main2_Frame(self)#品項分析
            self.Main1.pack(pady=40,padx=40,fill='both',expand=1)
        def open_data_analyze (event):
            self.bt_.reset_color()
            self.bt_.data_analyze_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.forget_()
            # self.Main.pack_forget()
            # self.Main=Main_Frame(self)#數據分析
            self.Main.pack(pady=40,padx=40,fill='both',expand=1)
        self.bt_.pd_analyze_button.bind("<Button-1>", open_pd_analyze)
        self.bt_.data_analyze_button.bind("<Button-1>", open_data_analyze)
    def forget_(self):
        self.Main.pack_forget()
        self.Main1.pack_forget()
class Main_Frame(customtkinter.CTkFrame):#數據分析
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        a=customtkinter.CTkFrame(self)
        date_label=customtkinter.CTkLabel(a,text='日期',font=("microsoft yahei", 18, 'bold'))
        self.date1=DateEntry(a,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 10, 'bold'))
        self.date2=DateEntry(a,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 10, 'bold'))
        self.date1.set_date('2000-01-01')
        search=customtkinter.CTkButton(a,text='查詢',fg_color=("#5b5a5a"),command=self.search,font=("microsoft yahei", 18, 'bold'))
        output=customtkinter.CTkButton(a,text='輸出資料表',fg_color=("#5b5a5a"),command=self.output_excel,font=("microsoft yahei", 18, 'bold'))
        date_label.grid(row=0,column=0)
        self.date1.grid(row=0,column=1,padx=30)
        self.date2.grid(row=1,column=1,padx=30)
        search.grid(row=0,column=2)
        output.grid(row=0,column=3,padx=30)
        a.pack(anchor='w',padx=30,fill='x')
        b=customtkinter.CTkFrame(self)
        b.columnconfigure((0,1),weight=1)
        b.rowconfigure((1,3),weight=1)
        Profit_Analysis_frame=customtkinter.CTkFrame(b)
        for i in range(6):Profit_Analysis_frame.rowconfigure(i,weight=1)
        Profit_Analysis_frame.columnconfigure((0,1),weight=1)
        PAlabel1=customtkinter.CTkLabel(Profit_Analysis_frame,text='銷售總訂單數量',font=("microsoft yahei", 18, 'bold'))
        PAlabel2=customtkinter.CTkLabel(Profit_Analysis_frame,text='銷售總品項數量',font=("microsoft yahei", 18, 'bold'))
        PAlabel3=customtkinter.CTkLabel(Profit_Analysis_frame,text='銷售總購買人數量',font=("microsoft yahei", 18, 'bold'))
        PAlabel4=customtkinter.CTkLabel(Profit_Analysis_frame,text='銷售總金額',font=("microsoft yahei", 18, 'bold'))
        PAlabel5=customtkinter.CTkLabel(Profit_Analysis_frame,text='銷售優惠總額',font=("microsoft yahei", 18, 'bold'))
        PAlabel6=customtkinter.CTkLabel(Profit_Analysis_frame,text='銷售總利潤',font=("microsoft yahei", 18, 'bold'))
        PAlabel1.grid(row=0,column=0)
        PAlabel2.grid(row=1,column=0)
        PAlabel3.grid(row=2,column=0)
        PAlabel4.grid(row=3,column=0)
        PAlabel5.grid(row=4,column=0)
        PAlabel6.grid(row=5,column=0)

        self.PAlabel1_=customtkinter.CTkLabel(Profit_Analysis_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.PAlabel2_=customtkinter.CTkLabel(Profit_Analysis_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.PAlabel3_=customtkinter.CTkLabel(Profit_Analysis_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.PAlabel4_=customtkinter.CTkLabel(Profit_Analysis_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.PAlabel5_=customtkinter.CTkLabel(Profit_Analysis_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.PAlabel6_=customtkinter.CTkLabel(Profit_Analysis_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.PAlabel1_.grid(row=0,column=1)
        self.PAlabel2_.grid(row=1,column=1)
        self.PAlabel3_.grid(row=2,column=1)
        self.PAlabel4_.grid(row=3,column=1)
        self.PAlabel5_.grid(row=4,column=1)
        self.PAlabel6_.grid(row=5,column=1)

        Pick_Up_frame=customtkinter.CTkFrame(b)
        Pick_Up_frame.columnconfigure((0,1,2),weight=1)
        Pick_Up_frame.rowconfigure((0,1,2),weight=1)

        pulabel1=customtkinter.CTkLabel(Pick_Up_frame,text='現場',font=("microsoft yahei", 18, 'bold'))
        pulabel2=customtkinter.CTkLabel(Pick_Up_frame,text='宅配',font=("microsoft yahei", 18, 'bold'))
        pulabel3=customtkinter.CTkLabel(Pick_Up_frame,text='銷售量',font=("microsoft yahei", 18, 'bold'))
        pulabel4=customtkinter.CTkLabel(Pick_Up_frame,text='銷售總金額',font=("microsoft yahei", 18, 'bold'))
        self.pulabel1_=customtkinter.CTkLabel(Pick_Up_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.pulabel2_=customtkinter.CTkLabel(Pick_Up_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.pulabel3_=customtkinter.CTkLabel(Pick_Up_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.pulabel4_=customtkinter.CTkLabel(Pick_Up_frame,text='',font=("microsoft yahei", 18, 'bold'))
        pulabel1.grid(row=1,column=0)
        pulabel2.grid(row=2,column=0)
        pulabel3.grid(row=0,column=1)
        pulabel4.grid(row=0,column=2)
        self.pulabel1_.grid(row=1,column=1)
        self.pulabel2_.grid(row=1,column=2)
        self.pulabel3_.grid(row=2,column=1)
        self.pulabel4_.grid(row=2,column=2)

        path_frame=customtkinter.CTkFrame(b)
        path_frame.columnconfigure((0,1,2),weight=1)
        path_frame.rowconfigure((0,1,2),weight=1)

        palabel1=customtkinter.CTkLabel(path_frame,text='現場',font=("microsoft yahei", 18, 'bold'))
        palabel2=customtkinter.CTkLabel(path_frame,text='網站',font=("microsoft yahei", 18, 'bold'))
        palabel3=customtkinter.CTkLabel(path_frame,text='銷售量',font=("microsoft yahei", 18, 'bold'))
        palabel4=customtkinter.CTkLabel(path_frame,text='銷售總金額',font=("microsoft yahei", 18, 'bold'))
        self.palabel1_=customtkinter.CTkLabel(path_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.palabel2_=customtkinter.CTkLabel(path_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.palabel3_=customtkinter.CTkLabel(path_frame,text='',font=("microsoft yahei", 18, 'bold'))
        self.palabel4_=customtkinter.CTkLabel(path_frame,text='',font=("microsoft yahei", 18, 'bold'))
        palabel1.grid(row=1,column=0)
        palabel2.grid(row=2,column=0)
        palabel3.grid(row=0,column=1)
        palabel4.grid(row=0,column=2)
        self.palabel1_.grid(row=1,column=1)
        self.palabel2_.grid(row=1,column=2)
        self.palabel3_.grid(row=2,column=1)
        self.palabel4_.grid(row=2,column=2)

        label1=customtkinter.CTkLabel(b,text='利潤分析',font=("microsoft yahei", 18, 'bold'))
        label2=customtkinter.CTkLabel(b,text='會員分析',font=("microsoft yahei", 18, 'bold'))
        label3=customtkinter.CTkLabel(b,text='通路分析',font=("microsoft yahei", 18, 'bold'))
        label1.grid(row=0,column=0)
        Profit_Analysis_frame.grid(row=1,column=0,padx=10,pady=10,sticky='nswe',rowspan=3)
        label2.grid(row=0,column=1)
        Pick_Up_frame.grid(row=1,column=1,padx=10,pady=10,sticky='nswe')
        label3.grid(row=2,column=1)
        path_frame.grid(row=3,column=1,padx=10,pady=10,sticky='nswe')
        b.pack(anchor='w',padx=30,pady=30,fill='both',expand=1)
    def output_excel(self):
        # od_count,pd_count,p_count,sum_money,sum_discount,sum_profit,on_site,home_delivery,p_on_site,p_internet=date_search(Session(engine),self.date1.get_date(),self.date2.get_date())
        try:
            record=pd.DataFrame(
            [
                ['利潤分析','','','','會員分析',''],
                ['銷售總訂單數量',self.PAlabel1_.cget('text'),'','','銷售量','銷售總金額'],
                ['銷售總品項數量',self.PAlabel2_.cget('text'),'','現場',self.pulabel1_.cget('text'),self.pulabel2_.cget('text')],
                ['銷售總購買人數量',self.PAlabel3_.cget('text'),'','宅配',self.pulabel3_.cget('text'),self.pulabel4_.cget('text')],
                ['銷售總金額',self.PAlabel4_.cget('text'),'','','通路分析',''],
                ['銷售優惠總額',self.PAlabel5_.cget('text'),'','','銷售量','銷售總金額'],
                ['銷售總利潤',self.PAlabel6_.cget('text'),'','現場',self.palabel1_.cget('text'),self.palabel2_.cget('text')],
                ['','','','網站',self.palabel3_.cget('text'),self.palabel4_.cget('text')]
            ]
            )
            fill_path=customtkinter.filedialog.asksaveasfilename(defaultextension='.xlsx',filetypes=[('Excel活頁簿','.xlsx')],initialfile='數據分析')
            record.to_excel(fill_path,index=False)
            tkinter.messagebox.showinfo(title='匯出成功', message=f"匯出成功\n檔案位置：{fill_path}", )
        except:
            tkinter.messagebox.showinfo(title='匯出失敗', message=f"匯出失敗", )
    def search(self):
        od_count,pd_count,p_count,sum_money,sum_discount,sum_profit,on_site,home_delivery,p_on_site,p_internet=date_search(Session(engine),self.date1.get_date(),self.date2.get_date())
        self.PAlabel1_.configure(text=od_count)
        self.PAlabel2_.configure(text=pd_count)
        self.PAlabel3_.configure(text=p_count)
        self.PAlabel4_.configure(text=sum_money)
        self.PAlabel5_.configure(text=sum_discount)
        self.PAlabel6_.configure(text=sum_profit)
        self.pulabel1_.configure(text=0 if on_site[0]==None else on_site[0])
        self.pulabel2_.configure(text=0 if on_site[1]==None else on_site[1])
        self.pulabel3_.configure(text=0 if home_delivery[0]==None else home_delivery[0])
        self.pulabel4_.configure(text=0 if home_delivery[1]==None else home_delivery[1])
        
        self.palabel1_.configure(text=0 if p_on_site[0]==None else p_on_site[0])
        self.palabel2_.configure(text=0 if p_on_site[1]==None else p_on_site[1])
        self.palabel3_.configure(text=0 if p_internet[0]==None else p_internet[0])
        self.palabel4_.configure(text=0 if p_internet[1]==None else p_internet[1])
class Main2_Frame(customtkinter.CTkFrame):#品項分析
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        a=customtkinter.CTkFrame(self,fg_color=("#DDDDDD"))
        date_label=customtkinter.CTkLabel(a,text='日期',font=("microsoft yahei", 18, 'bold'))
        self.date1=DateEntry(a,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 10, 'bold'))
        self.date2=DateEntry(a,selectmode='day',date_pattern='yyyy-mm-dd',font=("microsoft yahei", 10, 'bold'))
        self.date1.set_date('2000-01-01')
        search=customtkinter.CTkButton(a,text='查詢',fg_color=("#5b5a5a"),command=self.search,font=("microsoft yahei", 18, 'bold'))
        output=customtkinter.CTkButton(a,text='輸出資料表',fg_color=("#5b5a5a"),command=self.output_excel,font=("microsoft yahei", 18, 'bold'))

        date_label.grid(row=0,column=0)
        self.date1.grid(row=0,column=1,padx=30)
        self.date2.grid(row=1,column=1,padx=30)
        output.grid(row=0,column=3,padx=30)
        search.grid(row=0,column=2)
        a.pack(anchor='w',fill='x')
        self.b=customtkinter.CTkScrollableFrame(self,fg_color=("#DDDDDD"))
        self.b.columnconfigure((0,1,2),weight=1)
        title_label=customtkinter.CTkLabel(self.b,text='品項分析',font=("microsoft yahei", 18, 'bold'))
        title_label1=customtkinter.CTkLabel(self.b,text='所有品項名稱',font=("microsoft yahei", 18, 'bold'))
        title_label2=customtkinter.CTkLabel(self.b,text='銷售量',font=("microsoft yahei", 18, 'bold'))
        title_label3=customtkinter.CTkLabel(self.b,text='銷售總金額',font=("microsoft yahei", 18, 'bold'))
        title_label.grid(row=0,column=0,sticky='w')
        title_label1.grid(row=1,column=0)
        title_label2.grid(row=1,column=1)
        title_label3.grid(row=1,column=2)
        self.b.pack(fill='both',expand=1)
    def output_excel(self):
        try:
            pd_=pd_Analysis(Session(engine),self.date1.get_date(),self.date2.get_date())
            c1=[]
            c2=[]
            for i in list(pd_.values()):
                c1.append(i[0])
                c2.append(i[1])
            a=pd.DataFrame(
                {
                    '所有品項名稱':list(pd_.keys()),
                    '銷售量':c1,
                    '銷售總金額':c2
                }
            )
            fill_path=customtkinter.filedialog.asksaveasfilename(defaultextension='.xlsx',filetypes=[('Excel活頁簿','.xlsx')],initialfile='品項分析')
            a.to_excel(fill_path,index=False)
            tkinter.messagebox.showinfo(title='匯出成功', message=f"匯出成功\n檔案位置：{fill_path}", )
        except:
            tkinter.messagebox.showinfo(title='匯出失敗', message=f"匯出失敗", )
    def search(self):
        self.b.pack_forget()
        self.b.destroy()
        self.b=customtkinter.CTkScrollableFrame(self,fg_color=("#DDDDDD"))
        self.b.columnconfigure((0,1,2),weight=1)
        title_label=customtkinter.CTkLabel(self.b,text='品項分析',font=("microsoft yahei", 18, 'bold'))
        title_label1=customtkinter.CTkLabel(self.b,text='所有品項名稱',font=("microsoft yahei", 18, 'bold'))
        title_label2=customtkinter.CTkLabel(self.b,text='銷售量',font=("microsoft yahei", 18, 'bold'))
        title_label3=customtkinter.CTkLabel(self.b,text='銷售總金額',font=("microsoft yahei", 18, 'bold'))
        title_label.grid(row=0,column=0,sticky='w')
        title_label1.grid(row=1,column=0)
        title_label2.grid(row=1,column=1)
        title_label3.grid(row=1,column=2)
        pd=pd_Analysis(Session(engine),self.date1.get_date(),self.date2.get_date())
        l=2
        for key,value in pd.items():
            self.b.rowconfigure(l,weight=1)
            pd1=customtkinter.CTkLabel(self.b,text=key,font=("microsoft yahei", 18, 'bold'))
            pd2=customtkinter.CTkLabel(self.b,text=value[0],font=("microsoft yahei", 18, 'bold'))
            pd3=customtkinter.CTkLabel(self.b,text=value[1],font=("microsoft yahei", 18, 'bold'))
            pd1.grid(row=l,column=0)
            pd2.grid(row=l,column=1)
            pd3.grid(row=l,column=2)
            l+=1
        self.b.pack(fill='both',expand=1)
class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #5b5a5a
        self.data_analyze_button = customtkinter.CTkButton(self, text="數據分析", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.data_analyze_button.grid(row=0, column=5,padx=30)
        self.pd_analyze_button = customtkinter.CTkButton(self, text="品項分析", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.pd_analyze_button.grid(row=0, column=6,padx=30)


    def reset_color(self):
        self.data_analyze_button.configure(fg_color = ("#EEEEEE"),text_color='black')
        self.pd_analyze_button.configure(fg_color = ("#EEEEEE"),text_color='black')