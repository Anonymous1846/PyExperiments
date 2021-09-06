#!/usr/bin/python3


#Author: Sharath Sunil
#A simple python script for displaying ascii art on linux terminal

import os
import pyfiglet 
from random import choice


USERNAME = os.getenv('USER')

print_username = pyfiglet.figlet_format(f'Hello {USERNAME} !', font = "slant")
print_meme1 = pyfiglet.figlet_format('Noob',font='doh') 
print_meme2 = pyfiglet.figlet_format('Hey I Use  Linux !')
print_meme3 = pyfiglet.figlet_format('Exception Occured !!')
print_meme4 = pyfiglet.figlet_format('Whoknows !',font='slant')

possible_titles = [print_username,print_meme1,print_meme2,print_meme3,print_meme4]
print(choice(possible_titles))
