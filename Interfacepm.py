import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import os
import os.path as p
from tkinter import messagebox
import hashlib
import json
boomusername=''

class Storage :
    password = None
    username = None
    def setUsername(self,us):
        Storage.username = us
    def setPassword(self,pw):
        Storage.password = pw
    def getUsername(self):
        return Storage.username
    def getPassword(self):
        return Storage.password    


    

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
        for F in (StartPage, Register, Login):
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
        self.Button1.place(relx=0.502, rely=0.511, height=43, width=115)
        self.Button1.configure(text='''Login''',command=lambda : self.verify(controller))

        
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
                controller.show_frame('Register')
            else:
                messagebox.showinfo('Error','Incorrect Password')
        else:
            messagebox.showinfo('MisMatch',"Incorrect username")
            self.Entry3.delete(0,tk.END)




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()