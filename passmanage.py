import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Calibri', size=18, weight="bold")
        self.geometry("300x300")
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
        
        username=tk.StringVar()
        password=tk.StringVar()
        
        tk.Label(self,text="Username --").pack()
        name=tk.Entry(self,textvariable=username)
        name.pack()
        
        tk.Label(self,text="Password--").pack()
        pasw=tk.Entry(self,textvariable=password)
        pasw.pack()
        
        button = tk.Button(self, text="Register",width="25",height="2",
                command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Login",width="25",height="2",
                           command=lambda: controller.show_frame("Login"))
        
        button.pack()
        button1.pack()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Verify that it's you", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        user_name=tk.StringVar()
        pass_word=tk.StringVar()
        tk.Label(self,text="Username --").pack()
        name=tk.Entry(self,textvariable=user_name)
        name.pack()
        
        tk.Label(self,text="Password--").pack()
        pasw=tk.Entry(self,textvariable=pass_word)
        pasw.pack()
        
        button = tk.Button(self, text="Login",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()