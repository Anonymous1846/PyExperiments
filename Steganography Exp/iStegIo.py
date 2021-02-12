'''jStegIO is a python script/application used to hide or extract information from or to images
jStegIO uses LSB encryption technique, which means that it will replace the least significant
bit of the pixel value(RGB) with the text information We can also use the same script to uncover
the message from the image. The message to be encrypted can either be a text file or a prompt !'''
from PIL import Image
#for ascii to binary conversion and vice versa
import binascii
#most of the times the file/image may not be in the same directory as that of the Script File !;
from tkinter.filedialog import *
import tkinter.filedialog as f
#the module for ascii art 
import pyfiglet
heading=pyfiglet.figlet_format('i S t e g I O')
print(heading)
#multiplying the tuple containing the - 50 times
print('VERSION 1.0')
print(*50*('-',))
'''
params: the r,g and b values of the color pixel(s)
return:the hexadecimal value of the corresponding color !
the if we give the input as 12,12,123 we get #0C0C7B(X is used for Capital Hex letters)
'''
def rgb_to_hex(r,g,b):
	return '#{:02x}{:02x}{:02x}'.format(r,g,b)
'''
params:hex code for the corresponding color 
return: tuple containing the rgb values
in the function we have gave the hex code staring from 1 because we have to avoid the # symbol !
'''
def hex_to_rgb(hex_code):
        #the pound symbol is removed by starting the string from 1st index !
        r,g,b=bytes.fromhex(hex_code[1:])
        #the bytes method return a series of immutable bytes ranging from 0 to 255
        #and then returned as a tuple !
        return (r,g,b)
'''
params:the string value(usually the text file to be encrypted)
return: the binary representation of the string value (with the 0b replaced by the None)
we use this function to convert the string value to hex 16 and finally to the binary(0b1001001110)->(100001001000)
'''
def string_to_binary(the_string):
	#first we converted the str into the hex value to int64 and replace the first two 0b from the binary to None
        return bin(int(binascii.hexlify(the_string.encode()),16)).replace('0b','')
'''
params: binary value to be converted to string
return: the final string values after it is first converted into int to base 2 and finally to str
representation of the hex in %x %x %x
'''
def binary_to_string(binary):
	return binascii.unhexlify('%x' % (int('0b'+ binary ,2))).decode()

def encrypt(hex_code,digit):
	if hex_code[-1] in range(0,6):
		#we will append the digit or the information at the end of our hex
		hex_code=hexcode[:-1]+digit
		return hex_code
	else:
		#otherise return Nothing !
		return None
def decrypt(hex_code):
	if hex_code[-1] in ['0','1']:return hex_code[-1]
	else:return None

def hide():
	pass
def extract():
	pass
'''
the function to convert the image into png, so that it can work properly in this case !
params: the jpeg image
return: the png image
'''
def convert_to_png(the_jpeg_image):
	#lambda function to convert the .jpeg or jpg file to .png file !
	some_image=lambda x:x.replace('.jpg','.png') if '.jpg' in x else x.replace('.jpeg','.png')
	working_image=Image.open(the_jpeg_image)
	working_image.save(some_image(the_jpeg_image))
	return working_image
while True:
	choice=int(input('1)Encrypt\n2)Decrypt\n3)Exit\n'))
	if choice==1:
		print(rgb_to_hex(12,12,12))
		print(binary_to_string(string_to_binary('Hello')))
	elif choice==2:
		the_image=f.askopenfilename()
		convert_to_png(the_image)
	else:
		break
		print('Exiting...... !')
		exit()

