from tkinter import *
from tkinter import ttk
import database,add_order
from tkinter import messagebox
class ViewOrder:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x600")
        self.root.title("ALL ORDERS")
    def view_order_widgets(self):
        self.f=Frame(self.root,bg="Lightyellow")
        self.f.place(x=0,y=0,width=600,height=600)
        self.tree_view=ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H"))
        
        self.tree_view.heading("#0",text="Id")
        self.tree_view.column("#0",width=50)

        self.tree_view.heading("#1",text="Table no")
        self.tree_view.column("#1",width=70)

        self.tree_view.heading("#2",text="Food Code")
        self.tree_view.column("#2",width=70)

        self.tree_view.heading("#3",text="quantity")
        self.tree_view.column("#3",width=70)
        self.tree_view.heading("#4",text="Total Bill")
        self.tree_view.column("#4",width=70)

        self.tree_view.heading("#5",text="Change status")
        self.tree_view.column("#5",width=90)

        self.tree_view.heading("#6",text="delete")
        self.tree_view.column("#6",width=70)
        
        self.tree_view.heading("#7",text="Update")
        self.tree_view.column("#7",width=70)
        for i in database.show_all_order():
             self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],i[3],i[4],i[5],"Delete","Update")) 
        self.tree_view.bind("<Double-Button-1>",self.tree_view_actions)
        self.tree_view.place(x=15,y=10,width=570,height=550)
    def tree_view_actions(self,e):
        row=self.tree_view.focus()
        print("Focus row-",row)

        column_id=self.tree_view.identify_column(e.x)
        print("Column Id - ", column_id)
        focused_row_data = self.tree_view.item(row)
        print("Focused row data - ", focused_row_data)
        selected_order_id = focused_row_data.get("text")
        print("Selected order id - ", selected_order_id)
        if column_id == "#6":
            delete_confirmation = messagebox.askyesno("Alert!","Do you really want to delete this item?")
            if delete_confirmation:
                data = (selected_order_id,)
                result = database.delete_order_info(data)
                if result:
                    messagebox.showinfo("Messsage","order deleted successfuly")
                    self.root.destroy()
                    k =ViewOrder()
                    k.view_member_order_widgets()
                else:
                    messagebox.showwarning("Alert!","Something went wrong")
            else:
                print("Not Deleted")
        elif column_id == "#7":
            a = add_order.AddOrder(self.tree_view.item(row))
            self.root.destroy()
            a.add_order_widgets()

if __name__=="__main__":
    k=ViewOrder()
    k.view_order_widgets()
    k.root.mainloop()