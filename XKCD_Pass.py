from __future__ import print_function
import random

f = open("1000_Common_words.txt")
txt = f.read()
lines = txt.split()

chars = 'abcdefghijklmnopqrstuvwxyz' \
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
        '1234567890' \
        ')(*&^%$#@!'

yes = {'yes','y', 'ye'}
no = {'no', 'n'}

def XKCD():
    password = ''

    length = input("How many words? ")
    length = int(length)

    for c in range(length):
        password += '_' + random.choice(lines)
    print(password)

def charPass():
    password = ''
    length = input("Password length? ")
    length = int(length)
    for c in range(length):
        password += random.choice(chars)
    print(password)

choice = input("Would you like an XKCD password? [y/n] ").lower()
if choice in yes:
    XKCD()
else:
    charPass()




