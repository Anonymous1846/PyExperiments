import ctypes
import os
import random
import schedule
from time import sleep
#the directory where the photos where the photos are stored and it can be changed !
PIC_DIRECTORY=f'C:\\Users\\{os.getlogin()}\\Pictures\\Camera Roll'
EXTS=['jpg','jpeg','png']
#filtering out only the pictures with png, jpg, and jpeg !
PICS=[picture for picture in os.listdir(PIC_DIRECTORY) if any(picture.endswith(extension) for extension in EXTS)]
def change_wallpaper():
	#a random pic is chosen from the list !
	wallpaper=random.choice(PICS)
	#the path to the wallpapper provided in the third parameter !
	ctypes.windll.user32.SystemParametersInfoW(20, 0,os.path.join(PIC_DIRECTORY,wallpaper), 0)

schedule.every(2).minutes.do(change_wallpaper)
while True:
	schedule.run_pending()
	sleep(1)
