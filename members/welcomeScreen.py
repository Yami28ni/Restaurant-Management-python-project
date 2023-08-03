from tkinter import *
import admin_login
import members_loginPage

class WelcomeScreen:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x600")
        self.root.title("Welcome Page")

    def widgets(self):
        self.f=Frame(self.root,bg="lavender")
        self.f.place(x=0,y=0,width=600,height=600)

        self.title=Label(self.f,text="WELCOME ALL",font=("Google Sans",20,"bold"),bg="lavender")
        self.title.place(x=200,y=90,width=200)
        
        self.admin_frame_button = Button(self.f,text="Admin Page",command=self.open_adminPage_frame)
        self.admin_frame_button.place(x=120,y=190,width=150)

        self.members_frame_button = Button(self.f,text="Members Login Page",command=self.open_MembersLoginPage_frame)
        self.members_frame_button.place(x=350,y=190,width=150)

    def open_adminPage_frame(self):
        self.root.destroy()
        a = admin_login.admin_login()
        a.admin_login_widgets()
    
    def open_MembersLoginPage_frame(self):
        self.root.destroy()
        j=members_loginPage.MembersLogin()
        j.members_login_widgets()

if __name__=="__main__":
  k=WelcomeScreen()
  k.widgets()
  k.root.mainloop()
