from tkinter import *
from tkinter import ttk
import database
class view_category:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x600")
        self.root.title("All Categories")
    def view_category_widgets(self):
        self.f=Frame(self.root,bg="Lightyellow")
        self.f.place(x=0,y=0,width=600,height=600)
        self.tree_view=ttk.Treeview(self.f,columns=("A","B","C","D"))
        
        self.tree_view.heading("#0",text="Id")
        self.tree_view.column("#0",width=140)

        self.tree_view.heading("#1",text="Category Name")
        self.tree_view.column("#1",width=140)

        self.tree_view.heading("#2",text="Delete")
        self.tree_view.column("#2",width=140)
        self.tree_view.heading("#3",text="Update")
        self.tree_view.column("#3",width=140)
        for i in database.show_all_category():
             self.tree_view.insert("",0,text=i[0],values=(i[1],"Delete","Update")) 
        self.tree_view.bind("<Double-Button-1>",self.tree_view_actions)
        self.tree_view.place(x=15,y=10,width=570,height=550)
        
k=view_category()
k.view_category_widgets()
k.root.mainloop()