from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import database,view_members

class AddMembers:
    def __init__(self,selected_members_data=""):
        self.root=Tk()
        self.root.geometry("800x800")

        self.selectedMembersData = selected_members_data
        
        if self.selectedMembersData:
            self.root.title('UPDATE MEMBERS')
        else:
            self.root.title('ADD MEMBERS')
        
    def add_members_widgets(self):
        self.f=Frame(self.root,bg="Lightgrey")
        self.f.place(x=0,y=0,width=800,height=800)

        self.main_title=Label(self.f,text="Members Details",font=("Google Sans",20,"bold"),bg="Lightgrey",fg="DeepSkyBlue4")
        self.main_title.place(x=270,y=100)
        
        #name
        self.name=Label(self.f,text=" Name:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.name.place(x=100,y=190)
        self.name_entry=Entry(self.f,font=("Century Gothic",12))
        self.name_entry.place(x=100,y=220,height=25,width=200)
        
        #phone no
        self.phone_no=Label(self.f,text="phone no:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.phone_no.place(x=450,y=190)
        self.phone_no_entry=Entry(self.f,font=("Century Gothic",12))
        self.phone_no_entry.place(x=450,y=220,height=25,width=200)
        
        #designation
        self.designation=Label(self.f,text="Designation:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.designation.place(x=100,y=280)

        self.type_list=["cook","waiter","bartender","manager"]
        self.type_combobox=Combobox(self.f,values=self.type_list,font=("Google Sans",12),state="readonly")
        self.type_combobox.place(x=100,y=310,height=25,width=200)        
        
        #address
        self.address=Label(self.f,text="address:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.address.place(x=450,y=280)
        self.address_entry=Entry(self.f,font=("Century Gothic",12))
        self.address_entry.place(x=450,y=310,height=25,width=200)
        #username
        self.username=Label(self.f,text="Username:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.username.place(x=100,y=370)
        self.username_entry=Entry(self.f,font=("Century Gothic",12))
        self.username_entry.place(x=100,y=400,height=25,width=200)
        #password
        self.password=Label(self.f,text="Password:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.password.place(x=450,y=370)
        self.password_entry=Entry(self.f,font=("Century Gothic",12))
        self.password_entry.place(x=450,y=400,height=25,width=200)
        
        

        if self.selectedMembersData:
            print("selected menu data - ", self.selectedMembersData)
            result = dict(self.selectedMembersData).get("values")
            self.name_entry.insert(0,result[0])
            self.phone_no_entry.insert(0,result[1])
            self.type_combobox.set(result[2])
            self.address_entry.insert(0,result[3])
           
            
            self.b=Button(self.f, text="UPDATE",bg='DeepSkyBlue4',font=("Google Sans",12),command=self.run_update_members_query)
            self.b.place(x=290,y=480,width=150)
        else:
            self.b=Button(self.f, text="Submit",bg='DeepSkyBlue4',font=("Google Sans",12),command=self.run_add_members_query)
            self.b.place(x=290,y=480,width=150)
    def run_add_members_query(self):
        members_items=(
            self.name_entry.get(),
            self.phone_no_entry.get(),
            self.type_combobox.get(),
            self.address_entry.get(),
            self.username_entry.get(),
            self.password_entry.get()
        )
        
        print("All members items are:",members_items)
        
        result=database.add_members_info(members_items)
        if result:
            messagebox.showinfo("Message"," Members is  added successfully")
            self.root.destroy()
            s = view_members.ViewMembers()
            s.view_members_widgets()
        else:
            messagebox.showinfo("Message","Alert!,Something went wrong")

    def run_update_members_query(self):
        updated_members_details = (
            self.name_entry.get(),
            self.phone_no_entry.get(),
            self.type_combobox.get(),
            self.address_entry.get(),
            dict(self.selectedMembersData).get("text")
        )

        update_result = database.update_members(updated_members_details)
        print("Update result - ", update_result)
        if update_result:
            messagebox.showinfo("Message","members updated successfully")
            self.root.destroy()
            s= view_members.ViewMembers()
            s.view_members_widgets()
        else:
            messagebox.showwarning("Alert!","Something went wrong")

if __name__=="__main__":
    a=AddMembers()
    a.add_members_widgets()
    a.root.mainloop()















     