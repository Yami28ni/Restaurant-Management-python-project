from tkinter import *
from tkinter.ttk import Combobox
import database,view_member_order
from tkinter import messagebox
class AddOrder:
    def __init__(self,selected_order_data=""):
        self.root=Tk()
        self.selectedOrderData = selected_order_data
        
        if self.selectedOrderData:
            self.root.title('UPDATE ORDER')
        else:
            self.root.title('ADD ORDER')
        
        self.root.title("FOOD ORDER | Restaurent Management")
        self.root.geometry("800x800")
        self.selected_menu_price = 0
    def add_order_widgets(self):
        self.f=Frame(self.root,bg="Lightgrey")
        self.f.place(x=0,y=0,width=800,height=800)

        self.main_title=Label(self.f,text="Food Order",font=("Google Sans",20,"bold"),bg="Lightgrey",fg="DeepSkyBlue4")
        self.main_title.place(x=250,y=100)
        
        #Table no
        self.table_no=Label(self.f,text="Table No",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.table_no.place(x=100,y=190)

        self.type_list=["1","2","3","4","5","6","7","8"]
        self.type_combobox=Combobox(self.f,values=self.type_list,font=("Google Sans",12),state="readonly")
        self.type_combobox.place(x=300,y=190,height=25,width=200) 
        #Food items
        self.food_code=Label(self.f,text="Menu Code:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.food_code.place(x=100,y=230)
        
        self.type_list=[]
        for i in database.show_all_menu():
            print(i)
            self.type_list.append("{b}".format(b=i[2])) # 0 to get id,1 for text
        self.type_combobox1=Combobox(self.f,values=self.type_list,font=("Google Sans",12),state="readonly")
        self.type_combobox1.bind("<<ComboboxSelected>>",self.get_menu_price)
        self.type_combobox1.place(x=300,y=230,height=25,width=200)
        
        #quantity
        self.quantity=Label(self.f,text="Quantity (In Plates):",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
        self.quantity.place(x=100,y=270)

        self.type_list=["1","2","3"]
        self.type_combobox3=Combobox(self.f,values=self.type_list,font=("Google Sans",12),state="readonly")
        self.type_combobox3.bind("<<ComboboxSelected>>",self.get_menu_quantity)
        self.type_combobox3.place(x=300,y=270,height=25,width=200)        
   


    def get_menu_price(self,event):
        selected_menu_code = self.type_combobox1.get()
        print(selected_menu_code)

        result = database.get_menu_price((selected_menu_code, ))
        if result:
            self.code_label = Label(self.f)
            self.code_label.place(x=550,y=230,width=200)
            self.code_label.config(text="Price - {a}".format(a = result[0]))

            self.selected_menu_price = result[0]
            print("Selected menu price - ", self.selected_menu_price)
    
    def get_menu_quantity(self,event):
        selected_quantity=self.type_combobox3.get()
        print(selected_quantity)
        result1=selected_quantity
        if result1:
            self.code_label = Label(self.f)
            self.code_label.place(x=550,y=270,width=200)
            self.code_label.config(text="quantity - {a}".format(a = result1[0]))

            self.selected_quantity = result1[0]
            print("Selected menu price - ", self.selected_quantity)
        
            #total bill
            self.Total_bill=Label(self.f,text="Total Bill:",font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
            self.Total_bill.place(x=100,y=320)

            self.total_bill_amount_label=Label(self.f,font=("Google Sans",15),bg="Lightgrey",fg="DeepSkyBlue4")
            self.total_bill_amount_label.place(x=300,y=320,width=100)

            self.total_bill_amount = int(self.type_combobox3.get()) * int(self.selected_menu_price)
            self.total_bill_amount_label.config(text="{a}".format(a=self.total_bill_amount))

        if self.selectedOrderData:
            print("selected order data - ", self.selectedOrderData)
            result = dict(self.selectedOrderData).get("values")
            self.type_combobox.set(result[0])
            self.type_combobox1.set(result[1])
            self.type_combobox3.set(result[2])
            self.b=Button(self.f, text="Update",bg='DeepSkyBlue4',font=("Google Sans",12),command=self.run_update_order_query)
            self.b.place(x=270,y=400,width=150)
        else:
            self.b=Button(self.f, text="Add",bg='DeepSkyBlue4',font=("Google Sans",12),command=self.run_add_order_query)
            self.b.place(x=270,y=400,width=150)

    def run_add_order_query(self):
        showOrder=(self.type_combobox.get(),self.type_combobox1.get(),self.type_combobox3.get(),self.total_bill_amount,"PENDING")
        print("Items in the order are",showOrder)
        order_result=database.add_order_info(showOrder)
        
        if order_result:
            messagebox.showinfo("Message","order is  added successfully")
            self.root.destroy()
            k = view_member_order.ViewOrder()
            k.view_order_widgets()
        else:
            messagebox.showinfo("Message","Alert!,Something went wrong")

    def run_update_order_query(self):
        updated_order_details = (self.type_combobox.get(),self.type_combobox1.get(),self.type_combobox3.get(),self.total_bill_amount,
            
            dict(self.selectedOrderData).get("text")
        )

        update_result = database.update_order(updated_order_details)
        print("Update result - ", update_result)
        if update_result:
            messagebox.showinfo("Message","order updated successfully")
            self.root.destroy()
            k= view_member_order.ViewOrder()
            k.view_order_widgets()
        else:
            messagebox.showwarning("Alert!","Something went wrong")
if __name__=="__main__":
  s=AddOrder()
  s.add_order_widgets()
  s.root.mainloop()