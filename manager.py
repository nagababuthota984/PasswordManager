import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import os
import os.path as p
from tkinter import messagebox
import hashlib
import json
import tkinter.ttk as ttk


class Storage :
    password = None
    username = None
    data=None
    def setData(self,d):
        Storage.data=d
    def setUsername(self,us):
        Storage.username = us
    def setPassword(self,pw):
        Storage.password = pw
    def getUsername(self):
        return Storage.username
    def getPassword(self):
        return Storage.password    
    def getData(self):
        return Storage.data
    @staticmethod
    def writeData(data):
        path=os.getcwd()+'/SAFE/'+Storage.username+'.json'
        f=open(path,'w')
        data=json.dumps(data)
        f.write(data)
        f.close()
    
    @staticmethod
    def sortDict(data):
        l=list(data[1].items())
        l.sort()
        data[1]=dict(l)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.createSafe()
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Calibri', size=18, weight="bold")
        self.geometry("620x450+650+150")
        self.resizable(0,0)
        

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Register, Login, ShowFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    def createSafe(self):
        self.path=os.getcwd()+'/SAFE/'
        if p.exists(self.path):
            pass
        else:
            os.mkdir(self.path)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Password Manager!", font=controller.title_font, bg = "grey", fg = "white")
        
        self.register=tk.Button(self)
        self.register.place(relx=0.163,rely=0.374,height=43,width=156)
        self.register.configure(text='Register',command=lambda : controller.show_frame("Register"))
        self.lab1=tk.Label(self)
        self.lab1.place(relx=0.176,rely=0.308,height=26,width=137)
        self.lab1.configure(text="New User? Register.")
        
        
        self.login=tk.Button(self)
        self.login.place(relx=0.600,rely=0.374,height=43,width=156)
        self.login.configure(text="Login",command =  lambda : controller.show_frame("Login"))
        self.lab2=tk.Label(self)
        self.lab2.place(relx=0.660,rely=0.308,width=76,height=26)
        self.lab2.configure(text='Login here')

class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Give your username and password!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        
        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.197, rely=0.156, height=26, width=83)
        self.Label1.configure(text='''Username :''')
        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.205, rely=0.247, height=26, width=78)
        self.Label2.configure(text='''Password :''')
        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.182, rely=0.336, height=26, width=92)
        self.Label3.configure(text='''Enter again :''')
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.629, rely=0.511, height=43, width=116)
        self.Button1.configure(text='''Register''',command=self.createUser)
        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.629, rely=0.64, height=43, width=116)
        self.Button2.configure(text='''Back to Login''',command = lambda : controller.show_frame("Login"))
        
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.355, rely=0.16,height=24, relwidth=0.329)
        self.Entry1.configure(background="white")
        self.Entry1.configure(insertbackground="black")
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.355, rely=0.251,height=24, relwidth=0.329)
        self.Entry2.configure(background="white")
        self.Entry2.configure(insertbackground="black",show="*")
        self.Entry3 = tk.Entry(self)
        self.Entry3.place(relx=0.355, rely=0.344,height=24, relwidth=0.329)
        self.Entry3.configure(insertbackground="black",show="*")
    def createUser(self):
        username=self.Entry1.get()
        p1=self.Entry2.get()
        p2=self.Entry3.get()
        if(p1!=p2):
            messagebox.showerror('Error',"Password did not match")
        else:
            password=(p1).encode('utf-8')
            hashed_password=hashlib.sha512(password).hexdigest()
            l=[]
            l.append(hashed_password)
            l.append(dict())
            path=os.getcwd()+'/SAFE/'+username+'.json'
            if p.exists(path):
                messagebox.showinfo('exists','An account with similar user name already exists\nPlease go to login page')
            else:
                f=open(path,'w')
                data=json.dumps(l,indent=4)
                f.write(data)
                f.close()
                messagebox.showinfo('Done','please go to login page')

class Login(tk.Frame):
    flag = False
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
  
        label = tk.Label(self, text="Verify that it's you", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        
        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.21, rely=0.333, height=26, width=78)
        self.Label2.configure(text='''Password :''')
        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.194, rely=0.244, height=26, width=92)
        self.Label3.configure(text='''Username :''')
  
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.602, rely=0.511, height=43, width=115)
        self.Button1.configure(text='''Login''',command=lambda : self.verify(controller))
        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.180,rely=0.511,height=43,width=115)
        self.Button2.configure(text="Back",command = lambda : controller.show_frame("StartPage"))
        
        #global Entry2,Entry3
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.355, rely=0.251,height=24, relwidth=0.329)
        self.Entry2.configure(background="white")

        self.Entry3 = tk.Entry(self)
        self.Entry3.place(relx=0.355, rely=0.344,height=24, relwidth=0.329)
        self.Entry3.configure(background="white",show="*")
    
    def verify(self,controller):
        us = self.Entry2.get()
        pw = self.Entry3.get()
        pw=pw.encode('utf-8')
        s = Storage()
        s.setUsername(us)
        s.setPassword(pw)
        path=os.getcwd()+'/SAFE/'+us+'.json'
        if p.exists(path):
            file=open(path,'r')
            f=file.read()
            file.close()
            data=json.loads(f)
            has_pw=hashlib.sha512(pw).hexdigest()
            if has_pw==data[0]:
                s.setData(data)
                Login.flag = True
                controller.show_frame('ShowFrame')
            else:
                messagebox.showinfo('Error','Incorrect Password')
        else:
            messagebox.showinfo('MisMatch',"Incorrect username")
        self.Entry3.delete(0,tk.END)
        self.Entry2.delete(0,tk.END)

class ShowFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        s=Storage()

        self.data=s.getData()
        self.s1=ttk.Treeview(self)
        self.s1.place(relx=0.026,rely=0.036,relheight=0.923,relwidth=0.658)
        self.s1.configure(columns='Username')
        self.s1.heading("#0",text="Website")
        self.s1.heading("#0",anchor="w")
        self.s1.column("#0",width="243")
        self.s1.column("#0",minwidth="20")
        self.s1.column("#0",stretch="1")
        self.s1.column("#0",anchor="w")
        self.s1.heading("Username",text="Username")
        self.s1.heading("Username",anchor="w")
        self.s1.column("#0",width="233")
        self.s1.column("Username",minwidth="20")
        self.s1.column("Username",stretch="1")
        self.s1.column("Username",anchor="w")
        self.Button1_0 = tk.Button(self)
        self.Button1_0.place(relx=0.761, rely=0.100, height=33, width=131) 
        self.Button1_0.configure(pady="0")
        self.Button1_0.configure(text='''Add''',command=self.addWindow)
        
        self.Button1_1 = tk.Button(self)
        self.Button1_1.place(relx=0.761, rely=0.420, height=33, width=131)
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Delete''') 
        
        self.Button1_2 = tk.Button(self)
        self.Button1_2.place(relx=0.761, rely=0.250, height=33, width=131)
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Edit''')
        self.Button1_3 = tk.Button(self)
        self.Button1_3.place(relx=0.761,rely=0.570,height=33,width=133)
        self.Button1_3.configure(text="Logout",command=lambda : controller.show_frame("StartPage"))
        self.Button1_4 = tk.Button(self)
        self.Button1_4.place(relx=0.751,rely=0.7100,height=33,width=150)
        self.Button1_4.configure(text='''Change Master password''',command= self.changeMasterPassword)
        self.open=False
        self.bind('<Enter>',self.loadTreeview())
        vsb = ttk.Scrollbar(self.s1, orient="vertical", command=self.s1.yview)
        self.s1.configure(yscrollcommand=vsb.set)
        vsb.pack(side='right',fill='y')
    def loadTreeview(self):
        p=Storage()
        self.data=p.getData()
        for i,j in self.data[1].items():
            self.s1.insert('','end',text=i)
            self.s1.insert('','end',text=j)
    
    
    
    
    
    def changeMasterPassword(self):
        if not self.open:
            sobj = Storage()
            user = sobj.getUsername()
            self.open=True
            self.cha=tk.Toplevel(self)
            self.cha.title("Change the master password")
            self.cha.geometry("562x355+321+137")
            self.cha.resizable(False,False)
            self.cha.protocol('WM_DELETE_WINDOW', self.closeCha)
            b2 = tk.Button(self.cha)
            b2.place(relx=0.726, rely=0.691, height=36, width=106)
            b2.configure(text='''Cancel''', command= self.closeCha)
            b1 = tk.Button(self.cha)
            b1.place(relx=0.443, rely=0.691, height=36, width=106)
            b1.configure(text='''Change''',command=self.changeAndSave )
    
            self.entry2 = tk.Entry(self.cha)
            self.entry2.place(relx=0.39, rely=0.24, height=24, relwidth=0.356)
            self.entry2.configure(background="white")
            self.entry2.insert(0,user)
            self.entry3 = tk.Entry(self.cha)
            self.entry3.place(relx=0.391, rely=0.373, height=24, relwidth=0.356)
            self.entry3.configure(background="white", show="*")
            self.entry4 = tk.Entry(self.cha)
            self.entry4.place(relx=0.391, rely=0.512, height=24, relwidth=0.356)
            self.entry4.configure(background="white", show="*")

            la2 = tk.Label(self.cha)
            la2.place(relx=0.222, rely=0.235, height=26, width=92)
            la2.configure(text='''Username :''')
            la3 = tk.Label(self.cha)
            la3.place(relx=0.242, rely=0.371, height=26, width=75)
            la3.configure(text='''Password :''')
            la4 = tk.Label(self.cha)
            la4.place(relx=0.249, rely=0.507, height=26, width=70)
            la4.configure(text='''Re-Enter :''')

    def close(self):
        self.open=False
        self.win.destroy()
    def closeCha(self):
        self.open=False
        self.cha.destroy()
    def changeAndSave(self):
        p= Storage()
        self.data=p.getData()
        self.user = p.getUsername()
        
            
        if self.entry3.get()==self.entry4.get():
            if self.entry2.get()!=self.user:
                new_user = self.entry2.get()
                path1 = os.getcwd()+"/SAFE/"+self.user+'.json'
                path2 = os.getcwd()+"/SAFE/"+new_user+'.json'
                os.rename(path1,path2)
                p.setUsername(new_user)
            pas=self.entry3.get()
            pas=pas.encode('utf-8')
            pas=hashlib.sha512(pas).hexdigest()
            self.data[0]=pas 
            p.setData(self.data)
            Storage.writeData(self.data)
            messagebox.showinfo('Success',"Master password has been successfully changed!")
            self.closeCha()
        else:
            messagebox.showinfo('Mismatch','the password did not match')

    def saveAndClose(self):
        p= Storage()
        self.data = p.getData()
        website=self.en1.get()
        username=self.en2.get()
        password=self.en3.get()
        re_entry=self.en4.get()
        if len(password)+len(username)+len(website)>3 and password==re_entry :
            self.data[1][website]=[username,password]
            Storage.writeData(self.data)
            self.close()
        else:
            if password!=re_entry:
                messagebox.showinfo('Mismatch','paswords did not match')
            else:
                messagebox.showinfo('unfilled entries','Please make sure you have Entered all the fields')

    def addWindow(self):

        if not self.open:
            self.open=True
            self.win = tk.Toplevel(self)
            self.win.title('Add the password')
            self.win.geometry("562x375+321+157")
            self.win.resizable(False,False)
            self.win.protocol('WM_DELETE_WINDOW',self.close)

            self.b2 = tk.Button(self.win)
            self.b2.place(relx=0.726,rely=0.691,height=36,width=106)
            self.b2.configure(text = '''Cancel''',command =   self.close)
            self.b1 = tk.Button(self.win)
            self.b1.place(relx=0.443,rely=0.691,height=36,width=106)
            self.b1.configure(text = '''Add''',command = self.saveAndClose)
            
            self.en1 = tk.Entry(self.win)
            self.en1.place(relx=0.391,rely=0.107,relwidth=0.356,height=24)
            self.en1.configure(background = "white")
            self.en2 = tk.Entry(self.win)
            self.en2.place(relx=0.39,rely=0.24,height=24,relwidth=0.356)
            self.en2.configure(background="white")
            self.en3 = tk.Entry(self.win)
            self.en3.place(relx=0.391,rely=0.373,height=24,relwidth=0.356) 
            self.en3.configure(background = "white",show="*")
            self.en4 = tk.Entry(self.win)
            self.en4.place(relx=0.391,rely=0.512,height=24,relwidth=0.356)  
            self.en4.configure(background = "white",show="*")

            self.la1 = tk.Label(self.win)
            self.la1.place(relx=0.253,rely=0.101,height=26,width=67) 
            self.la1.configure(text='''Website :''')
            self.la2 = tk.Label(self.win)
            self.la2.place(relx=0.222,rely=0.235,height=26,width=92)
            self.la2.configure(text='''Username :''')  
            self.la3 = tk.Label(self.win)
            self.la3.place(relx=0.242,rely=0.371,height=26,width=75)
            self.la3.configure(text='''Password :''')
            self.la4 = tk.Label(self.win)
            self.la4.place(relx=0.249,rely=0.507,height=26,width=70)    
            self.la4.configure(text='''Re-Enter :''')
            
       

        


if __name__ == "__main__":
    app = SampleApp()
    
    app.mainloop()