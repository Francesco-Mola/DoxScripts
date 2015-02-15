#!/usr/bin/env python
# coding=utf-8

# '-------------------------------'
# GitHub Email Puller
# '-------------------------------'

#Created by Respire
#Copyright RespireDev © 2015
#https://github.com/respiredev

import requests
import json
import sys
from colorama import init

username = raw_input('\033[1;36m[+] Input the Username: \033[1;m')

r = requests.get('https://api.github.com/users/%s'%username, verify=True)

#Check JSON output for information. 
#If No information is present, print NULL
#Except all KeyErrors, Error Checks.

try:
	login = r.json()['login']
	print('[!] Login Name: %s'%login)
except KeyError:
	print('[!] Login Name: NULL ')

try:
	email = r.json()['email']
	print('[!] Email: %s'%email)
except KeyError:
	print('[!] Email: NULL ')

try:
	id = r.json()['id']
	print('[!] ID: %s'%id)
except KeyError:
	print('[!] ID: NULL ')

try:
	type = r.json()['type']
	print('[!] Type: %s'%type)
except KeyError:
	print('[!] Type: NULL ')

try:
	admin = r.json()['site_admin']
	print('[!] Admin: %s'%admin)
except KeyError:
	print('[!] Admin: NULL ')

try:
	blog = r.json()['blog']
	print('[!] Blog: %s'%blog)
except KeyError:
	print('[!] Blog: NULL ')

try:
	location = r.json()['location']
	print('[!] Location: %s'%location)
except KeyError:
	print('[!] Location: NULL ')

try:
	bio = r.json()['bio']
	print('[!] Bio: %s'%bio)
except KeyError:
	print('[!] Bio: NULL ')

try:
	created = r.json()['created_at']
	print('[!] Date Created: %s'%created)
except KeyError:
	print('[!] Date Created: NULL ')

try:
	updated = r.json()['updated_at']
	print('[!] Date Updated: %s'%updated)
except KeyError:
	print('[!] Date Updated: NULL ')
