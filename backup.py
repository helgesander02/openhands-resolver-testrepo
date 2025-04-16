import os
import time
import customtkinter
from sql_app.database import engine,Base,sessionmaker
import tkinter as tk
import tkinter.messagebox 
class backup_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bt_frame=customtkinter.CTkFrame(self,fg_color='#EEEEEE')

        self.backup_bt=customtkinter.CTkButton(self.bt_frame,text="備份",command=self.backup)
        
        self.restore_bt=customtkinter.CTkButton(self.bt_frame,text='恢復',command=self.restore)

        self.backup_bt.pack(side='left',padx=20)
        self.restore_bt.pack(side='left',padx=20)
        self.bt_frame.pack(pady=50,padx=20,anchor='n',fill='x')
            # DB_HOST = 'localhost'
            # DB_USER = 'postgres'
            # DB_PASS = 'admin'
            # DB_NAME = 'postgres'
            # DB_HOST = 'localhost'
            # DB_USER = 'postgres'
            # DB_PASS = '1234'
            # DB_NAME = 'first_data'
    def backup(self):
        try:
            b=os.getcwd()#原本的路徑
            DB_HOST = 'localhost'
            DB_USER = 'postgres'
            DB_PASS = 'admin'
            DB_NAME = 'postgres'
            

            TIMESTAMP = time.strftime('%Y-%m-%d-%H-%M-%S')
            BACKUP_FILE = DB_NAME + '_' + TIMESTAMP + '.sql'
            BACKUP_PATH = customtkinter.filedialog.asksaveasfilename(defaultextension='.sql',filetypes=[('自訂檔','.sql')],initialfile=f'{BACKUP_FILE}')
            if BACKUP_PATH=="":
                raise
            a="C://Program Files//PostgreSQL//15//bin"
            os.chdir(a)
            BACKUP_CMD = f"pg_dump --dbname=postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME} > {BACKUP_PATH} "
            os.system(BACKUP_CMD)
            os.chdir(b)
            tkinter.messagebox.showinfo(title='成功', message="備份成功", )
        except:
            tkinter.messagebox.showinfo(title='失敗', message="備份失敗", )
        # os.path.join(BACKUP_PATH, BACKUP_FILE)
    def restore(self):
        try:
            b=os.getcwd()#原本的路徑

            DB_HOST = 'localhost'
            DB_USER = 'postgres'
            DB_PASS = 'admin'
            DB_NAME = 'postgres'
            restore_PATH = customtkinter.filedialog.askopenfilename()
            if restore_PATH=="":
                raise
            sessionmaker.close_all()
            Base.metadata.drop_all(engine)
            a="C://Program Files//PostgreSQL//15//bin"
            os.chdir(a)
            restore_CMD=f'psql --dbname=postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME} -f {restore_PATH}'
            os.system(restore_CMD)
            os.chdir(b)
            tkinter.messagebox.showinfo(title='成功', message="恢復成功", )
        except:
            tkinter.messagebox.showinfo(title='失敗', message="恢復失敗", )