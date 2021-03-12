import ctypes
import os
import random
import schedule
from time import sleep
from shutil import copyfile
#the currently logged in user name
current_user=os.getlogin()
exe_path=f'C:\\Users\\{current_user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\DynaMic.pyw'

#the directory where the photos where the photos are stored and it can be changed !
PIC_DIRECTORY=f'C:\\Users\\{current_user}\\Pictures\\Camera Roll'
EXTS=['jpg','jpeg','png']
#filtering out only the pictures with png, jpg, and jpeg !
PICS=[picture for picture in os.listdir(PIC_DIRECTORY) if any(picture.endswith(extension) for extension in EXTS)]
if not os.path.isfile(exe_path):
	#if it is not in the startup folder then copy it to the startup folder !
	copyfile('./DynaMic.pyw',exe_path)	
def change_wallpaper():
	#a random pic is chosen from the list !
	wallpaper=random.choice(PICS)
	#the path to the wallpapper provided in the third parameter !
	ctypes.windll.user32.SystemParametersInfoW(20, 0,os.path.join(PIC_DIRECTORY,wallpaper), 0)
#the schedule library performs a particular operation every 2 minutes(can be changed !) 
schedule.every(2).minutes.do(change_wallpaper)
while True:
	schedule.run_pending()
	sleep(1)
