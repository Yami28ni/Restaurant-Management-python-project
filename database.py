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
