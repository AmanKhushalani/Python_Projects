from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

FILE=''
root=Tk()
root.geometry('700x600')
root.title('Untitled - Notebook')
#-------------- FONT STYLE SECTION ------------------------------------

A='arial'
B=''
C='15'

def font_style():

      
      
      root=Tk()
      root.geometry('400x350')
      root.title('Font settings')

      outer=LabelFrame(root,text='Sample',height=50,font='15')
      l=Label(outer,text='SAMPLE text',font=A+B+C)
      l.pack(padx=15,pady=15)
      outer.place(x=40,y=260)

      def  done_settings():
            a.configure(font=A+' '+C+' '+B)
            root.destroy()
      
      
#------------------------------------------------------------           

      font_frame=LabelFrame(root,text='Choose Font',bd=6)
      font_frame.place(x=20,y=20)
      li=['Arial','Times','Algerian','Bahnschrift','Broadway','Courier','Latin','Papyrus','Playbill','Ravie','Rockwell','Roman','Script','StikaBanner','Stencil','Symbol','System','Tahoma','Terminal','Verdana','Vivaldi','WedSymboLys','Wingdings']
      s=Scrollbar(font_frame,)
      s.pack(side=RIGHT,fill=Y)
      fnt=StringVar()
      listbox1=Listbox(font_frame,relief=FLAT,listvariable=fnt,bd=5,height=9,width=13,yscrollcommand=s.set)
      for i in li:
            listbox1.insert(END,i)
      listbox1.pack()
      s.config(command=listbox1.yview,)
#---------------------------------------------------------------
            

      style_frame=LabelFrame(root,text='Choose Style',bd=6)
      style_frame.place(x=150,y=20)
      lo=['bold','italic','underline','regular']
      s=Scrollbar(style_frame,)
      s.pack(side=RIGHT,fill=Y)
      sty=StringVar()
      listbox2=Listbox(style_frame,relief=FLAT,listvariable=sty,bd=5,height=9,width=13,yscrollcommand=s.set)
      for i in  lo:
            listbox2.insert(END,i)
      listbox2.pack()
      s.config(command=listbox2.yview,)
#-----------------------------------------------------------------------------
            
                  
      size_frame=LabelFrame(root,text='Font Size',bd=6)
      size_frame.place(x=280,y=20)
      s=Scrollbar(size_frame,)
      s.pack(side=RIGHT,fill=Y)
      siz=IntVar()
      listbox3=Listbox(size_frame,relief=FLAT,listvariable=siz,bd=5,height=9,width=10,yscrollcommand=s.set)
      for i in range(1,70):
            listbox3.insert(END,str(i))
      listbox3.pack()
      s.config(command=listbox3.yview)
  
#-------------------------------------------------------------
      def change_font():
            global A,B,C
            A=listbox1.curselection()
            if A==():
                  pass
            else:
                  temp=li[A[0]]
                  A=temp
                  l.configure(font=temp)
            
      def change_size():
            global A,B,C
            C=listbox3.curselection()
            if C==():
                  pass
            else:
                  temp=str(C[0])
                  C=temp
                  l.configure(font=A+' '+C+' '+B)

      def change_style():
            global A,B,C
            B=listbox2.curselection()
            if B==():
                  pass
            else:
                  temp=lo[B[0]]
                  if temp=='regular':
                        temp=''
                  B=temp
                  temp=A+' '+C+' '+temp
                  l.configure(font=temp)
      
      

      b=Button(root,text='GO..!',width=10,command=change_font)
      b.place(x=40,y=210)
      b=Button(root,text='GO..!',width=10,command=change_style)
      b.place(x=160,y=210)
      b=Button(root,text='Go..!',width=10,command=change_size)
      b.place(x=280,y=210)

      b=Button(root,text='Done !',width=10,command=done_settings,fg='green',relief=GROOVE,)
      b.place(x=280,y=300)
      root.mainloop()
      




#------------------SHORT CUTS-----------------------------------
def op_file():
      FILE=askopenfilename(defaultextension=".txt",filetypes=[('All files',"*.*"),('Text Documents',"*.txt")])

      if FILE=="":
            FILE=None
      else:
            root.title(os.path.basename(FILE+' - Notebook'))
            a.delete(1.0,END)
            f=open(FILE,'r')
            a.insert(1.0,f.read())
            f.close()
      
def open_file(event):
      op_file()

      
def n_file():
      global FILE
      root.title('Untitled - Notebook')
      FILE=None
      a.delete(1.0,END)
def new_file(event):
      n_file()

      
def sa_file():

      global FILE
      if FILE==None:
            FILE=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[('All files',"*.*"),('Text Documents',"*.txt")])

            if FILE=="":
                  FILE=None
            else:
                  f=open(FILE,'w')
                  f.write(a.get(1.0,END))
                  f.close()
                  root.title(os.path.basename(FILE)+' - Notebook')
      else:
            f=open(FILE,'w')
            f.write(a.get(1.0,END))
            f.close()
            
      
def save_file(event):
      sa_file()
      
def d_exit():
      root.destroy()
def do_exit(event):
      d_exit()
      
root.bind('<Control-o>',open_file)
root.bind('<Control-n>',new_file)
root.bind('<Control-s>',save_file)
root.bind('<Control-q>',do_exit)


#====================== MENU ================================#
scrollbar=Scrollbar(root)
a=Text(root,undo=4,yscrollcommand=scrollbar.set)
FILE=None
scrollbar.config(command=a.yview)
scrollbar.pack(side=RIGHT,fill=Y)
a.pack(fill=BOTH,expand=1)


new_menu=Menu(root)
root.config(menu=new_menu,)

#------------------ FILE MENU ---------------------------
file_menu=Menu(new_menu)
new_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New        Ctrl + n',command=n_file)
file_menu.add_command(label='Save        Ctrl + s',command=sa_file)
file_menu.add_command(label='Open      Ctrl + o',command=op_file)
file_menu.add_command(label='Exit          Ctrl + q',command=d_exit)


#--------------------- EDIT MENU --------------------------------
def do_cut():
      a.event_generate('<<Cut>>')
def do_paste():
      a.event_generate('<<Paste>>')
def do_copy():
      a.event_generate('<<Copy>>')
      
edit_menu=Menu(new_menu)
new_menu.add_cascade(label='Edit',menu=edit_menu)
new=Menu(edit_menu)
edit_menu.add_command(label='Cut            Ctrl + x',command=do_cut)
edit_menu.add_command(label='Copy         Ctrl + c',command=do_copy)
edit_menu.add_command(label='Paste         Ctrl + v',command=do_paste)


#---------------------- THEMES STARTED -------------------------------

edit_menu.add_cascade(label='Theme',menu=new)

def dark_mode():
      a.configure(bg='black',fg='white',insertbackground='white')
def light_mode():
      a.configure(bg='white',fg='black',insertbackground='black')
def grey_mode():
      a.configure(bg='grey',fg='black',insertbackground='black')
def custom_mode():

      
      custom_root=Tk()
      custom_root.geometry('400x250')
      custom_root.title('Theme settings')
      
      back_frame=LabelFrame(custom_root,text='Choose Background',bd=6)
      back_frame.place(x=20,y=20)
      li=['Black','White','Pink','Gold','Silver','Blue','Red','Yellow','Green','Cyan']
      s=Scrollbar(back_frame,)
      s.pack(side=RIGHT,fill=Y)
      fnt=StringVar()
      listbox1=Listbox(back_frame,relief=FLAT,listvariable=fnt,bd=5,height=9,width=11,yscrollcommand=s.set)
      for i in li:
            listbox1.insert(END,i)
      listbox1.pack()
      s.config(command=listbox1.yview,)
#---------------------------------------------------------------
            

      front_frame=LabelFrame(custom_root,text='Choose Foreground',bd=6)
      front_frame.place(x=150,y=20)
      lo=['Black','White','Pink','Gold','Silver','Blue','Red','Yellow','Green','Cyan']
      s=Scrollbar(front_frame,)
      s.pack(side=RIGHT,fill=Y)
      sty=StringVar()
      listbox2=Listbox(front_frame,relief=FLAT,listvariable=sty,bd=5,height=9,width=11,yscrollcommand=s.set)
      for i in  lo:
            listbox2.insert(END,i)
      listbox2.pack()
      s.config(command=listbox2.yview,)
#-----------------------------------------------------------------------------
            
                  
      cursor_frame=LabelFrame(custom_root,text='Choose Cursor',bd=6)
      cursor_frame.place(x=280,y=20)
      s=Scrollbar(cursor_frame,)
      s.pack(side=RIGHT,fill=Y)
      lis=['Black','White','Pink','Gold','Silver','Blue','Red','Yellow','Green','Cyan']
      siz=IntVar()
      listbox3=Listbox(cursor_frame,relief=FLAT,listvariable=siz,bd=5,height=9,width=11,yscrollcommand=s.set)
      for i in lis:
            listbox3.insert(END,i)
      listbox3.pack()
      s.config(command=listbox3.yview)
      
      def change_bg():
            A=listbox1.curselection()
            if A==():
                  A='white'
            else:                
                  AM=int(A[0])
                  A=li[AM]
            a.configure(bg=A)
      def change_fg():
            B=listbox2.curselection()
            if B==():
                  B='black'
            else:                
                  BM=int(B[0])
                  B=li[BM]
            a.configure(fg=B)
      def change_insert():
            C=listbox3.curselection()
            if C==():
                  C='black'
            else:                
                  CM=int(C[0])
                  C=li[CM]              
            a.configure(insertbackground=C)

      b=Button(custom_root,text='GO..!',width=10,command=change_bg)
      b.place(x=40,y=210)
      b=Button(custom_root,text='GO..!',width=10,command=change_fg)
      b.place(x=160,y=210)
      b=Button(custom_root,text='GO..!',width=10,command=change_insert)
      b.place(x=280,y=210)
      
  
      custom_root.mainloop()

new.add_command(label='Light theme',command=light_mode)
new.add_command(label='Dark theme',command=dark_mode)
new.add_command(label='Grey theme',command=grey_mode)
new.add_command(label='Custom theme',command=custom_mode)

#-------------- THEMES ENDED ---------------------------
edit_menu.add_command(label='Font ',command=font_style)



#-------------- ABOUT MENU -------------------------------
def about_():
      a=messagebox.showinfo(title='About " Notebook "',message='''This is a simple text editor similar as Notepad.
\n Just with a new feature of setting pre-defined themes \n and making custom themes and font colors.''')
      
about_menu=Menu(new_menu)
new_menu.add_cascade(label='About',menu=about_menu)
about_menu.add_command(label='About Notebook',command=about_)



root.mainloop()


























