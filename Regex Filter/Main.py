import random
import os
import re
def create_details_list():
    # we already have a Names list with Random Names
    with open('Names.txt','r') as f:
        names_list=f.readlines()
    names,emails,numbers=[],['@gamil.com','@outlook.com','@yahoo.com','@hotmail.com'],['1','2','3','4','5','6','7','8','9','0']
    for name in names_list:
        names.append(name.replace('\n',''))

    file_names=open('Details.txt','w')
    for  _ in range(len(names)):
        #choosing a random first name and last name
        first_name,last_name=random.choice(names),random.choice(names)
        #email in the format name<some-random-number>@<gmail,yahoo,outlook>.com
        email=(first_name+''.join(random.sample(numbers,2))+random.choice(emails)).lower()
        #phone number starts with 0 as per indian standards
        phone=f"+{random.choice(['0','512','31','43','88','1'])} {''.join(random.choice(numbers) for i in range(10))}"
        #writing to a file
        file_names.write(f'{first_name} {last_name}\n{email}\n{phone}\n\n')
        #closing the file streams !
    file_names.close()

def seperate():
    #the regex for first name and last name !
    name_finder=re.compile(r'([a-zA-Z]{3,15}\s*)+ ([a-zA-Z]{3,15})')
    #finding the format '+ <some-numbers> space 10numbers' 
    phone_number=re.compile(r'\+[\d]+\s[0-9]{10}')
    #seperating the email in the format <username>@<domain-name>.com/edu/eu
    email_finder=re.compile(r'[\w]+\@[A-Za-z]+\.[a-z]{2,3}')
    names_file,email_file,phone_file=open('NamesOnly.txt','w'),open('EmailOnly.txt','w'),open('PhoneOnly.txt','w')
    with open('Details.txt') as f:
            full_details=f.read()
            #in the for loops we find the pattern for number, email and name, finally we segregate the details and store them in different files
    for phone in phone_number.finditer(full_details):
        phone_file.writelines(f'{full_details[phone.span()[0]:phone.span()[1]]}\n')
    for email in email_finder.finditer(full_details):
        email_file.writelines(f'{full_details[email.span()[0]:email.span()[1]]}\n')
    for name in name_finder.finditer(full_details):
        #the span tuple allows to get the ending and starting index of the text of characters
        names_file.writelines(f'{full_details[name.span()[0]:name.span()[1]]}\n')
#first we check if the details exists in the Details.txt file/other words if the file exists !
if os.path.exists('./Details.txt'):
    # if the file exists then we can perform the seperation of the names, phone numbers and email
    seperate()
else:
    #we first invoke the create details function to create the details file and then call the sepertor !
    create_details_list()
    seperate()