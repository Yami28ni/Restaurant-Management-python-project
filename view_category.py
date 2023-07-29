from tkinter import *
from tkinter import ttk
import database,add_category
from tkinter import messagebox
class viewCategory:
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

        self.tree_view.heading("#1",text="category")
        self.tree_view.column("#1",width=140)

        self.tree_view.heading("#2",text="Delete")
        self.tree_view.column("#2",width=140)
        self.tree_view.heading("#3",text="Update")
        self.tree_view.column("#3",width=140)
        for i in database.show_all_category():
             self.tree_view.insert("",0,text=i[0],values=(i[1],"Delete","Update")) 
        self.tree_view.bind("<Double-Button-1>",self.tree_view_actions)
        self.tree_view.place(x=15,y=10,width=570,height=550)
    def tree_view_actions(self,e):
        row=self.tree_view.focus()
        print("Focus row-",row)

        column_id=self.tree_view.identify_column(e.x)
        print("Column Id - ", column_id)
        focused_row_data = self.tree_view.item(row)
        print("Focused row data - ", focused_row_data)
        selected_category_id = focused_row_data.get("text")
        print("Selected category id - ", selected_category_id)
        if column_id == "#2":
            delete_confirmation = messagebox.askyesno("Alert!","Do you really want to delete this item?")
            if delete_confirmation:
                data = (selected_category_id,)
                result = database.delete_category_info(data)
                if result:
                    messagebox.showinfo("Messsage","Category deleted successfuly")
                    self.root.destroy()
                    k =viewCategory()
                    k.view_category_widgets()
                else:
                    messagebox.showwarning("Alert!","Something went wrong")
            else:
                print("Not Deleted")
        elif column_id == "#3":
            a = add_category.AddCategory(self.tree_view.item(row))
            self.root.destroy()
            a.add_category_widgets()

if __name__=="__main__":
    k=viewCategory()
    k.view_category_widgets()
    k.root.mainloop()