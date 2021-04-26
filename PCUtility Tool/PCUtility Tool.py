'''
Author: Sharath Sunil
GitHub: https://github.com/Anonymous1846
Copyright: 2021
Language:Python

A Simple Python program/script which parallely moniters the battery status, and changes the backgroud wallpaper at an interval of 2 minutes !
'''
from shutil import copyfile
from time import sleep
from plyer import notification
import schedule
import random
import psutil
import ctypes
import sys
import os

sys.setrecursionlimit(10**6) #recursion limit set to 10^6 otherwise error will pop up !
'''
The currently logged in user is obtained then we locate his/her startup directory and check if the file is already there, if not
then we copy the file from the current location to the startup directory.
The pictures are loaded from the camera roll directory of the currenty logged in user !
'''
current_user=os.getlogin() #the currently logged in user name
exe_path=f'C:\\Users\\{current_user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PCUtility Tool.pyw'
PIC_DIRECTORY=f'C:\\Users\\{current_user}\\Pictures\\Camera Roll' #the directory where the photos where the photos are stored and it can be changed !
EXTS=['jpg','jpeg','png']
PICS=[picture for picture in os.listdir(PIC_DIRECTORY) if any(picture.endswith(extension) for extension in EXTS)] #filtering out only the pictures with png, jpg, and jpeg !

#if not os.path.isfile(exe_path):
#	copyfile('./PCUtility Tool.pyw',exe_path) #if it is not in the startup folder then copy it to the startup folder !

'''
The helper function for randomly choose a image for the background, and the image is set using the ctypes interface
SystemParametersInfoW function, the dir is the camera roll directory, to change to the directory of your choice, please
change the variable PIC_DIRECTORY !

return: None

params: None
'''
def _change_wallpaper():
	wallpaper=random.choice(PICS)#a random pic is chosen from the list !
	ctypes.windll.user32.SystemParametersInfoW(20, 0,os.path.join(PIC_DIRECTORY,wallpaper), 0) #the path to the wallpapper provided in the third parameter !

'''
The function which actually makes a call to the above function, here the _change_wallpaper function is called at an interval of 2 mins.
We can change the interval to our liking !

return: None

params: None
'''
def change_wallpaper():
	schedule.every(2).minutes.do(change_wallpaper) #the schedule library performs a particular operation every 2 minutes(can be changed !)
	while True:
		schedule.run_pending()
		sleep(1)


'''
The battery information is retrieved by the python module named psutil, which is a cross platform utility
used for getting the process/services information of the OSes. The basic idea of the function is to warn the user
to charge the laptop, when the battery percentage is less than 25 and remove the charger if the battery % is
greater than 95%

Params:None

Return:None
'''
def _check_battery_status():
	battery_info=psutil.sensors_battery()
	battery_percentage = battery_info.percent #grabbing the battery percent
	is_plugged_in = battery_info.power_plugged # grabbing the info whether the battery is is_plugged_in or not !
	if is_plugged_in and float(battery_percentage) > 95.00:
		notification.notify("PC Util v1.0", "Please Remove The Charging Cable, The Battery is 95%+ !", timeout = 10)
	elif not is_plugged_in and float(battery_percentage) < 90.00:
		notification.notify("PC Util v1.0", "Please Plug In The Charger, Your Battery Is Less Than 25% !", timeout = 10)


'''
This function will call the above function in an interval of 2 secs, so that it can check the status at each iteration

params: None

Return: None

'''
def check_battery_status():
	schedule.every(30).seconds.do(_check_battery_status)
	while  1:
		schedule.run_pending()
		sleep(1)


def do_tasks():
	schedule.every(30).seconds.do(_check_battery_status)
	schedule.every(2).minutes.do(_change_wallpaper)
	while True:
		schedule.run_pending()
		sleep(1)

do_tasks() # function to execute the scheduled tasks 
