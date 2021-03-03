#a simple gui calculator made with tkinter and python !
import tkinter as tk
from tkinter import *
from tkinter.ttk import Button,Label
main=tk.Tk()
num1=num2=operator=None
#the geomtery stands for the width and the height later we have given the title
main.geometry('450x400')
main.title('Calculator v1.0')
#the params of the calculator are root, height, width and the state(so it is readonly)
text_field=Text(main,height=3,width=54)
#text entry function
#its actually number
def enter_text(text):
	already_text=text_field.get(1.0,"end")
	text_field.delete(1.0,"end")
	already_text=already_text[:-1]+text
	text_field.insert(1.0,already_text)
text_field.pack()
def handle_operation(op):
	if op=='+':
		num1=text_field.get(1.0,"end")
		operator="+"
		text_field.delete(1.0,'end')

	elif op=="-":
		num1=text_field.get(1.0,"end")
		operator="-"
		text_field.delete(1.0,'end')
	elif op=='/':
		num1=text_field.get(1.0,"end")
		operator='/'
		text_field.delete(1.0,'end')

	elif op=='x':
		num1=text_field.get(1.0,'end')
		operator='x'
		text_field.delete(1.0,'end')
	elif op=='%':
		num1=text_field.get(1.0,'end')
		new_num=float(num1)/100
		text_field.delete(1.0,"end")
		text_field.insert(1.0,str(new_num))
	elif op=='=':
		num2=text_field.get(1.0,'end')
		if operator=='+':
			ans=float(num1)+float(num2)
			text_field.delete(1.0,'end')
			text_field.insert(1.0,str(ans))
#the numerical buttons !
one=Button(main,text='1',command=lambda:enter_text("1")).place(x=10,y=65)
four=Button(main,text='4',command=lambda:enter_text("4")).place(x=10,y=105)
seven=Button(main,text='7',command=lambda:enter_text("7")).place(x=10,y=145)
two=Button(main,text='2',command=lambda:enter_text("2")).place(x=110,y=65)
five=Button(main,text='5',command=lambda:enter_text("5")).place(x=110,y=105)
four=Button(main,text='8',command=lambda:enter_text("8")).place(x=110,y=145)
three=Button(main,text='3',command=lambda:enter_text("3")).place(x=210,y=65)
six=Button(main,text='6',command=lambda:enter_text("6")).place(x=210,y=105)
nine=Button(main,text='9',command=lambda:enter_text("9")).place(x=210,y=145)
#operatonal buttons
add=Button(main,text='+',command=lambda:handle_operation("+")).place(x=10,y=185)
sub=Button(main,text='-').place(x=110,y=185)
mul=Button(main,text='x').place(x=210,y=185)
div=Button(main,text='/').place(x=310,y=185)
per=Button(main,text='%',command=lambda:handle_operation("%")).place(x=310,y=145)
mod=Button(main,text='mod').place(x=310,y=105)
equals=Button(main,text="=",command=lambda:handle_operation("=")).place(x=310,y=65)
main.mainloop()
