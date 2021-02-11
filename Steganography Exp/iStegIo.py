'''jStegIO is a python script/application used to hide or extract information from or to images
jStegIO uses LSB encryption technique, which means that it will replace the least significant
bit of the pixel value(RGB) with the text t information We can also use the same script to uncover
the message from the image. The message to be encrypted can either be a text file or a prompt !'''
import PIL
#most of the times the file/image may not be in the same directory as that of the Script File !;
from tkinter.filedialog import *
import tkinter.filedialog as f
def encrypt():
	pass
def decrypt():
	name_of_image=f.askopenfilename()
	print(name_of_image)
while True:
	choice=int(input('1)Encrypt\n2)Decrypt\n3)Exit\n'))
	if choice==1:
		print('Print Encrypt')
	elif choice==2:
		decrypt()
	else:
		break
		exit()

