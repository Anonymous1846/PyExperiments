import tkinter as tk
import json
from tkinter.ttk import Label,Combobox

#this is a simple python GUI application which simplifies the selection of regex expressions so that it can be used for form validation !

#loading the actual json file (dictionary ) !
with open('Regexes.txt','r') as f:
	the_file=f.readlines()
print(the_file)

root =tk.Tk()
root.geometry('500x400')
root.title('Regex Template Generator !')
#now we need to extract the names and the correponding regexes !
titles=list(map(lambda x:x.replace('\n',''),the_file))
print(names)
#adding the text at the centre top of the dialog box !
Label(root,text='Choose a regex template ',foreground='green').pack(padx=10,pady=20)
#creating the combobox for the regex templates

n=tk.StringVar()
regex_combobox=Combobox(root,width=15,textvariable=n)

#adding the values to the combobox !
regex_combobox['values']=tuple(names)
regex_combobox.pack(padx=10,pady=30)
regex_combobox.current()

root.mainloop()
