import tkinter as tk
from tkinter.ttk import Label,Combobox
#this is a simple python GUI application which simplifies the selection of regex expressions so that it can be used for form validation !
root =tk.Tk()
root.geometry('500x400')
root.title('Regex Template Generator !')
#adding the text at the centre top of the dialog box !
Label(root,text='Choose a regex template ',foreground='green').pack(padx=10,pady=20)
#creating the combobox for the regex templates
n=tk.StringVar()
regex_combobox=Combobox(root,width=15,textvariable=n)
#adding the values to the combobox !
regex_combobox['values']=('Password','MasterCard','Email','Phone Number')
regex_combobox.pack(padx=10,pady=30)
regex_combobox.current()
root.mainloop()
