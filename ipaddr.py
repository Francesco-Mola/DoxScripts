#!/usr/bin/env python

#Created by Respire
#Copyright RespireDev © 2014
#https://github.com/respiredev

# Wait a minute?!  Didn't you copy this from Matthew Blankenship?!!!  I think so, Francesco!!!
# Err...  Embarassing.

from bs4 import BeautifulSoup

import mechanize
import cookielib
import sys

ip = sys.argv[1]

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()

host = 'http://www.whatismyipaddress.com/ip/' + ip

def getip(br, cj, host):
        br.set_cookiejar(cj)
        br.addheaders = [('User-agent','Firefox')]
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        code = br.open(host)
        html = code.read()
        soup = BeautifulSoup(html)
        table = soup.findAll('table')[0]
        rows = table.findAll('tr')
        for row in rows:
                print row.th.text,
                print row.td.text

def main():
        getip(br, cj, host)

main()
