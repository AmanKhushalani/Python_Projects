from tkinter import * 
from datetime import datetime
from prettytable import PrettyTable
from tkinter import messagebox,ttk
import os,sqlite3
from time import strftime

x = PrettyTable()
x.field_names = ["P/No." , "Product Name", "Quantity Taken", "Total Price"]
bill_font = ("BOLD",12)
main_color = "LightSkyBlue4"

total_bill_made_today = 0
final_bill_number = ""
final_bill_date = str(datetime.today().date())
total_items = 0
total_price = 0
fina_customer_id = ""
final_customer_name = ""
final_city = ""
final_phone_no = 0
final_product_database_name = ""
                # BILL_NUMBER TEXT PRIMARY KEY,
                # CUSTOMER_ID TEXT,
                # CUSTOMER_NAME TEXT,
                # PHONE_NO INT,
                # CITY TEXT,
                # BILL_DATE TEXT,
                # TOTAL_ITEMS_PURCHASED INT,
                # TOTAL_PAYMENT INT);




def mainpage(root):



    #------------------------- FRAME 1 ---------------------------------------
    def make_bill():
        global x
        lines = [
            "\nBill Number   = "+final_bill_number,
            "\nCustomer_name = "+final_customer_name,
            "\nPhone No      = "+str(final_phone_no),
            "\nDate          = "+str(final_bill_date),
            "\nCity          = "+str(final_city),
            "\nTotal Items   = "+str(total_items),
            "\nTotal Payment = "+str(total_price)+"\n\n",
            str(x)
        ]
        months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        name ="Bills/" + months[datetime.today().month]
        
        if os.path.exists(name) == False:
            os.makedirs(name)


        if(os.path.exists("Bills/"+name+"/"+final_bill_number+".txt") == False):
            file_object = open(name+"/"+final_bill_number+".txt" , "a")

            file_object.writelines(lines)

            file_object.close()


    def _bill_name_generate():
        months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        name = months[datetime.today().month] +"_"+ str(datetime.today().year)
        return str(name)+"_bill.db"
        
    def get_last_id():
        conn = sqlite3.connect(_bill_name_generate())
        value = str(1000+len(list(conn.execute("SELECT BILL_NUMBER FROM BILL;"))))
        conn.close()
        return value


    
    def state_bill_number():
        global final_bill_number
        bill_number.configure(text = "Bill Number:- #"+get_last_id())

        final_bill_number = get_last_id()
    
    # Final function
    def final_function():
        global total_bill_made_today ,final_bill_number ,final_bill_date,x
        global total_items ,total_price ,fina_customer_id ,final_customer_name
        global final_city ,final_phone_no , final_product_database_name

        # /////////////////// Update Generate /////////////////////
        conn = sqlite3.connect(_bill_name_generate())
        conn.execute(f"""
            INSERT INTO BILL(
                BILL_NUMBER , CUSTOMER_NAME , PHONE_NO, CITY, BILL_DATE, 
                TOTAL_ITEMS_PURCHASED , TOTAL_PAYMENT
            )
            VALUES(
                "{final_bill_number}","{final_customer_name}",
                {final_phone_no},"{final_city}","{final_bill_date}",
                {total_items},{total_price}
            );
        """)
        conn.commit()
        conn.close()

        # /////////////////// Revenue Generate /////////////////////
        conn = sqlite3.connect(_rev_name_generate())
        values = list(conn.execute(f"""SELECT * FROM MONTHLY_REV WHERE DATES = "{datetime.today().date()}"; """))
        initial_items = values[0][1]
        initial_income= values[0][2]
        initial_bills = values[0][3]
        
        conn.execute(f"""
            UPDATE MONTHLY_REV SET TOTAL_ITEMS_SOLD = {initial_items+total_items},
                                   TOTAL_INCOME_MADE = {initial_income+total_price},
                                   TOTAL_BILLS_MADE  = {initial_bills+1}
            WHERE DATES = "{datetime.today().date()}";
        """)

        conn.commit()
        conn.close()

        # ////////////////////// Products sold details updation ///////////////////////////////////

            # conn.execute("""CREATE TABLE PRODUCTS_BILL(
            #     BILL_NUMBER TEXT,
            #     CUSTOMER_NAME TEXT,
            #     PRODUCT_NAME TEXT,
            #     QUANTITY_TAKEN INT,
            #     PRICE INT
            # )""")
        
        counter = 1
        conn = sqlite3.connect(final_product_database_name)
        for i in tree.get_children():
            values = list(tree.item(i)['values'])
            conn.execute(f"""INSERT INTO PRODUCTS_BILL(
                BILL_NUMBER , CUSTOMER_NAME , PRODUCT_NAME , QUANTITY_TAKEN , PRICE)
                VALUES("#{final_bill_number}","{final_customer_name}",
                "{values[0]}",{values[1]},{values[1]*values[2]});
             """)
            x.add_row([counter,values[0],values[1],values[1]*values[2]])
            conn.commit()
        conn.close()
        
        
        make_bill()
        messagebox.showinfo(title="Product Bill",message="Bill generated successfully !")
        state_bill_number()
        clear_all_entries()
        clear_tree()
        update_revenue()

    def clear_tree():
        for i in tree.get_children():
            tree.delete(i)

    def fill_form():
        fill = False
        if(os.path.exists("Reserved_Customer.db")==True and customer_id.get()!=""):
            conn = sqlite3.connect("Reserved_Customer.db")
            values = conn.execute("SELECT * FROM CUSTOMER;")
            for i in values:
                if(customer_id.get().upper()==i[0]):
                    fill = True
                    cname.delete(0,END)
                    pno.delete(0,END)
                    city.delete(0,END)
                    cname.insert(0,i[1])
                    pno.insert(0,i[2])
                    city.insert(0,i[3])
                    break
            if(fill==False):
                messagebox.showerror(title="Fill Form",message="Customer ID not Found !")
        

            
    
    def check_bills():
        # It will contain just the total of a bill
        if(os.path.exists(_bill_name_generate())==False):
            conn = sqlite3.connect(_bill_name_generate())
            conn.execute("""CREATE TABLE BILL(
                BILL_NUMBER TEXT PRIMARY KEY,
                CUSTOMER_NAME TEXT,
                PHONE_NO INT,
                CITY TEXT,
                BILL_DATE TEXT,
                TOTAL_ITEMS_PURCHASED INT,
                TOTAL_PAYMENT INT);
            """)
            conn.execute(f"""
                INSERT INTO BILL(BILL_NUMBER)
                VALUES("#{1000}");
            """)
            conn.commit()
            conn.close()
        
    def submit_customer_details():
        if(cname.get()=="" or pno.get()=="" or city.get()==""):
            messagebox.showerror(title="Customer Details",message="Fill all the details about customer !")
            return 0
        global fina_customer_id,final_customer_name,final_city,final_phone_no
        final_customer_name = cname.get()
        final_customer_id = customer_id.get()
        final_city = city.get()

        if len(str(pno.get())) == 10:
            try:
                final_phone_no = int(pno.get())
            except:
                messagebox.showerror(title="Customer Details",message="Phone No. might be wrong !")
                return 0
        else:
            messagebox.showerror(title="Customer Details",message="Phone No. might be wrong !")
            return 0
    
        return 1

    def clear_all_entries():
        cname.delete(0,END)
        pno.delete(0,END)
        city.delete(0,END)
        customer_id.delete(0,END)
        t_items.configure(state="normal")
        t_items.delete(0,END)
        t_items.configure(state="readonly")
        t_payment.configure(state="normal")
        t_payment.delete(0,END)
        t_payment.configure(state="readonly")
        



    Frame1 = LabelFrame(root, text="New Bill" ,width=600, bd=5, background=main_color)
    Frame1.pack(side=LEFT, fill=Y)

    

    # Bill Number
    bill_number = Label(Frame1, font=("BOLD",20),bg=main_color)
    bill_number.place(x=20,y=10)
    
    Label(Frame1,text="Fill by ID ?                :- ",font=bill_font,bg=main_color).place(x=30,y=120)
    customer_id = Entry(Frame1,)
    customer_id.place(x=250,y=120)
    Button(Frame1,text="Fill by ID",width=10,command=fill_form,background="slategray3",activebackground="slategray2").place(x=450,y=118)
    
    Label(Frame1,text="Customer Name      :- ",font=bill_font,background=main_color).place(x=30,y=160)
    Label(Frame1,text="Phone No                 :- ",font=bill_font,background=main_color).place(x=30,y=200)
    Label(Frame1,text="City                          :- ",font=bill_font,background=main_color).place(x=30,y=240)
    Label(Frame1,text="Date                         :- ",font=bill_font,background=main_color).place(x=30,y=280)
    Label(Frame1,text="Total Items              :- ",font=bill_font,background=main_color).place(x=30,y=320)
    Label(Frame1,text="Total Payment         :- ",font=bill_font,background=main_color).place(x=30,y=360)
    
    
    cname = Entry(Frame1,)
    cname.place(x=250,y=160)
    
    pno = Entry(Frame1)
    pno.place(x=250,y=200)

    city = Entry(Frame1)
    city.place(x=250,y=240)

    date = Entry(Frame1)
    date.place(x=250,y=280)
    date.insert(0,datetime.today().date())
    date.configure(state="readonly")

    t_items = Entry(Frame1,state="readonly")
    t_items.place(x=250,y=320)

    t_payment = Entry(Frame1,state="readonly")
    t_payment.place(x=250,y=360)

    # submit = Button(Frame1,text="Submit",width=10,command=submit_customer_details,bg="slategray3",activebackground="slategray2")
    # submit.place(x=30,y=400)
    
    clear_all = Button(Frame1,text="Clear",width=10,command=clear_all_entries,bg="slategray3",activebackground="slategray2")
    clear_all.place(x=30,y=400)
    
    exit_button = Button(Frame1,text="Exit !",width=10,command=root.destroy,bg="slategray3",activebackground="slategray2")
    exit_button.place(x=160,y=400)


    check_bills()
    state_bill_number()
    
















    #------------------------- FRAME 2 ---------------------------------------
    def _rev_name_generate():
        months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        name = months[datetime.today().month] +"_"+ str(datetime.today().year)
        return str(name)+"_revenue.db"
    
    # this will contain the revenue of the current date
    def create_monthly_revenue():
        conn = sqlite3.connect(_rev_name_generate())
        conn.execute("""CREATE TABLE MONTHLY_REV(
            DATES TEXT PRIMARY KEY,
            TOTAL_ITEMS_SOLD INT,
            TOTAL_INCOME_MADE INT,
            TOTAL_BILLS_MADE INT);
            """)

        conn.execute(f"""
            INSERT INTO MONTHLY_REV(DATES,TOTAL_ITEMS_SOLD,TOTAL_INCOME_MADE,TOTAL_BILLS_MADE )
            VALUES("{datetime.today().date()}",0,0,0);
        """)

        conn.commit()
        conn.close()
        

    def check_revenue():
        if(os.path.exists(_rev_name_generate())==False):
            create_monthly_revenue()
        else:
            conn = sqlite3.connect(_rev_name_generate())
            date = list(conn.execute("SELECT * FROM MONTHLY_REV;"))
            if(date[len(date)-1][0] == str(datetime.today().date()) == False):
                        conn.execute(f"""
                INSERT INTO MONTHLY_REV(DATES,TOTAL_ITEMS_SOLD,TOTAL_INCOME_MADE,TOTAL_BILLS_MADE )
                VALUES("{datetime.today().date()}",0,0,0);
            """)

            conn.close()

    def update_revenue():

        conn = sqlite3.connect(_rev_name_generate())
        values = list(conn.execute(f"SELECT * FROM MONTHLY_REV WHERE DATES = '{datetime.today().date()}';"))
        if(values==[]):
            conn.execute(f"""
                INSERT INTO MONTHLY_REV(DATES,TOTAL_ITEMS_SOLD,TOTAL_INCOME_MADE,TOTAL_BILLS_MADE )
                VALUES("{datetime.today().date()}",0,0,0);""")
            values = list(conn.execute(f"SELECT * FROM MONTHLY_REV WHERE DATES = '{datetime.today().date()}';"))[0]
        else:
            values = values[0]

        revenue_font = ("BOLD",15)
        Label(Frame2,text="Total Products Sold = \t"+str(values[1]),font=revenue_font,bg=main_color).place(x=15,y=20)
        Label(Frame2,text="Total Sale                 = \t"+str(values[2]),font=revenue_font,bg=main_color).place(x=15,y=70)
        Label(Frame2,text="Total Bills Made       = \t"+str(values[3]),font=revenue_font,bg=main_color).place(x=15,y=120)

        conn.close()


    
    Frame2 = LabelFrame(root, text="Daily Revenue" ,height=220, bd=5, bg=main_color)
    Frame2.pack(side=TOP,fill=X)    

    live_frame = LabelFrame(Frame2 ,bg="LightSkyBlue3", bd=5 ,width=250,height=120)
    live_frame.place(x=480,y=20)

    Label(live_frame,text="Date = "+str(datetime.today().date()),bg="LightSkyBlue3", font=("BOLD",15)).place(x=20,y=10)

    def change_time():
        current_time = "Time = "+strftime("%H:%M:%S")
        time_label.configure(text = current_time)
        time_label.after(1000,change_time)
    time_label = Label(live_frame,text="Time = "+str(strftime("%H:%M:%S")),bg="LightSkyBlue3",font=("BOLD",15))
    time_label.place(x=20,y=70)
    time_label.after(1000,change_time)

    check_revenue()
    update_revenue()
    
    
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    














    #------------------------- FRAME 3 ---------------------------------------


    def edit_product_window():
        def update_tree():
            existing_values = []
            for i in tree.get_children():
                if(str(i) == tree.selection()[0]):
                    existing_values.append( (f"{p_name.get()}",int(p_quantity.get()),int(price.get())))
                else:
                    existing_values.append(tuple(tree.item(i)['values']))
            
            for i in tree.get_children():
                tree.delete(i)

            count=0
            for i in existing_values:
                tree.insert('',count,values=i)
                count+=1
            
            root.destroy()


        values = list(tree.item(tree.selection())['values'])
        if(values!=[]):
            root = Toplevel()
            root.geometry("650x300")
            root.title("New Item Pannel")

            mainFrame = LabelFrame(root,text="Detail Form",bg=main_color,bd=5)
            mainFrame.pack(side=TOP,fill=BOTH,expand=1)

            Label(mainFrame,text="Product Name       :- ",font=bill_font,bg=main_color).place(x=10,y=10)
            Label(mainFrame,text="Quantity Taken :- ",font=bill_font,bg=main_color).place(x=10,y=60)
            Label(mainFrame,text="Price / Piece           :- ",font=bill_font,bg=main_color).place(x=10,y=110)

            

            p_name = Entry(mainFrame)
            p_name.place(x=190,y=10)
            p_name.insert(0,values[0])
            
            p_quantity = Entry(mainFrame)
            p_quantity.place(x=190,y=60)
            p_quantity.insert(0,values[1])
            
            price = Entry(mainFrame)
            price.place(x=190,y=110)
            price.insert(0,values[2])
            

            Button(mainFrame,text="Update Details !",width=10,command=update_tree,bg="slategray3",activebackground="slategray2").place(x=20,y=210)

            root.mainloop()

    def delete_from_tree():
        values = list(tree.item(tree.selection())['values'])
        if(values!=[]):
            tree.delete(tree.selection())

    def finalize_bill():
        global total_items,total_price
        cost = 0
        items = 0
        for i in tree.get_children():
            values = list(tree.item(i)['values'])
            items += values[1]
            cost = cost + (values[1]*values[2])
        total_price = cost
        total_items = items

        t_payment.config(state="normal")
        t_items.config(state="normal")
        
        t_items.delete(0,END)
        t_items.insert(0,total_items)
        t_payment.delete(0,END)
        t_payment.insert(0,total_price)

        t_payment.config(state="readonly")
        t_items.config(state="readonly")
        
        
        if submit_customer_details() == 1:
            final_function()

    # def add_product_window():

    def add_product_window():

        def close_window():
            root.destroy()
        
        def insert_product():
            try:
                result = [(f"{p_name.get()}",int(p_quantity.get()),int(price.get()))]
            except:
                messagebox.showerror(title="Bill Products" , message="You might have inserted \nWrong value in\nPrice or Quantity !")
                return                
            count=0
            for i in result:
                tree.insert('',count,values=i)
                count+=1
            p_name.delete(0,END)
            p_quantity.delete(0,END)
            price.delete(0,END)
            #messagebox.showinfo(title="Bill Product",message="Product inserted successfully !")


        root = Toplevel()
        root.geometry("650x300")
        root.title("New Item Pannel")

        mainFrame = LabelFrame(root,text="Detail Form",bg=main_color,bd=5)
        mainFrame.pack(side=TOP,fill=BOTH,expand=1)

        Label(mainFrame,text="Product Name       :- ",font=bill_font,bg=main_color).place(x=10,y=10)
        Label(mainFrame,text="Quantity Taken :- ",font=bill_font,bg=main_color).place(x=10,y=60)
        Label(mainFrame,text="Price / Piece           :- ",font=bill_font,bg=main_color).place(x=10,y=110)

        

        p_name = Entry(mainFrame)
        p_name.place(x=190,y=10)
        
        p_quantity = Entry(mainFrame)
        p_quantity.place(x=190,y=60)
        
        price = Entry(mainFrame)
        price.place(x=190,y=110)
        

        Button(mainFrame,text="Insert !",width=10,command=insert_product,bg="slategray3",activebackground="slategray2").place(x=20,y=210)
        Button(mainFrame,text="CLose !",width=10,command=close_window,bg="slategray3",activebackground="slategray2").place(x=180,y=210)

        root.mainloop()


    def add_buttons_frame3():
        Button_frame = Frame(Frame3,bg=main_color)
        Button_frame.pack(side=TOP,fill=X)
        
        Button(Button_frame,text=" + ",width=5,command=add_product_window,bg="slategray3",activebackground="slategray2").pack(side=LEFT,pady=5,padx=10)
        Button(Button_frame,text=" Edit ",width=10,command=edit_product_window,bg="slategray3",activebackground="slategray2").pack(side=LEFT,pady=5,padx=10)
        Button(Button_frame,text=" Delete ",width=10,command=delete_from_tree ,bg="slategray3",activebackground="slategray2").pack(side=LEFT,pady=5,padx=10)
        Button(Button_frame,text=" Print Bill ",width=13,command=finalize_bill,bg="slategray3",activebackground="slategray2").pack(side=LEFT,pady=5,padx=10)

    def add_tree_view(tree):

        x_scroll=Scrollbar(Frame3,orient=HORIZONTAL)
        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll=Scrollbar(Frame3,orient=VERTICAL)
        y_scroll.pack(side=RIGHT,fill=Y)

        tree.configure(yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)        

        x_scroll.config(command=tree.xview)
        y_scroll.config(command=tree.yview)


    
    def _product_bill_name_generate():
        months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        name = months[datetime.today().month] +"_"+ str(datetime.today().year)
        return str(name)+"_products_bill.db"

    def check_bills():
        global final_product_database_name
        if os.path.exists("Products_sale") == False:
            os.mkdir("Products_sale")
        
        name = "Products_sale/"+_product_bill_name_generate()
        final_product_database_name = name
        if os.path.exists(name) == False:
            conn = sqlite3.connect(name)
            conn.execute("""CREATE TABLE PRODUCTS_BILL(
                BILL_NUMBER TEXT,
                CUSTOMER_NAME TEXT,
                PRODUCT_NAME TEXT,
                QUANTITY_TAKEN INT,
                PRICE INT
            )""")
            conn.commit()
            conn.close()
    
    
    Frame3 = LabelFrame(root,height=380, bd=5,  bg=main_color)
    Frame3.pack(side=TOP,fill=X)

    a_tuple = ("PRODUCT_NAME","QUANTITY_TAKEN","PRICE")
    tree=ttk.Treeview(Frame3,height=18,columns=a_tuple)
    tree.pack(side=TOP,fill=BOTH,expand=1)
    i=0
    while i<len(a_tuple):
        tree.column(i)
        tree.heading(i,text=a_tuple[i])
        i+=1
    tree['show']='headings'


    add_buttons_frame3()
    add_tree_view(tree)
    check_bills()
    


        
        
        
