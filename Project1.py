"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Růžek
email: michalruzek@seznam.cz
discord: Michal R#1452
"""

from codecs import BOM_BE
from itertools import count
from task_template import TEXTS
oddelovac='-'*35
cache={}
login= {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
user = input('Insert your username: ')
password= input('Insert your password: ')
print('-'*35)



if login.get(user)==password:
    print(f'Welcome to the app, {user}.','We have three texts to be analyzed', sep='\n' )
else:
    print('unregistered user, terminating program..')
    quit()

print('-'*35)
cislo= input('Enter a number btw. 1 and 3 to select: ')
if cislo.isnumeric():
    if 0 < int(cislo) < 4:
        print('-'*35)
    else:
        print('Number not between 1 and 3, terminating program...')
else:
    print('number is not numeric, terminating program...')

selection = TEXTS[int(cislo)-1]
countofWords= len(selection.split())
countofTitlecase = sum(map(str.istitle, selection.split()))
countofUppercase = sum (map(str.isupper, selection.split()))
countofLowercase = sum (map(str.islower, selection.split()))
countofnumeric = sum (map(str.isnumeric, selection.split()))
sumup= [int(s) for s in selection.split() if s.isdigit()]
print('There are', countofWords ,'words in the selected text.')
print('There are', countofTitlecase ,'titlecase words.')
print('There are', countofUppercase ,'uppercase words.')
print('There are', countofLowercase ,'lowercase words.')
print('There are', countofnumeric ,'numeric strings.')
print(f'The sum of all the numbers is {sum(sumup)}.')
print(oddelovac,"""  LEN|    OCCURENCES      |NR.""",oddelovac,sep='\n')
rozdeleni=selection.split()
for slovo in rozdeleni:
    if len(slovo) not in cache:
        cache[len(slovo)]=1
    else:
        cache[len(slovo)]=cache[len(slovo)]+1
for key, value in sorted(cache.items()):
    print(f"{key:4} | {'*'*value:<19}| {value}")
print(oddelovac)


