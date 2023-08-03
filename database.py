import mysql.connector
con=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='restaurent'
)
cursor=con.cursor()

def admin_login(login_details):
    cursor.execute("select * from admin where username=%s and password=%s",login_details)
    return cursor.fetchone()

def add_category_info(showCategory):
    try:
        cursor.execute("INSERT INTO category (category_name) VALUES(%s)",showCategory)
        con.commit()
        return True
    except:
        return False

def show_all_category():
    cursor.execute("SELECT * FROM `category`")
    return cursor.fetchall()

def delete_category_info(category_id):
    print("Database: category id ", category_id)
    cursor.execute("DELETE FROM `category` WHERE `id`=%s",category_id)
    con.commit()
    return True
    
def update_category(updated_category_details):
    print("Database: updated category details ",updated_category_details)
    try:
        cursor.execute("UPDATE `category` SET `category_name`=%s WHERE `id`=%s",updated_category_details)
        con.commit()
        return True
    except:
        return False

def add_menu_info(menu_items):
    try:
        cursor.execute("INSERT INTO menu (food_name,code,category,price,size) VALUES(%s,%s,%s,%s,%s)",menu_items)
        con.commit()
        return True
    except:
        return False

def show_all_menu():
    cursor.execute("SELECT * FROM `menu`")
    return cursor.fetchall()

def get_menu_price(menu_code):
    print("Database: menu code - ", menu_code)
    cursor.execute("SELECT `price` FROM `menu` WHERE `code`=%s",menu_code)
    return cursor.fetchone()

def delete_menu_info(menu_id):
    print("Database: menu id ", menu_id)
    cursor.execute("DELETE FROM `menu` WHERE `id`=%s",menu_id)
    con.commit()
    return True
    
def update_menu(updated_menu_details):
    print("Database: updated menu details ",updated_menu_details)
    try:
        cursor.execute("UPDATE `menu` SET `food_name`=%s, `code`=%s, `category`=%s, `price`=%s, `size`=%s WHERE `id`=%s",updated_menu_details)
        con.commit()
        return True
    except:
        return False

def add_members_info(members_items):
    try:
        cursor.execute("INSERT INTO members (Name,Phone_no,Designation,Address,username,password) VALUES(%s,%s,%s,%s,%s,%s)",members_items)
        con.commit()
        return True
    except:
        return False

def show_all_members():
    cursor.execute("SELECT * FROM `members`")
    return cursor.fetchall()

def delete_members_info(members_id):
    print("Database: members id ", members_id)
    cursor.execute("DELETE FROM `members` WHERE `id`=%s",members_id)
    con.commit()
    return True
    
def update_members(updated_members_details):
    print("Database: updated members details ",updated_members_details)
    try:
        cursor.execute("UPDATE `members` SET `Name`=%s, `Phone_no`=%s, `Designation`=%s, `Address`=%s WHERE `id`=%s",updated_members_details)
        con.commit()
        return True
    except:
        return False

def members_login(members_details):
    cursor.execute("select * from members where username=%s and password=%s",members_details)
    return cursor.fetchone()


def add_order_info(showOrder):
    try:
        cursor.execute("INSERT INTO orders (table_no,food_code,quantity,total_bill,status) VALUES(%s,%s,%s,%s,%s)",showOrder)
        con.commit()
        return True
    except mysql.connector.Error as error:
        print("Error - ",error)
        return False

def show_all_order():
    cursor.execute("SELECT * FROM `orders`")
    return cursor.fetchall()

def delete_order_info(order_id):
    print("Database: order id ", order_id)
    cursor.execute("DELETE FROM `orders` WHERE `id`=%s",order_id)
    con.commit()
    return True
    
def update_order(updated_order_details):
    print("Database: updated order details ",updated_order_details)
    try:
        cursor.execute("UPDATE `orders` SET `table_no`=%s,`food_code`=%s,`quantity`=%s,`total_bill`=%s WHERE `id`=%s",updated_order_details)
        con.commit()
        return True
    except:
        return False

