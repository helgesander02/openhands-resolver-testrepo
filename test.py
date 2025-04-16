from sqlalchemy.orm import Session
from sqlalchemy import text
from sql_app.database import engine,Base
from sql_app.crud import *
import pandas as pd
import os
import customtkinter
import os
from PIL import Image
from tkinter import *
import datetime
import tkinter as tk
import os
import time
import sqlalchemy as sa
import tkinter.messagebox 
# a=pd_Analysis(Session(engine),'2000-01-01','2023-09-20')
# pd_=pd_Analysis(Session(engine),'2000-01-01','2023-09-20')
# print(list(pd_.values())[0])
# for i in list(pd_.values()):
#     print(i)
# tk._test()
# tk.messagebox.showinfo(title='新增失敗', message="新增失敗", )
# tkinter.messagebox.showinfo(title='新增失敗', message="新增失敗", )
# import os
# Base.metadata.drop_all(engine)
# DB_HOST = 'localhost'
# DB_USER = 'postgres'
# DB_PASS = '1234'
# DB_NAME = 'new'
# restore_PATH = customtkinter.filedialog.askopenfilename()
# restore_CMD=f'psql --dbname=postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME} -f {restore_PATH}'
# os.system(restore_CMD)
# from tkinter import *

# # Create an instance of tkinter frame
# win = Tk()

# # Set the size of the tkinter window
# win.geometry("700x350")

# def disable_entry():
#    entry.config(state= "disabled")

# # Create an entry widget
# entry=Entry(win, width= 40, font= ('Helvetica 16'))
# entry.insert(0,'abccc')
# entry.config(state= "disabled")
# entry.pack(pady=20)


# # Create a button
# button=Button(win, text="Disable Entry", font=('Arial', 12), command=disable_entry)
# button.pack()

# win.mainloop()