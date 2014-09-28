# '-------------------------------'
# skype.py Created by Respire
# '-------------------------------'

import requests
import sys
import re

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
data = requests.get("http://betaresolver.fr//api/apifree.php", params={'key': 'free', 'pseudo': username})

found = re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', data.content)
if len(found) > 0:
    for ip in found:
        print("Found: %s"%ip)
print('\r\n')
