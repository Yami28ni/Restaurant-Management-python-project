from tkinter import *
import database,view_category
from tkinter import messagebox
class AddCategory:
    def __init__(self,selected_category_data=""):
        self.root=Tk()

        self.selectedCategoryData = selected_category_data
        
        if self.selectedCategoryData:
            self.root.title('UPDATE CATEGORY')
        else:
            self.root.title('ADD CATEGORY')
        
        self.root.geometry("600x600")
        self.root.title("Add Category | Restaurent Management")

    def add_category_widgets(self):
        self.f=Frame(self.root,bg="MistyRose2")
        self.f.place(x=0,y=0,width=600,height=600)
        
        self.category=Label(self.f,text="Category Name",bg="MistyRose2",font=("Google Sans",17,"bold"))
        self.category.place(x=200,y=150)
        
        self.category_name_entry=Entry(self.f,font=("Century Gothic",12))
        self.category_name_entry.place(x=200,y=200)

        if self.selectedCategoryData:
            print("selected category data - ", self.selectedCategoryData)
            result = dict(self.selectedCategoryData).get("values")
            self.category_name_entry.insert(0,result[0])
            
            self.b = Button(self.f, text='UPDATE',bg='MistyRose2',fg='Black', font=("Century Gothic bold",12), command=self.run_update_category_query)
            self.b.place(x=250, y=250,width=100)
        else:
            self.b = Button(self.f, text='SUBMIT',bg='MistyRose2',fg='Black', font=("Century Gothic bold",12), command=self.run_add_category_query)
            self.b.place(x=250, y=250,width=100)
    
    def run_add_category_query(self):
        showCategory=(self.category_name_entry.get(),)
        print("Category is",showCategory)
        result=database.add_category_info(showCategory)
        if result:
            messagebox.showinfo("Message","category added successfully")
            self.root.destroy()
            v = view_category.viewCategory()
            v.view_category_widgets()
        else:
            messagebox.showwarning("Alert!","Something went wrong")

    def run_update_category_query(self):
        updated_category_details = (self.category_name_entry.get(),
            dict(self.selectedCategoryData).get("text")
        )

        update_result = database.update_category(updated_category_details)
        print("Update result - ", update_result)
        if update_result:
            messagebox.showinfo("Message","category updated successfully")
            self.root.destroy()
            v = view_category.viewCategory()
            v.view_category_widgets()
        else:
            messagebox.showwarning("Alert!","Something went wrong")

if __name__=="__main__":
    i=AddCategory()
    i.add_category_widgets()
    i.root.mainloop()       