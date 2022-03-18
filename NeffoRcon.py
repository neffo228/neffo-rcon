import os, sys, time, subprocess, colorama, requests
from os import system
from colorama import init, Fore, Style
from subprocess import Popen

def main():
    os.system('cls')
    ip = input("Айпи: ")
    port = input("Порт: ")
    password = input("Пароль: ")
    os.system('cls')
    print(f"Подключаюсь к {ip}")
    title = f"NeffoRcon @{ip}"
    system("title " + title)
    startcmd = f"mcrcon {ip} --port {port} --password {password}"
    Popen(startcmd, shell=False)

def passw():
    passwrd = "neffo"
    passf = input("Ключ доступа: ")
    if passf == passwrd:
        print("Ключ доступа верный, вы получили доступ к NeffoRcon!")
        time.sleep(1)
        main()
    else:
        print("Вы ввели недействительный ключ доступа!")
        passw()

def banner():
    nefforcon = '''
  _    _       __  __      _____              
 | \ | |     / _|/ _|    |  __ \                
 |  \| | ___| |_| |_ ___ | |__) |___ ___  _ __  
 | . ` |/ _ \  _|  _/ _ \|  _  // __/ _ \| '_ \ 
 | |\  |  __/ | | || (_) | | \ \ (_| (_) | | | |
 |_| \_|\___|_| |_| \___/|_|  \_\___\___/|_| |_|
             By @Neffo                                  
    '''
    print(Fore.GREEN + Style.DIM + nefforcon) 
    time.sleep(1)
    passw()

os.system('cls')
title = "NeffoRcon"
system("title " + title)
banner()

# mcrcon 0.0.0.0 --port 123 --password 123