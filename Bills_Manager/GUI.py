from main import add_new_customer, show_customer_details,show_about, show_help
from os import system
from tkinter import *
from Mainpage import *

main_color = "LightSkyBlue4"
Entry_karo = False

def login(root):
    login_frame = Frame(root, background=main_color)
    login_frame.pack(fill=BOTH, expand=Y)
    x_label = 500
    x_entry = 590
    y_label = 300
    y_entry = 300
        
    Label(login_frame,text="Username:- ",bg=main_color).place(x=x_label,y=y_label)
    uname = Entry(login_frame,)
    uname.place(x=x_entry,y=y_entry)    
    
    Label(login_frame,text="Password:- ",bg=main_color).place(x=500,y=330)
    pswd = Entry(login_frame,show='*')
    pswd.place(x=x_entry,y=y_entry+30)

    def check_values():
        #if True:
        if uname.get()=="user1234" and pswd.get()=="user1234":
            login_frame.pack_forget()
            myMenu(root)
            mainpage(root)

        else:
            uname.configure(fg="RED")
            pswd.configure(fg="RED")

    Button(login_frame,text="Login !", command=check_values,bg="slategray3",activebackground="slategray2").place(x=520,y=380)
    Button(login_frame,text="New User !",bg="slategray3",activebackground="slategray2").place(x=620,y=380)



def myMenu(root):

    pass
    my_menu = Menu()
    root.config(menu=my_menu)
    
    customer_menu=Menu(my_menu)
    products_menu=Menu(my_menu)
    
    my_menu.add_cascade(label='Customer ',menu=customer_menu)
    customer_menu.add_command(label='New Customer',command = add_new_customer)
    customer_menu.add_command(label='Show Customers',command = show_customer_details)
    
    # show=Menu(my_menu)
    # my_menu.add_cascade(label='Sales',menu=show)
    # show.add_command(label='Revenue',command=show_sales)
    # show.add_command(label='Sales',command=show_sales)
    
    about=Menu(my_menu)
    my_menu.add_cascade(label='About',menu=about)
    about.add_command(label='About',command=show_about)
    
    
    help=Menu(my_menu)
    my_menu.add_cascade(label='Help',menu=help)
    help.add_command(label='Help',command=show_help)
    

    pass

def start():
    root = Tk()
    root.geometry("1345x700+5+1")
    root.title("Bills Detail Manager")
    root.maxsize(width=1360,height=700)
    root.minsize(width=1360,height=700)

    login(root)

    root.mainloop()


if __name__ == "__main__":
    system("clear")
    start()
    
