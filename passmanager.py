import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

import json
from os.path import isfile
from os import getcwd
import hashlib
import sys
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Calibri', size=18, weight="bold")
        self.geometry("300x300")
        

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Register):
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
    
        


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Password Manager!", font=controller.title_font, bg = "grey", fg = "white")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Login",width="30",height="2",
                            command=lambda: controller.show_frame("Login"))
        button2 = tk.Button(self, text="Register",width="30",height="2",
                            command=lambda: controller.show_frame("Register"))
        button1.pack()
        
        button2.pack()


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Give your username and password!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        
        
        
        
        
        
        
        
        
        
        
        def register():
            username=tk.StringVar()
            password=tk.StringVar()
            
            tk.Label(self,text="Username --").pack()
            name=tk.Entry(self,textvariable=username)
            name.pack()
            
            tk.Label(self,text="Password--").pack()
            pasw=tk.Entry(self,textvariable=password)
            pasw.pack()

            obj=BackGround(username,password)
            l=tk.Label(self,text="Account added successfully",fg="green")
            l.pack()
            m=tk.Label(self,text="Get Logged in and save your passwords :)",fg="blue")
            m.pack()

        
        
        button = tk.Button(self, text="Register",width="25",height="2",
                                                                       command=register)
        button1 = tk.Button(self, text="Login",width="25",height="2",
                            command=lambda: controller.show_frame("Login"))
        
        button.pack()
        button1.pack()


    


class BackGround():

    def __init__(self,u,p):
        
        print("In BackGround constructor")
        
        
        if self.check():
            self.loadFile()
            
        else:
            self.create(self.u,self.p)
    def check(self):
        """
        this method is used to check if the json exists or not
        :return:
        """
        print("In the  check func.")
        self.path=getcwd()
        print(self.path)
        if isfile(self.path):
            return True
        else:
            return False
    def create(self,uname,password):
        """
        this function asks for permission and then takes the username and
        master password
        hashes the master password and store it in the json file in json
        array format

        :return: none
        """
        print("In create func.")
   
        
        f=open(self.path,'w+')
        self.username=uname
        self.password=password.encode('utf-8')
        self.hashed=hashlib.sha512(password).hexdigest()
        
        d=dict()
        d[username]=hashed
        l=[]
        l.append(d)
        l.append(dict())
        jdata=json.dumps(l,indent=4)
        f.write(jdata)
        f.close()
        return True
        
    def loadFile(self):
        """
        this method is used to load the safe file and feed the hashed
        master password and username and total no of paswords in the
        safe file
        :return: none
        """
        with open(self.path) as f:
            self.data = json.load(f)
        self.no_of_passwords=len(self.data[1])
        l=list((self.data[0]).keys())
        self.user_name=l[0]
        self.hashed_password=(self.data[0])[self.user_name]        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()