import re
'''
A Simple Python Script to seperate the username and the domain name
'''

email_id = input('Enter the Email Id : ')
#we have to first check whether email is valid or not !
# we will evaluate the emails xyz123@gamil.com
#abc@somemail.eu
#the username comes before the @
if re.search('[\w]+\@[a-zA-Z]+\.[a-z]{2,3}',email_id):
	username,domain=email_id[:email_id.index('@')],email_id[email_id.index('@')+1:]
	print(f'Username->\t{username}\nDomain->\t{domain}')
else:
	print('Sorry the email is invalid !!')
