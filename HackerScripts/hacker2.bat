@echo off
:random
color 07
ipconfig /all
color 7c
ping -n 3 -w 1 127.0.0.1
goto :random