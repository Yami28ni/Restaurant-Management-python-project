from tkinter import *
import database
from tkinter import messagebox
class MembersLogin:
    def __init__(self):
        self.root=Tk()
        self.root.title("Login Page")
        self.root.geometry("600x600")
    def members_login_widgets(self):
        self.f=Frame(self.root,bg="LightGray")
        self.f.place(x=0,y=0,width=600,height=600)
        self.title=Label(self.f,text="Members Login Page",font=("Google Sans",20,"bold"),bg="LightGray",fg="Blue")
        self.title.place(x=150,y=100)
        self.username=Label(self.f,text="Username:",font=("Google Sans",16),bg="LightGray",fg="Blue")
        self.username.place(x=100,y=200)
        self.username_entry=Entry(self.f)
        self.username_entry.place(x=250,y=200,height=25,width=200)
        self.password=Label(self.f,text="Password:",font=("Google Sans",16),bg="LightGray",fg="Blue")
        self.password.place(x=100,y=270)
        self.password_entry=Entry(self.f)
        self.password_entry.place(x=250,y=270,height=25,width=200)
        self.b=Button(self.f,text="Login",bg="Blue",font=("Google Sans",10,"bold"),command=self.run_members_login_query)
        self.b.place(x=220,y=350,width=130)
    def run_members_login_query(self):
        members_details=(self.username_entry.get(),self.password_entry.get())
        print("Username and password is ",members_details)
        result=database.members_login(members_details)
        if result:
            messagebox.showinfo("Message","Login successfull")
        else:
            messagebox.showinfo("Message","Incorrect username or password")

if __name__=="__main__":
    j=MembersLogin()
    j.members_login_widgets()
    j.root.mainloop()