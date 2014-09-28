#!/bin/bash

#Created by Respire
#Copyright RespireDev © 2014
#https://github.com/respiredev

echo "[+] Searchin for dis nigga: $1 in all of our hacked databases. ;)==="
grep --color -rwn $1 /root/DB/*
