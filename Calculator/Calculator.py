#a simple gui calculator made with tkinter and python !
import tkinter as tk
from tkinter import *
from tkinter.ttk import Button,Label
main=tk.Tk()
num1=num2=ans=operator=None
answered=False
#the geomtery stands for the width and the height later we have given the title
main.geometry('400x350')
main.title('Calculator v1.0')
#the params of the calculator are root, height, width and the state(so it is readonly)
text_field=Text(main,height=3,width=54)
#text entry function
#its actually number
'''
The function which recieves the first number num1 and stores it in the variable !
The existing the variable is taken and the new digit is appended at the end and then the old 
number is deleted, after that the new number is displayed on the console !
If the query is answered earlier then it will remove the entire number and start over again !
'''
def enter_text(text):
	global answered#flag to check whether equals has been pressed earlier !
	if answered == True:
		text_field.delete(1.0,"end")
		text_field.insert(1.0, text)
		answered=False
	else:
		already_text=text_field.get(1.0,"end")
		text_field.delete(1.0,"end")
		already_text=already_text[:-1]+text
		text_field.insert(1.0,already_text)	
text_field.pack()
'''
The function recieves the flag for operation and gets the second number and stores the operator information !
Note:global variables used for avoiding conflict !
'''
def handle_operation(op):
	global num1,operator,answered
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
		answered=True#providing true since it computes the answer here it self !
	elif op=='c':
		text_field.delete(1.0,'end')
	elif op=='m':
		num1=text_field.get(1.0,'end')
		operator='m'
		text_field.delete(1.0,'end')
'''
The main function for executing the mathematical operation,except for %
We perform the math operations,if both numbers are set !
'''
def equals_operation():
	global num2,num1,ans,answered
	if num1 != None:
		num2=text_field.get(1.0,'end')
		text_field.delete(1.0,'end')
		if operator=='+':
			ans=float(num1)+float(num2)
			text_field.insert(1.0,str(ans))
		if operator=='-':
			ans=float(num1)-float(num2)
			text_field.insert(1.0,str(ans))
		if operator=='x':
			ans=float(num1)*float(num2)
			text_field.insert(1.0,str(ans))
		if operator=='/':
			ans=float(num1)/float(num2)
			text_field.insert(1.0,str(ans))
		if operator=='m':
			try:
				ans=int(num1.replace('\n',''))%int(num2)
				text_field.insert(1.0,str(ans))
			except:
				print('Maybe the number format is wrong !')
		answered=True
		

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
zero=Button(main,text='0',command=lambda:enter_text('0')).place(x=10,y=185)
#operatonal buttons
add=Button(main,text='+',command=lambda:handle_operation("+")).place(x=10,y=225)
sub=Button(main,text='-',command=lambda:handle_operation('-')).place(x=110,y=185)
mul=Button(main,text='x',command=lambda:handle_operation('x')).place(x=210,y=185)
div=Button(main,text='/',command=lambda:handle_operation('/')).place(x=310,y=105)
per=Button(main,text='%',command=lambda:handle_operation("%")).place(x=310,y=145)
mod=Button(main,text='mod',command=lambda:handle_operation('m')).place(x=310,y=185)
equals=Button(main,text="=",command=lambda:equals_operation()).place(x=310,y=65)
c=Button(main,text='C/CE',width=28,command=lambda:handle_operation('x')).place(x=110,y=225)
main.mainloop()
