#!/usr/bin/env python
# coding=utf-8

# '-------------------------------'
# GitHub Email Puller
# '-------------------------------'

#Created by Respire
#Copyright RespireDev © 2015
#https://github.com/respiredev

import re
import requests
import json
import sys
from colorama import init


username = raw_input('\033[1;36m[+] Input the Username: \033[1;m')


r = requests.get('https://api.github.com/users/%s'%username, verify=True)
name = r.json()['name']
login = r.json()['login']
email = r.json()['email']
id = r.json()['id']
type = r.json()['type']
admin = r.json()['site_admin']
blog = r.json()['blog']
location = r.json()['location']
bio = r.json()['bio']
created = r.json()['created_at']
updated = r.json()['updated_at']


print('[!] Name: %s'%name)
print('[!] Login Name: %s'%login)
print('[!] Email: %s'%email)
print('[!] ID: %s'%id)
print('[!] Type: %s'%type)
print('[!] Admin: %s'%admin)
print('[!] Blog: %s'%blog)
print('[!] Location: %s'%location)
print('[!] Bio: %s'%bio)
print('[!] Date Created: %s'%created)
print('[!] Date Updated: %s'%updated)
