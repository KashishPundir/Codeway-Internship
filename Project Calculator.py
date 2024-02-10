import math
from tkinter import *
calc=Tk()
calc.title("Calculator")
calc.geometry("570x650")     
calc.resizable(False,False)
calc.configure(bg="black")
equation=""
equation1=""
s=""
def show(value):
    global equation
    global equation1
    if value=="factorial(":
        equation+="!("
    elif value=="⌫":
        equation=equation[0:len(equation)-1]
    else:
        equation+=value
    if value=="log(" or value=="factorial(":
        equation1+="math."+value
    elif value=="⌫":
        equation1=equation1[0:len(equation1)-1]
    else:
        equation1+=value
    result_box.config(text=equation)
    
def clear():
    global equation
    global equation1
    equation=""
    equation1=""
    result_box.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation1)
        except:
            result="Error"
            equation=""
    result_box.config(text=result)
result_box=Label(calc,height=3,width=35,text="",font=("arial",23))
result_box.pack()

Button(calc,text="C",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="red",command=lambda:clear()).place(x=10,y=123)
Button(calc,text=".",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show(".")).place(x=149,y=123)
Button(calc,text="/",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show("/")).place(x=290,y=123)
Button(calc,text="⌫",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show("⌫")).place(x=430,y=123)

Button(calc,text="log",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show(("log("))).place(x=10,y=210)
Button(calc,text="!x",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show(("factorial("))).place(x=149,y=210)
Button(calc,text="exp",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("**")).place(x=290,y=210)
Button(calc,text="*",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show("*")).place(x=430,y=210)

Button(calc,text="7",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("7")).place(x=10,y=297)
Button(calc,text="8",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("8")).place(x=148,y=297)
Button(calc,text="9",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("9")).place(x=290,y=297)
Button(calc,text="-",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show("-")).place(x=430,y=297)

Button(calc,text="4",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("4")).place(x=10,y=385)
Button(calc,text="5",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("5")).place(x=148,y=385)
Button(calc,text="6",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("6")).place(x=290,y=385)
Button(calc,text="+",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show("+")).place(x=430,y=385)

Button(calc,text="1",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("1")).place(x=10,y=473)
Button(calc,text="2",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("2")).place(x=148,y=473)
Button(calc,text="3",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("3")).place(x=290,y=473)
Button(calc,text="=",height=3,width=5,font=("arial",30,"bold"),bd=2,fg="red",command=lambda:calculate()).place(x=430,y=473)

Button(calc,text="(",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show("(")).place(x=10,y=561)
Button(calc,text="0",height=1,width=5,font=("arial",30,"bold"),bd=2,command=lambda:show("0")).place(x=148,y=561)
Button(calc,text=")",height=1,width=5,font=("arial",30,"bold"),bd=2,fg="green",command=lambda:show(")")).place(x=290,y=561)
calc.mainloop()
