from tkinter import *
import add_category,add_menu,add_members
import view_category,view_menu,view_members

class AdminDashboard:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x800")
        self.root.title("RESTAURANT FULL DETAILS")

    def dashboard_widgets(self):
        self.f=Frame(self.root,bg="LightGray")
        self.f.place(x=0,y=0,width=800,height=800)

        self.title=Label(self.f,text="Restaurant Detail",font=("Google Sans",20,"bold"),bg="LightGray")
        self.title.place(x=230,y=70)
        
        # Add category
        self.title_category=Label(self.f,text="Food Category:",font=("Google Sans",17,"bold"),bg="LightGray")
        self.title_category.place(x=110,y=180)
        self.addCategory_frame_button = Button(self.f,text="Add Category",font=("Google Sans",13),command=self.open_addCategoryPage_frame)
        self.addCategory_frame_button.place(x=350,y=180,width=150,height=30)

        #view category
        self.viewCategory_frame_button = Button(self.f,text="View Category",font=("Google Sans",13),command=self.open_viewCategoryPage_frame)
        self.viewCategory_frame_button.place(x=560,y=180,width=150,height=30)
        
        #add menu
        self.title_menu=Label(self.f,text="Food Menu:",font=("Google Sans",17,"bold"),bg="LightGray")
        self.title_menu.place(x=110,y=240)
        self.addMenu_frame_button = Button(self.f,text="Add Menu",font=("Google Sans",13),command=self.open_addMenuPage_frame)
        self.addMenu_frame_button.place(x=350,y=240,width=150,height=30)

        #view menu
        self.viewMenu_frame_button = Button(self.f,text="View Menu",font=("Google Sans",13),command=self.open_viewMenuPage_frame)
        self.viewMenu_frame_button.place(x=560,y=240,width=150,height=30)
        
        #add members
        self.title_members=Label(self.f,text="Resturant Members:",font=("Google Sans",17,"bold"),bg="LightGray")
        self.title_members.place(x=110,y=310)
        self.addMembers_frame_button = Button(self.f,text="Add Members",font=("Google Sans",13),command=self.open_addMembersPage_frame)
        self.addMembers_frame_button.place(x=350,y=310,width=150,height=30)

        #view members
        self.viewMembers_frame_button = Button(self.f,text="View Members",font=("Google Sans",13),command=self.open_viewMembersPage_frame)
        self.viewMembers_frame_button.place(x=560,y=310,width=150,height=30)
        #add orders
        self.title_orders=Label(self.f,text="Food orders:",font=("Google Sans",17,"bold"),bg="LightGray")
        self.title_orders.place(x=110,y=380)
        self.addOrders_frame_button = Button(self.f,text="Add Orders",font=("Google Sans",13))
        self.addOrders_frame_button.place(x=350,y=380,width=150,height=30)

        #view orders
        self.viewOrders_frame_button = Button(self.f,text="View Orders",font=("Google Sans",13))
        self.viewOrders_frame_button.place(x=560,y=380,width=150,height=30)
    def open_addCategoryPage_frame(self):
        self.root.destroy()
        i=add_category.AddCategory()
        i.add_category_widgets()
    
    def open_viewCategoryPage_frame(self):
        self.root.destroy()
        k=view_category.viewCategory()
        k.view_category_widgets()
    def open_addMenuPage_frame(self):
        self.root.destroy()
        a=add_menu.AddMenu()
        a.add_menu_widgets()

    def open_viewMenuPage_frame(self):
        self.root.destroy()
        s = view_menu.ViewMenu()
        s.view_menu_widgets()

    def open_addMembersPage_frame(self):
        self.root.destroy()
        a=add_members.AddMembers()
        a.add_members_widgets()
    def open_viewMembersPage_frame(self):
        self.root.destroy()
        s = view_members.ViewMembers()
        s.view_members_widgets()
    # def open_addOrdersPage_frame(self):
    # def open_viewOrdersPage_frame(self):
   
if __name__=="__main__":
 k=AdminDashboard()
 k.dashboard_widgets()
 k.root.mainloop()