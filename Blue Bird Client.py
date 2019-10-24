import os
os.system('color 1f')
import socket #adds socket library
import sys
import time
from _thread import *
import threading 
import subprocess

time.sleep(1)
s = socket.socket()         #Defines Socket
host = "127.0.0.1"
print("BLUE BIRD\n")
port = 9000
s.connect((host,port))

def create_account():    #informs server that there is a need to create a new account
    s.send(login.encode())
    print("Account Creation Menu\n")
    set_name = input(str("\nSet Username: "))
    set_name = set_name.encode()
    s.send(set_name)

    set_password = input(str("\nSet Password: "))
    set_password = set_password.encode()
    s.send(set_password)
    
    set_email = input(str("\nSet Email: "))
    set_email = set_email.encode()
    s.send(set_email)

    set_zip = input(str("\nSet Zip Code : "))
    set_zip = set_zip.encode()
    s.send(set_zip)
    print("\nAccount Created\n")

def do_not_create_account():    #informs server that there is no need to create a new account
    s.send(login.encode())

def login_info():
    name = input(str("\nUsername: "))
    password = input(str("\nPassword: "))
   
def send_name():
    s.send(name.encode())   #sends name to server
    s.send(password.encode())

def inMessage():
    while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        if (incoming_message == "Identify"):    #Returns the user's name to client(when asked by server)
            s.send(name.encode())
        else:
            print(incoming_message,"\n")

def outMessage():           #Constantly allows for messages to be sent from client
    while 1:
        message = input(str("")) 
        message = message.encode()
        print("\n")
        s.send(message)

login = input(str("Welcome - Create a new account(Enter '1'): "))
if (login == "1"):
     create_account()
else:
     do_not_create_account()

name = input(str("\nUsername: "))
password = input(str("\nPassword: "))

t1 = threading.Thread(target=outMessage,) 
t2 = threading.Thread(target=inMessage,)

send_name()
t1.start() 
t2.start() 
  
t1.join() 
t2.join() 
