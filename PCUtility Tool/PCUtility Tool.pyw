from shutil import copyfile
from time import sleep
import win10toast
import threading
import schedule
import random
import psutil
import ctypes
import os


current_user=os.getlogin() #the currently logged in user name

exe_path=f'C:\\Users\\{current_user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PCUtility Tool.pyw'


PIC_DIRECTORY=f'C:\\Users\\{current_user}\\Pictures\\Camera Roll' #the directory where the photos where the photos are stored and it can be changed !
EXTS=['jpg','jpeg','png']
#filtering out only the pictures with png, jpg, and jpeg !
PICS=[picture for picture in os.listdir(PIC_DIRECTORY) if any(picture.endswith(extension) for extension in EXTS)]
if not os.path.isfile(exe_path):
	#if it is not in the startup folder then copy it to the startup folder !
	copyfile('./PCUtility Tool.pyw',exe_path)
def _change_wallpaper():
	wallpaper=random.choice(PICS)#a random pic is chosen from the list !
	ctypes.windll.user32.SystemParametersInfoW(20, 0,os.path.join(PIC_DIRECTORY,wallpaper), 0) #the path to the wallpapper provided in the third parameter !

def change_wallpaper():
	schedule.every(2).minutes.do(change_wallpaper) #the schedule library performs a particular operation every 2 minutes(can be changed !)
	while True:
		schedule.run_pending()
		sleep(1)
'''
The battery information is retrieved by the python module named psutil, which is a cross platform utility used folder
getting the process information of the OSes.
'''
def check_battery_status():
	battery_info=psutil.sensors_battery()
	print(battery_info.percent)

check_battery_status()
