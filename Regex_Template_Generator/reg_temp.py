import pyperclip
import tkinter as tk
from tkinter.ttk import Button,Label,Combobox
from tkinter import messagebox

#this is a simple python GUI application which simplifies the selection of regex expressions so that it can be used for form validation !

#regex stord as a dictionary !
regexes={
		"URL":"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$",
		"Name":"^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)",
		"Youtube Video":"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$",
		"Email":"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
		"Phone Number":"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$",
		"Sentence":"^[a-zA-Z0-9_ ]*$",
		"IP":"(\\d{1, 2}|(0|1)\\d{2}|2[0-4]\\d|25[0-5])",
		"VISA":"^4[0-9]{12}(?:[0-9]{3})?$",
		"MasterCard":"5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$"
		}

root =tk.Tk()
root.geometry('400x400')
root.title('Regex Template Generator !')

#adding the text at the centre top of the dialog box !
Label(root,text='Choose a regex template ',foreground='green').pack(padx=10,pady=20)
#creating the combobox for the regex templates

n=tk.StringVar()
regex_combobox=Combobox(root,width=15,textvariable=n)

#adding the values to the combobox !
regex_combobox['values']=tuple(regexes.keys())
regex_combobox.pack(padx=10,pady=30)
regex_combobox.current()


#the funtion to get the regex of the choosen key !
def get_regex():
	value=regex_combobox.get()
	data=regexes[value]
	#copy to clipbroad !
	pyperclip.copy(data)
	#showing the prompt !
	messagebox.showinfo('Copied !','The Regex is copied to clipboard !')

copy_to_clipboard=Button(text='Copy',command=get_regex).pack(padx=0,pady=50)
cancel=Button(text='Cancel',command=root.destroy).pack(padx=0,pady=30)
root.mainloop()
