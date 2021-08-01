import sqlite3,os
from tkinter import *
from tkinter import ttk,messagebox
bill_font = ("BOLD",12)
customer_conn = ""
main_color = "LightSkyBlue4"



def show_help():
    
    command=''
    master=Tk()
    master.geometry('1345x700+10+10')
    master.title('Bill Details Manager')
    main_label=LabelFrame(master,bg=main_color,relief=RIDGE,bd=10)
    main_label.pack(fill=BOTH,expand=1)
    y_scroll=Scrollbar(main_label)
    y_scroll.pack(side=RIGHT,fill=Y)
    
    listbox=Listbox(main_label,yscrollcommand=y_scroll.set,selectforeground='black',selectbackground='white')
    listbox.pack(side=TOP,fill=BOTH,expand=1)

    y_scroll.config(command=listbox.yview)


    listbox.insert(END,'(1) HOW TO USE IT :-')
    listbox.insert(END,'')
    listbox.insert(END,' > Open the application, enter the Correct User-Name and Password, wrong Password will deny your request !')
    listbox.insert(END,' > The application is divided into 3 frames.')
    listbox.insert(END,'')
    listbox.insert(END,'')

    listbox.insert(END,'(2) Frame 1 :-')
    listbox.insert(END,'')
    listbox.insert(END,' > Add the data of customer in New Bill Frame (Left-most Frame)')
    listbox.insert(END,' > For more convinience, Go to customer menu and click on  \'New Customer\' and enter the following details :-')
    listbox.insert(END,'')
    listbox.insert(END,'    : Customer Name  :   000000000000 ')
    listbox.insert(END,'    : Phone No.  :   0000000000 ')
    listbox.insert(END,'    : City  :   000000 ')
    listbox.insert(END,'')
    listbox.insert(END,' > And click on save button! .')
    listbox.insert(END,' > Now you have the Unique customer ID and you can directly enter the ID in the Entry Widget and the application will fill the')
    listbox.insert(END,' > the details of respective customer for you !')
    listbox.insert(END,'')
    listbox.insert(END,'')

    listbox.insert(END,'(3) Frame 2 :-')
    listbox.insert(END,'')
    listbox.insert(END,' > This is the live frame of the application.')
    listbox.insert(END,' > It will tell you the current time, date, sales, bills made and number of products sold !')
    listbox.insert(END,'')
    listbox.insert(END,'')

    listbox.insert(END,'(4) Frame 3 :-')
    listbox.insert(END,'')
    listbox.insert(END,' > To enter the products in list')
    listbox.insert(END,' > click on th \'+\' sign button and add the asked details about the product and click on insert.')
    listbox.insert(END,' > If you want the modify the details of a product then select the particular product and click on edit.')
    listbox.insert(END,' > If you want the delete a product then select the particular product and click on delete.')
    listbox.insert(END,' > When you are done, click on \'Print Bill\' Button it will calculate the total amount and total numer of products.')
    listbox.insert(END,' > THe success notification will print on the screen and bill will be printed in the folder name with current month name.')
    listbox.insert(END,'')
    listbox.insert(END,'')

    listbox.insert(END,'(5) FOR MORE QURIES :-')
    listbox.insert(END,' > Contact us :-    Email:- khushalaniaman1@gmail.com')
    listbox.insert(END,' >                            LinkedIn:-  Aman Khushalani ( www.linkedin.com/in/aman-khushalani-1b774818b )')
    listbox.insert(END,' >                            Whatsapp :- +91 8505069888')
    listbox.insert(END,'')
    listbox.insert(END,'')
    listbox.insert(END,'')
    listbox.insert(END,'')
    


    master.mainloop()

#show_help()

def show_about():

    command=''
    master=Toplevel()
    master.geometry('330x200')
    master.maxsize(width=340,height=200)
    master.minsize(width=340,height=200)
    # master.wm_iconbitmap(icon_address)
    main_label=LabelFrame(master,bg="LightSkyBlue3",relief=RIDGE,bd=10)
    main_label.pack(fill=BOTH,expand=1)
    Label(main_label,text='Retail Sales Manager',bg="LightSkyBlue3",font=('arial',15,'bold')).pack(side=TOP,pady=10)
    Label(main_label,text='Unregistered',bg="LightSkyBlue3").pack(side=TOP,)
    Label(main_label,text='Copyright © 2021   ~Aman Khushalani\n Version 1.1.0',bg="LightSkyBlue3",font=(13)).pack(side=TOP,pady=20)
    master.mainloop()


# To create a new customer id database
def create_customer_database():
    global customer_conn
    if(customer_conn ==""):
        customer_conn = sqlite3.connect("Reserved_Customer.db")
    # customer_conn = sqlite3.connect("Reserved_Customer.db")
    customer_conn.execute("""
        CREATE TABLE CUSTOMER(
            CUSTOMER_ID TEXT PRIMARY KEY,
            CUSTOMER_NAME TEXT,
            PHONE_NO INT,
            CITY TEXT
        );        
    """)
    customer_conn.commit()
    customer_conn.close()


# to get the unique customer id for new customer
def get_number():
    global customer_conn
    if(customer_conn ==""):
        customer_conn = sqlite3.connect("Reserved_Customer.db")
    customer_conn = sqlite3.connect("Reserved_Customer.db")
    values = len(list(customer_conn.execute("SELECT * FROM CUSTOMER;")))
    customer_conn.close()
    customer_conn = ""
    return values

def get_unique_customer_id():
    global customer_conn
    customer_conn = sqlite3.connect("Reserved_Customer.db")
    values = customer_conn.execute("SELECT * FROM CUSTOMER;")

    if(get_number() == 0):
        custo_id = "CUSTO_1"    
    else:
        custo_id =  "CUSTO_"+str(get_number()+1)

    if(customer_conn != ""):
        customer_conn.close()
        customer_conn = ""
    return custo_id





# to add new customer details
def add_new_customer():

    def save_details():
        global customer_conn
        if(customer_conn == ""):
            customer_conn = sqlite3.connect("Reserved_Customer.db")
        customer_conn.execute(f"""
            INSERT INTO CUSTOMER(CUSTOMER_ID ,CUSTOMER_NAME ,PHONE_NO ,CITY)
            VALUES("{c_id.get()}","{c_name.get()}",{int(p_no.get())},"{city.get()}");
        """)
        customer_conn.commit()
        messagebox.showinfo(title="New Customer !",message="Inserted successfully !")
        # customer_conn.close()
        # customer_conn = ""
        root.destroy()


    if(os.path.exists("Reserved_Customer.db")==False):
        answer = messagebox.askyesno(title="Customer Database",message="Customer Database not exists,\nDo you want to create a new Database..?")
        if(answer==True):
            create_customer_database()
        else:
            return 0;
    
    root = Toplevel()
    root.geometry("650x300")
    root.title("New Customer Pannel")

    mainFrame = LabelFrame(root,text="Detail Form",bg=main_color,bd=5)
    mainFrame.pack(side=TOP,fill=BOTH,expand=1)

    Label(mainFrame,text="Customer ID       :- ",font=bill_font,bg=main_color).place(x=10,y=10)
    Label(mainFrame,text="Customer Name :- ",font=bill_font,bg=main_color).place(x=10,y=60)
    Label(mainFrame,text="Phone No.           :- ",font=bill_font,bg=main_color).place(x=10,y=110)
    Label(mainFrame,text="City                     :- ",font=bill_font,bg=main_color).place(x=10,y=160)

        

    c_id = Entry(mainFrame)
    c_id.place(x=190,y=10)
    c_id.insert(0,get_unique_customer_id())
    c_id.configure(state="readonly")
        
    c_name = Entry(mainFrame)
    c_name.place(x=190,y=60)
        
    p_no = Entry(mainFrame)
    p_no.place(x=190,y=110)
        
    city = Entry(mainFrame)
    city.place(x=190,y=160)

    Button(mainFrame,text="Save !",width=10,command=save_details,bg="slategray3",activebackground="slategray2").place(x=20,y=210)

    root.mainloop()
































#to show customer details !
def show_customer_details():

    def get_tuple(conn):
        names=conn.execute('PRAGMA table_info(CUSTOMER);')
        a_tuple=()
        for i in names:
            a_tuple+=(i[1],)
        return a_tuple
    
    def put_heading(tree,a_tuple):
        i=0
        while i<len(a_tuple):
            tree.column(i)
            tree.heading(i,text=a_tuple[i])
            i+=1
        tree['show']='headings'


    # ============================== EDIT CUSTOMER ====================================
    def Edit_customer(conn):

        def upadte_details():
            conn.execute(f'''UPDATE CUSTOMER SET 
                    CUSTOMER_NAME = "{c_name.get()}",
                    PHONE_NO = {int(p_no.get())},
                    CITY = "{city.get()}"
                    WHERE CUSTOMER_ID = "{c_id.get()}";
            ''')
            conn.commit()
            messagebox.showinfo(title="Upadte Details",message="Details Updated Successfully !")
            root.destroy()
            update_tree(conn)
            conn.close()
            return

        values = list(tree.item(tree.selection())['values'])
        if(values!=[]):
            root = Toplevel()
            root.geometry("650x300")
            root.title("New Customer Pannel")

            mainFrame = LabelFrame(root,text="Detail Form",bg=main_color,bd=5)
            mainFrame.pack(side=TOP,fill=BOTH,expand=1)

            Label(mainFrame,text="Customer ID       :- ",font=bill_font,bg=main_color).place(x=10,y=10)
            Label(mainFrame,text="Customer Name :- ",font=bill_font,bg=main_color).place(x=10,y=60)
            Label(mainFrame,text="Phone No.           :- ",font=bill_font,bg=main_color).place(x=10,y=110)
            Label(mainFrame,text="City                     :- ",font=bill_font,bg=main_color).place(x=10,y=160)

            

            c_id = Entry(mainFrame)
            c_id.place(x=190,y=10)
            c_id.insert(0,values[0])
            
            c_name = Entry(mainFrame)
            c_name.place(x=190,y=60)
            c_name.insert(0,values[1])
            
            p_no = Entry(mainFrame)
            p_no.place(x=190,y=110)
            p_no.insert(0,values[2])
            
            city = Entry(mainFrame)
            city.place(x=190,y=160)
            city.insert(0,values[3])

            Button(mainFrame,text="Upadte Details !",width=13,command=upadte_details,bg="slategray3",activebackground="slategray2").place(x=20,y=210)

            root.mainloop()

    


    
    def edit_temp(event):
        Edit_customer(conn)
    def delete_temp(event):
        values = list(tree.item(tree.selection())['values'])
        if(values!=[]):
            tree.delete(tree.selection())
            conn.execute(f'DELETE FROM CUSTOMER WHERE CUSTOMER_ID = "{values[0]}"')
            conn.commit()
            messagebox.showinfo(title="Delete CUstomer",message="Deleted Successfully !")


    def put_buttons(root):
        button_frame = LabelFrame(root,bg=main_color,height=40,bd=5)
        button_frame.pack(side=BOTTOM,fill=X)
        
        btn_edit = Button(button_frame,text="Edit !",width=10,bg="slategray3",activebackground="slategray2")
        btn_edit.pack(side=LEFT,padx=10,pady=5)
        btn_edit.bind('<Button-1>',edit_temp)
        
        btn_delete = Button(button_frame,text="Delete !",width=10,bg="slategray3",activebackground="slategray2")
        btn_delete.pack(side=LEFT,padx=10,pady=5)
        btn_delete.pack(side=LEFT,padx=10,pady=5)
        btn_delete.bind('<Button-1>',delete_temp)

    
    # Update Tree
    def update_tree(conn):
        for i in tree.get_children():
            tree.delete(i)

        result=conn.execute('SELECT * FROM CUSTOMER')
        count=0
        for i in result:
            tree.insert('',count,values=i)
            count+=1



    if(os.path.exists("Reserved_Customer.db")==False):
        answer = messagebox.askyesno(title="Customer Database",message="Customer Database not exists,\nDo you want to create a new Database..?")
        if(answer==True):
            create_customer_database()
        else:
            return 0;


    conn = sqlite3.connect("Reserved_Customer.db")
    values = conn.execute("SELECT * FROM CUSTOMER;")

    root = Tk()
    root.geometry("800x670")
    root.title("Reserved Customer Details")
    root.minsize(width=800,height=670)
    root.maxsize(width=800,height=670)
        

    a_tuple = get_tuple(conn)
    x_scroll=Scrollbar(root,orient=HORIZONTAL)
    x_scroll.pack(side=BOTTOM,fill=X)
    y_scroll=Scrollbar(root,orient=VERTICAL)
    y_scroll.pack(side=RIGHT,fill=Y)
    tree=ttk.Treeview(root,columns=a_tuple,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    tree.pack(side=TOP,fill=BOTH,expand=1)

    x_scroll.config(command=tree.xview)
    y_scroll.config(command=tree.yview)

    put_heading(tree,a_tuple)
    put_buttons(root)
    update_tree(conn)

    root.mainloop()

    conn.close()
    

#add_new_customer(["Heena_Khushalani",9928018333,"Kishangarh"])
# add_new_customer(["Aman_Khushalani",8505069888,"Kishangarh"])
# add_new_customer(["Rajesh_Khushalani",9928586265,"Kishangarh"])
os.system("clear")
#show_customer_details()
#add_new_customer()








































# def create():
#     conn = sqlite3.connect('aman.db')
#     conn.execute('CREATE TABLE PRODUCTS(PRODUCT_ID INT PRIMARY KEY, NAME TEXT, AVAILABLE_QUANTITY INT);')
#     conn.commit()
#     conn.close()


# def show():
#     conn = sqlite3.connect('aman.db')
#     values = conn.execute('SELECT * FROM PRODUCTS;')
#     if(len(list(values))==0):
#         conn.close()
#         return False
#     else:
#         values = conn.execute('SELECT * FROM PRODUCTS;')
#         for i in values:
#             print(i)
#     conn.close()




# def length_of_values():
#     conn = sqlite3.connect('aman.db')
#     values = conn.execute('SELECT * FROM PRODUCTS;')
#     if(len(list(values))==0):
#         conn.close()
#         return False
#     else:
#         conn.close()
#         return True

    


# def insert(product_name,available_quantity):

#     def check_exists(product_name):
#         conn = sqlite3.connect('aman.db')
#         values = list(conn.execute('SELECT * FROM PRODUCTS;'))
#         for item in values:
#             if(item[1]==product_name):
#                 return True
#         conn.close()
#         return False

#     def get_unique():
#         conn = sqlite3.connect('aman.db')
#         values = list(conn.execute('SELECT * FROM PRODUCTS;'))
#         if(len(values)==0):
#             answer = 111
#         else:
#             answer = values[len(values)-1][0] + 1
#         conn.close()

#         return answer

#     def insert_values(product_name,available_quantities,unique_id):
#         conn = sqlite3.connect('aman.db')
#         conn.execute(f'INSERT INTO PRODUCTS(PRODUCT_ID , NAME , AVAILABLE_QUANTITY ) VALUES({unique_id},"{product_name}",{available_quantities});')
#         conn.commit()
#         print(f"New Product added Successfully with Product_ID = {unique_id} !")
#         conn.close()
        

#     if(check_exists(product_name)):
#         print("Product with same name already available !")
#     else:
#         insert_values(product_name,available_quantity,get_unique())






# def search_product(product_id):
#         conn = sqlite3.connect('aman.db')
#         values = conn.execute("SELECT * FROM PRODUCTS;")
#         for i in values:
#             if(i[0]==product_id):
#                 conn.close()
#                 return True
#         conn.close()
#         return False


# def delete_product():

#     def delete_it(product_id):
#         if search_product(product_id)== True:
#             conn = sqlite3.connect('aman.db')
#             conn.execute(f"DELETE FROM PRODUCTS WHERE PRODUCT_ID = {product_id};")
#             conn.commit()
#             conn.close()
#             print("Product Deleted Successfully !")
#         else:
#             print("Invalid Product ID !")

#     if length_of_values()==False:
#         print("Nothing to Delete !")
#     else:
#         product_id = int(input("\n\nEnter the Product ID to delete() = "))
#         delete_it(product_id)


# def modify_product():
#     if length_of_values()==False:
#         print("Nothing to Modify !")
#     else:
#         product_id = int(input("\n\nEnter the Product ID to delete() = "))
#         if(search_product(product_id)==True):
#             pass
#         else:
#             print("Invalid Product ID !")


























































conn_product = ""


# # To create a new product id database
# def create_product_database():
#     conn = sqlite3.connect("Reserved_Product.db")
#     conn.execute('CREATE TABLE PRODUCTS(PRODUCT_ID TEXT PRIMARY KEY, PRODUCT_NAME TEXT,PRICE INT, AVAILABLE_QUANTITY INT);')
#     conn.commit()
#     conn.close()



# # to add new product details
# def add_new_product():

#     def save_details():
#         global conn_product
#         if(conn_product==""):
#             conn_product = sqlite3.connect("Reserved_Product.db")
#         try:
#             conn_product.execute(f"""
#                 INSERT INTO PRODUCTS(PRODUCT_ID ,PRODUCT_NAME ,PRICE ,AVAILABLE_QUANTITY)
#                 VALUES("{product_id.get()}","{product_name.get()}",{int(price.get())},{int(a_quantity.get())});
#             """)
#             conn_product.commit()
#             messagebox.showinfo(title="New Product !",message="Inserted successfully !")
#         except Exception as e:
#             if(str(e) == "UNIQUE constraint failed: PRODUCTS.PRODUCT_ID"):
#                 messagebox.showerror(title="New Product !" ,message="Take a Unique ID for your \nProduct !")
#         finally:            
#             conn_product.close()
#             conn_product = ""
#             root.destroy()


#     if(os.path.exists("Reserved_Product.db")==False):
#         answer = messagebox.askyesno(title="Product Database",message="Product Database not exists,\nDo you want to create a new Database..?")
#         if(answer==True):
#             create_product_database()
#         else:
#             return 0;
#     else:

#         root = Toplevel()
#         root.geometry("650x300")
#         root.title("New Product Pannel")

#         mainFrame = LabelFrame(root,text="Detail Form",bg="RED",bd=5)
#         mainFrame.pack(side=TOP,fill=BOTH,expand=1)

#         Label(mainFrame,text="Product ID       :- ",font=bill_font).place(x=10,y=10)
#         Label(mainFrame,text="Product Name :- ",font=bill_font).place(x=10,y=60)
#         Label(mainFrame,text="Price           :- ",font=bill_font).place(x=10,y=110)
#         Label(mainFrame,text="Available Quantity      :- ",font=bill_font).place(x=10,y=160)

        

#         product_id = Entry(mainFrame)
#         product_id.place(x=190,y=10)
        
#         product_name = Entry(mainFrame)
#         product_name.place(x=190,y=60)
        
#         price = Entry(mainFrame)
#         price.place(x=190,y=110)
        
#         a_quantity = Entry(mainFrame)
#         a_quantity.place(x=190,y=160)

#         Button(mainFrame,text="Save !",width=10,command=save_details).place(x=20,y=210)

#         root.mainloop()





























# #to show customer details !
# def show_product_details():

#     def get_tuple(conn):
#         names=conn.execute('PRAGMA table_info(PRODUCTS);')
#         a_tuple=()
#         for i in names:
#             a_tuple+=(i[1],)
#         return a_tuple
    
#     def put_heading(tree,a_tuple):
#         i=0
#         while i<len(a_tuple):
#             tree.column(i)
#             tree.heading(i,text=a_tuple[i])
#             i+=1
#         tree['show']='headings'


#     # ============================== EDIT CUSTOMER ====================================
#     def Edit_products(conn):
#             # CUSTOMER_ID TEXT PRIMARY KEY,
#             # CUSTOMER_NAME TEXT,
#             # PHONE_NO INT,
#             # CITY TEXT

#         def upadte_details():
#             conn.execute(f'''UPDATE PRODUCTS SET 
#                     PRODUCT_NAME = "{product_name.get()}",
#                     PRICE = {int(price.get())},
#                     AVAILABLE_QUANTITY = "{a_quantity.get()}"
#                     WHERE PRODUCT_ID = "{product_id.get()}";
#             ''')
#             conn.commit()
#             messagebox.showinfo(title="Upadte Details",message="Details Updated Successfully !")
#             root.destroy()
#             update_tree(conn)
#             return

#         values = list(tree.item(tree.selection())['values'])
#         if(values!=[]):
#             root = Toplevel()
#             root.geometry("650x300")
#             root.title("New Customer Pannel")

#             mainFrame = LabelFrame(root,text="Detail Form",bg="RED",bd=5)
#             mainFrame.pack(side=TOP,fill=BOTH,expand=1)

#             Label(mainFrame,text="Product ID       :- ",font=bill_font).place(x=10,y=10)
#             Label(mainFrame,text="Product Name :- ",font=bill_font).place(x=10,y=60)
#             Label(mainFrame,text="Price           :- ",font=bill_font).place(x=10,y=110)
#             Label(mainFrame,text="Available Quantity                     :- ",font=bill_font).place(x=10,y=160)

            

#             product_id = Entry(mainFrame)
#             product_id.place(x=190,y=10)
#             product_id.insert(0,values[0])
#             product_id.configure(state="readonly")
            
#             product_name = Entry(mainFrame)
#             product_name.place(x=190,y=60)
#             product_name.insert(0,values[1])
            
#             price = Entry(mainFrame)
#             price.place(x=190,y=110)
#             price.insert(0,values[2])
            
#             a_quantity = Entry(mainFrame)
#             a_quantity.place(x=190,y=160)
#             a_quantity.insert(0,values[3])

#             Button(mainFrame,text="Upadte Details !",width=13,command=upadte_details).place(x=20,y=210)

#             root.mainloop()

    


    
#     def edit_temp(event):
#         Edit_products(conn_product)
    
#     def delete_temp(event):
#         values = list(tree.item(tree.selection())['values'])
#         if(values!=[]):
#             tree.delete(tree.selection())
#             conn_product.execute(f'DELETE FROM PRODUCTS WHERE PRODUCT_ID = "{values[0]}"')
#             conn_product.commit()
#             messagebox.showinfo(title="Delete Product",message="Deleted Successfully !")


#     def put_buttons(root):
#         button_frame = LabelFrame(root,bg="RED",height=40,bd=5)
#         button_frame.pack(side=BOTTOM,fill=X)
        
#         btn_edit = Button(button_frame,text="Edit !",width=10)
#         btn_edit.pack(side=LEFT,padx=10,pady=5)
#         btn_edit.bind('<Button-1>',edit_temp)
        
#         btn_delete = Button(button_frame,text="Delete !",width=10)
#         btn_delete.pack(side=LEFT,padx=10,pady=5)
#         btn_delete.bind('<Button-1>',delete_temp)

    
#     # Update Tree
#     def update_tree(conn):
#         for i in tree.get_children():
#             tree.delete(i)

#         result=conn.execute('SELECT * FROM PRODUCTS')
#         count=0
#         for i in result:
#             tree.insert('',count,values=i)
#             count+=1



#     if(os.path.exists("Reserved_Product.db")==False):
#         answer = messagebox.askyesno(title="Products Database",message="Products Database not exists,\nDo you want to create a new Database..?")
#         if(answer==True):
#             create_customer_database()
#         else:
#             return 0;

#     global conn_product
#     if(conn_product==""):
#         conn_product = sqlite3.connect("Reserved_Product.db")
#     values = conn_product.execute("SELECT * FROM PRODUCTS;")

#     root = Toplevel()
#     root.geometry("800x670")
#     root.title("Reserved Products Details")
#     root.minsize(width=800,height=670)
#     root.maxsize(width=800,height=670)
        

#     a_tuple = get_tuple(conn_product)
#     x_scroll=Scrollbar(root,orient=HORIZONTAL)
#     x_scroll.pack(side=BOTTOM,fill=X)
#     y_scroll=Scrollbar(root,orient=VERTICAL)
#     y_scroll.pack(side=RIGHT,fill=Y)
#     tree=ttk.Treeview(root,columns=a_tuple,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
#     tree.pack(side=TOP,fill=BOTH,expand=1)

#     x_scroll.config(command=tree.xview)
#     y_scroll.config(command=tree.yview)

#     put_heading(tree,a_tuple)
#     put_buttons(root)
#     update_tree(conn_product)

#     root.mainloop()

#     if(conn_product!=""):
#         conn_product.close()
    

