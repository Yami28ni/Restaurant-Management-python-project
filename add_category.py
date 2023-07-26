from tkinter import *
import database
class add_category:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x600")
        self.root.title("Category")
    def add_category_widgets(self):
        self.f=Frame(self.root,bg="Lightpink")
        self.f.place(x=0,y=0,width=600,height=600)
        self.category=Label(self.f,text="Category Name",bg="Lightpink",font=("Google Sans",17,"bold"))
        self.category.place(x=200,y=150)
        self.entrybox=Entry(self.f,font=("Century Gothic",12))
        self.entrybox.place(x=200,y=200)
        self.b=Button(self.f,text="Sumit",bg="Lightpink",command=self.run_add_category_query)
        self.b.place(x=250,y=250)

    def run_add_category_query(self):
        showCategory=(self.entrybox.get(),)
        print("Category is",showCategory)
        result=database.add_category_info(showCategory)
        if result:
            print("category added")
        else:
            print("category not added")
i=add_category()
i.add_category_widgets()
i.root.mainloop()       