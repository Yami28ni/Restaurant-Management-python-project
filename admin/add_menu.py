from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import database,view_menu

class AddMenu:
    def __init__(self,selected_menu_data=""):
        self.root=Tk()
        self.root.geometry("800x800")

        self.selectedMenuData = selected_menu_data
        
        if self.selectedMenuData:
            self.root.title('UPDATE MENU')
        else:
            self.root.title('ADD MENU')
        
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

        self.type_list=[]
        for i in database.show_all_category():
            self.type_list.append(i[1]) # 0 to get id,1 for text
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

        if self.selectedMenuData:
            print("selected menu data - ", self.selectedMenuData)
            result = dict(self.selectedMenuData).get("values")
            self.food_name_entry.insert(0,result[0])
            self.food_code_entry.insert(0,result[1])
            self.type_combobox.set(result[2])
            self.food_price_entry.insert(0,result[3])
            self.type_combobox1.set(result[4])
            
            self.b=Button(self.f, text="UPDATE",bg='DeepSkyBlue4',font=("Google Sans",12),command=self.run_update_menu_query)
            self.b.place(x=290,y=480,width=150)
        else:
            self.b=Button(self.f, text="Submit",bg='DeepSkyBlue4',font=("Google Sans",12),command=self.run_add_menu_query)
            self.b.place(x=290,y=480,width=150)
    def run_add_menu_query(self):
        menu_items=(self.food_name_entry.get(),self.food_code_entry.get(),self.type_combobox.get(),self.food_price_entry.get(),self.type_combobox1.get())
        print("All menu items are:",menu_items)
        result=database.add_menu_info(menu_items)
        if result:
            messagebox.showinfo("Message"," Menu is  added successfully")
            self.root.destroy()
            s = view_menu.ViewMenu()
            s.view_menu_widgets()
        else:
            messagebox.showinfo("Message","Alert!,Something went wrong")

    def run_update_menu_query(self):
        updated_menu_details = (self.food_name_entry.get(),self.food_code_entry.get(),self.type_combobox.get(),self.food_price_entry.get(),self.type_combobox1.get(),
            dict(self.selectedMenuData).get("text")
        )

        update_result = database.update_menu(updated_menu_details)
        print("Update result - ", update_result)
        if update_result:
            messagebox.showinfo("Message","menu updated successfully")
            self.root.destroy()
            s= view_menu.ViewMenu()
            s.view_menu_widgets()
        else:
            messagebox.showwarning("Alert!","Something went wrong")

if __name__=="__main__":
    a=AddMenu()
    a.add_menu_widgets()
    a.root.mainloop()















     