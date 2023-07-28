from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import database

class AddMenu:
    def __init__(self):
        self.root=Tk()
        self.root.title("ADD MENU")
        self.root.geometry("800x800")
    def add_menu_widgets(self):
        self.f=Frame(self.root,bg="Lightgrey")
        self.f.place(x=0,y=0,width=800,height=800)

        self.main_title=Label(self.f,text="Food Menu",font=("Google Sans",20,"bold"),bg="Lightgrey",fg="DeepSkyBlue4")
        self.main_title.place(x=270,y=100)
        #food name
        self.food_name=Label(self.f,text="Food Name:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_name.place(x=100,y=190)
        self.food_name_entry=Entry(self.f,font=("Century Gothic",12))
        self.food_name_entry.place(x=100,y=220,height=25,width=200)
        #food code
        self.food_code=Label(self.f,text="Food Code:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_code.place(x=450,y=190)
        self.food_code_entry=Entry(self.f,font=("Century Gothic",12))
        self.food_code_entry.place(x=450,y=220,height=25,width=200)
        #category
        self.food_name=Label(self.f,text="Category:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_name.place(x=100,y=280)

        self.type_list=["Veg","NonVeg"]
        self.type_combobox=Combobox(self.f,values=self.type_list,font=("Google Sans",12),state="readonly")
        self.type_combobox.place(x=100,y=310,height=25,width=200)        
         #price
        self.food_price=Label(self.f,text="Price:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_price.place(x=450,y=280)
        self.food_price_entry=Entry(self.f,font=("Century Gothic",12))
        self.food_price_entry.place(x=450,y=310,height=25,width=200)
         #size
        self.food_size=Label(self.f,text="Food Size:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_size.place(x=100,y=370)
        self.type_list = ["Small","Medium","Large"]
        self.type_combobox1=Combobox(self.f,values=self.type_list,font=("Google Sans",12),state="readonly")
        self.type_combobox1.place(x=100,y=400,height=25,width=200)
        #add
        self.b=Button(self.f, text="Submit",bg='DeepSkyBlue4',font=("Google Sans",12),command=self.run_add_menu_query)
        self.b.place(x=290,y=480,width=150)
    def run_add_menu_query(self):
        menu_items=(self.food_name_entry.get(),self.food_code_entry.get(),self.type_combobox.get(),self.food_price_entry.get(),self.type_combobox1.get())
        print("All menu items are:",menu_items)
        result=database.add_menu_info(menu_items)
        if result:
            messagebox.showinfo("Message"," Menu is  added successfully")
        else:
            messagebox.showinfo("Message","Alert!,Something went wrong")
        
k=AddMenu()
k.add_menu_widgets()
k.root.mainloop()















     