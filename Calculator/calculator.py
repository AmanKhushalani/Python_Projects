from tkinter import *
from math import *

root=Tk()
root.geometry("220x250")
root.maxsize(width=220,height=250)
root.minsize(width=220,height=250)
root.title("Calci")
root.configure(bg='grey')
def click(event,a=None):
      global main_var
      text=event.widget.cget('text')
      if text=='=':
            try:
                  
                  if '>' in main_var.get() or '<' in main_var.get():
                        answer=eval(main_var.get())
                        if answer==1:
                              answer='True'
                        if answer==0:
                              answer='False'
                  else:
                        answer=eval(main_var.get())
                        if type(answer)==float:
                              answer=round(float(answer),2)
            except:
                  answer='Error'
            finally:
                  main_var.set(answer)
                  screen.update()
                  if answer=='Error':
                        root.configure(bg='red')
                  elif answer==0:
                        root.configure(bg='blue')
                  else:
                        root.configure(bg='green')
                        
      elif text=='CE':
            main_var.set("")
            screen.update()
            root.configure(bg='grey')
      else:
            if len(main_var.get())>11:
                  root.configure(bg='red')
                  pass
            else:
                  main_var.set(main_var.get()+text)
                  screen.update()
      


main_var=StringVar()
screen=Entry(root,font='arial 20 bold',width=13,relief=FLAT,textvariable=main_var)
screen.pack(ipadx=1,ipady=3,padx=10,pady=4)

li=['1','2','3','/','*','4','5','6','+','-','7','8','9','<','>','.','0','%','(',')','sin','cos','tan','CE','=']
i=0
u=0
p=50
count=0
while i<5:
      j=0
      u=0
      while j<5:
            b=Button(root,text=li[count],width=5,height=2,font='lucida 9 bold')
            b.place(x=u,y=p)
            b.bind('<Button-1>',click)
            u+=45
            count+=1
            j+=1
      p+=40
      i+=1

root.mainloop()
