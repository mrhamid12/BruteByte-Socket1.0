import art
from socket import *
import socket
import sys

lgo = "BruteBytes"
print(art.text2art(lgo))
print("SOCKET BY BRUTEBYTE")
print("This is used to create a socket not anything serious!!!")
socket_name = input("Enter Socket Name : ")

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create " + str(socket_name))
    print("REASON: " + str(err))
    sys.exit()
print(str(socket_name) + " created :) ")

lhost=input("Host Name (example: www.abcd.com) : ")
lport=input("Type in port number (Default Port:8080) : ")

try:
    sock.connect((lhost,int(lport)))
    print("Socket connected to : " + str(lhost)+":"+str(lport))
except socket.error as err:
    print("The Host name " + str(lhost) + " is wrong ")
    print("REASON: "+ str(err))
    sys.exit()

print("Success :)")


    
