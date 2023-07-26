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