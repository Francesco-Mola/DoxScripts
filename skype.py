#!/usr/bin/env python
# coding=utf-8

# '-------------------------------'
# skype.py Created by Respire
# '-------------------------------'
#!/usr/bin/env python
# coding=utf-8

#Created by Respire
#Copyright RespireDev © 2015
#https://github.com/respiredev

import requests
import sys
import re
import urllib3

urllib3.disable_warnings()

#Simple Class Color
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False 
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
       
        return False
has_colours = has_colours(sys.stdout)

def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)
                
# Resolver:
printout("*\--------------------------------------\*\r\n"  , RED) 
printout("Python Skype Resolver ~ Created by Respire\r\n"  , CYAN)
printout("*\--------------------------------------\*\r\n" , RED) 

username = raw_input('> Skype Username: ')

#BetaResolver API
betaresolver = requests.get("http://api.betaresolver.fr/apifree.php", params={'key': '146530553', 'username': username}, verify=False)

found = re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', betaresolver.content)
if len(found) > 0:
    for ip in found:
        print('[!] BetaResolver API')
        print("> Found: %s"%ip)
print('\r\n')

#Idk Public API? lol
data = requests.get('https://www.hackthatapi.com/?command=7&username=%s'%username, verify=False)

ip = data.content

print('[!] HackThatAPI: ')
print('> Found IP: %s'%ip)

#GoResolver

gores = requests.get('http://goresolver.com/free.php?key=052cae565fd3a3d23ac831b9f51892c2&user=%s'%username, verify=False)

goip = gores.content

print('[!] GoResolver API: ')
print('> Found IP: %s'%goip)

#SkypeGrab

skypegrab = requests.get('http://skypegrab.net/api.php?key=Yvht6Tbiudma53kGXE&username=%s'%username, verify=False)

skip = skypegrab.content

print('[!] SkypeGrab API:')
print('> Found IP: %s'%goip)
