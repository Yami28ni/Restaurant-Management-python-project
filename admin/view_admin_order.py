from tkinter import *
from tkinter import ttk
import database

class ViewAdminOrder:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x600")
        self.root.title("VIEW ORDER")

    def view_admin_order_widgets(self):
        self.f = Frame(self.root,bg="Light Yellow")
        self.f.place(x=20,y=20,width=860,height=560)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D"))

        self.tree_view.heading("#0",text="Id")
        self.tree_view.column("#0",width=50)

        self.tree_view.heading("#1",text="Food Code")
        self.tree_view.column("#1",width=150)

        self.tree_view.heading("#2",text="Member Id")
        self.tree_view.column("#2",width=150)

        self.tree_view.heading("#3",text="Change Status")
        self.tree_view.column("#3",width=150)
        
        for i in database.show_all_order():
            self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],"PENDING"))    
        self.tree_view.place(x=10,y=10)


v = ViewAdminOrder()
v.view_admin_order_widgets()
v.root.mainloop()