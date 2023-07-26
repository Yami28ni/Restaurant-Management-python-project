from tkinter import *
import database
from tkinter import messagebox
class admin_login:
    def __init__(self):
        self.root=Tk()
        self.root.title("Login Page")
        self.root.geometry("600x600")
    def admin_login_widgets(self):
        self.title=Label(self.root,text="Login Page",font=("Google Sans",17,"bold"))
        self.title.place(x=200,y=100)
        self.username=Label(self.root,text="Username",font=("Google Sans",14))
        self.username.place(x=100,y=200)
        self.username_entry=Entry(self.root)
        self.username_entry.place(x=250,y=200)
        self.password=Label(self.root,text="Password",font=("Google Sans",14))
        self.password.place(x=100,y=230)
        self.password_entry=Entry(self.root)
        self.password_entry.place(x=250,y=230)
        self.b=Button(self.root,text="Login",bg="Lightblue",font=("Google Sans",10,"bold"),command=self.run_admin_login_query)
        self.b.place(x=250,y=290)
    def run_admin_login_query(self):
        admin_details=(self.username_entry.get(),self.password_entry.get())
        print("Username and password is ",admin_details)
        result=database.admin_login(admin_details)
        if result:
            messagebox.showinfo("Message","Login successfull")
        else:
            messagebox.showinfo("Message","Incorrect username or password")
j=admin_login()
j.admin_login_widgets()
j.root.mainloop()