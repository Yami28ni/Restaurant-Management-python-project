from tkinter import *
# from tkinter import messagebox

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
        self.food_name_entry=Entry(self.f,font=("Century Gothic",12))
        self.food_name_entry.place(x=100,y=310,height=25,width=200)
         #price
        self.food_name=Label(self.f,text="Price:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_name.place(x=450,y=280)
        self.food_name_entry=Entry(self.f,font=("Century Gothic",12))
        self.food_name_entry.place(x=450,y=310,height=25,width=200)
         #size
        self.food_name=Label(self.f,text="Food Size:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_name.place(x=100,y=370)
        self.food_name_entry=Entry(self.f,font=("Century Gothic",12))
        self.food_name_entry.place(x=100,y=400,height=25,width=200)
         #add
        self.b=Button(self.f, text="Submit",bg='DeepSkyBlue4',font=("Google Sans",12))
        self.b.place(x=290,y=480,width=150)

        
k=AddMenu()
k.add_menu_widgets()
k.root.mainloop()















i=Add_menu()
i.Add_menu_widgets()
i.root.mainloop()











     