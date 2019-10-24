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
port = 9000
s.connect((host,port))

def print_profile():
    incoming_username = s.recv(1024) 
    incoming_username = incoming_username.decode()

    incoming_password = s.recv(1024) 
    incoming_password = incoming_password.decode()

    incoming_fname = s.recv(1024) 
    incoming_fname = incoming_fname.decode()

    incoming_lname = s.recv(1024) 
    incoming_lname = incoming_lname.decode()

    incoming_gender = s.recv(1024) 
    incoming_gender = incoming_gender.decode()

    incoming_interest = s.recv(1024) 
    incoming_interest = incoming_interest.decode()

    incoming_age = s.recv(1024) 
    incoming_age = incoming_age.decode()

    incoming_child = s.recv(1024) 
    incoming_child = incoming_child.decode()

    incoming_ethnic = s.recv(1024) 
    incoming_ethnic = incoming_ethnic.decode()

    incoming_religion = s.recv(1024) 
    incoming_religion = incoming_religion.decode()

    incoming_school = s.recv(1024) 
    incoming_school = incoming_school.decode()

    incoming_career = s.recv(1024) 
    incoming_career = incoming_career.decode()

    incoming_sports = s.recv(1024) 
    incoming_sports = incoming_sports.decode() 

    incoming_football = s.recv(1024) 
    incoming_football = incoming_football.decode()

    incoming_baseball = s.recv(1024) 
    incoming_baseball = incoming_baseball.decode()

    incoming_basketball = s.recv(1024) 
    incoming_basketball = incoming_basketball.decode() 

    incoming_soccer = s.recv(1024) 
    incoming_soccer = incoming_soccer.decode()

    incoming_other = s.recv(1024) 
    incoming_other = incoming_other.decode()

    incoming_movies = s.recv(1024) 
    incoming_movies = incoming_movies.decode() 

    incoming_music = s.recv(1024) 
    incoming_music = incoming_music.decode()

    incoming_dance = s.recv(1024) 
    incoming_dance = incoming_dance.decode()

    incoming_social = s.recv(1024) 
    incoming_social = incoming_social.decode()

    incoming_reading = s.recv(1024) 
    incoming_reading = incoming_reading.decode()

    incoming_bio = s.recv(1024) 
    incoming_bio = incoming_bio.decode()

    print(incoming_bio)


def header():
    print("""              ██████╗ ██╗     ██╗   ██╗███████╗    ██████╗ ██╗██████╗ ██████╗ 
              ██╔══██╗██║     ██║   ██║██╔════╝    ██╔══██╗██║██╔══██╗██╔══██╗ 
              ██████╔╝██║     ██║   ██║█████╗      ██████╔╝██║██████╔╝██║  ██║
              ██╔══██╗██║     ██║   ██║██╔══╝      ██╔══██╗██║██╔══██╗██║  ██║
              ██████╔╝███████╗╚██████╔╝███████╗    ██████╔╝██║██║  ██║██████╔╝
              ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝ """)

def create_account(conn):    #informs server that there is a need to create a new account
    s.send(login.encode())
    cls2()
    set_name = input(str("\nSet Username: "))
    set_name = set_name.encode()
    s.send(set_name)

    cls2()
    set_password = input(str("\nSet Password: "))
    set_password = set_password.encode()
    s.send(set_password)

    cls2()
    set_firstname = input(str("\nWhat's your first name?: "))
    set_firstname = set_firstname.encode()
    s.send(set_firstname)

    cls2()
    set_lastname = input(str("\nWhat's your last name?: "))
    set_lastname = set_lastname.encode()
    s.send(set_lastname)

    cls2()
    set_gender = input(str("\nWhat's your gender? Female('1') or Male('2') : "))
    set_gender = set_gender.encode()
    s.send(set_gender)

    cls2()
    set_interest = input(str("\nAre you interested in Women('1') or Men('2')? : "))
    set_interest = set_interest.encode()
    s.send(set_interest)

    cls2()
    set_age = input(str("\nWhat's your age? Examples: '23' or '35' : "))
    set_age = set_age.encode()
    s.send(set_age)

    cls2()
    set_child = input(str("\nDo you have children? No('1') or Yes('2') : "))
    set_child = set_child.encode()
    s.send(set_child)

    cls2()
    set_ethnic = input(str("\nWhat's your ethnic background? Examples: Caucasian, African-American, Asian, etc : "))
    set_ethnic = set_ethnic.encode()
    s.send(set_ethnic)

    cls2()
    set_religion = input(str("\nWhat's your religion? : "))
    set_religion = set_religion.encode()
    s.send(set_religion)

    cls2()
    set_school = input(str("\nWhat's your highest level of education? : "))
    set_school = set_school.encode()
    s.send(set_school)

    cls2()
    set_career = input(str("\nWhat's your occupation? : "))
    set_career = set_career.encode()
    s.send(set_career)

    cls2()
    set_sports = input(str("\nDo you like sports? No('1') or Yes('2') : "))
    set_sports = set_sports.encode()
    s.send(set_sports)

    cls2()
    set_football = input(str("\nDo you like football? No('1') or Yes('2') : "))
    set_football = set_football.encode()
    s.send(set_football)

    cls2()
    set_baseball = input(str("\nDo you like baseball? No('1') or Yes('2') : "))
    set_baseball = set_baseball.encode()
    s.send(set_baseball)

    cls2()
    set_basketball = input(str("\nDo you like basketball? No('1') or Yes('2') : "))
    set_basketball = set_basketball.encode()
    s.send(set_basketball)
    
    cls2()
    set_soccer = input(str("\nDo you like soccer? No('1') or Yes('2') : "))
    set_soccer = set_soccer.encode()
    s.send(set_soccer)

    cls2()
    set_other = input(str("\nDo you like any other sport? No('1') or Yes('2') : "))
    set_other = set_other.encode()
    s.send(set_other)

    cls2()
    set_movies = input(str("\nDo you like movies? No('1') or Yes('2') : "))
    set_movies = set_movies.encode()
    s.send(set_movies)

    cls2()
    set_music = input(str("\nDo you like music? No('1') or Yes('2') : "))
    set_music = set_music.encode()
    s.send(set_music)

    cls2()
    set_dance = input(str("\nDo you like dance? No('1') or Yes('2') : "))
    set_dance = set_dance.encode()
    s.send(set_dance)

    cls2()
    set_social = input(str("\nDo you like social media? No('1') or Yes('2') : "))
    set_social = set_social.encode()
    s.send(set_social)

    cls2()
    set_reading = input(str("\nDo you like reading? No('1') or Yes('2') : "))
    set_reading = set_reading.encode()
    s.send(set_reading)

    cls2()
    set_bio = input(str("\nPlease complete the form by writing a few sentences,\nwhich will be you profile's bio? : "))
    set_bio = set_bio.encode()
    s.send(set_bio)

    print("\nAccount Created\n")

def do_not_create_account():    #informs server that there is no need to create a new account
    s.send(login.encode())

def login_retry():
    print ("Invalid username or password\n")
    name = input(str("\nUsername: "))
    password = input(str("\nPassword: "))
    send_name()
   
def send_name():
    s.send(name.encode())   #sends name to server
    s.send(password.encode())

def inMessage():
    while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        if (incoming_message == "start print_profile"):
            print_profile()
        else:
            print(incoming_message,"\n")

def outMessage():           #Constantly allows for messages to be sent from client
    while 1:
        message = input(str("")) 
        message = message.encode()
        print("\n")
        s.send(message)


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    header()
    print("\n   MY PROFILE('1')      MESSAGES('2')      MATCH ME('3')      SEARCH('4')      OPTIONS('5)\n");

def cls2():  #only for the create account function
    os.system('cls' if os.name=='nt' else 'clear')
    header()
    print("\n                                  Account Creation Menu\n")

def cls3():  #for profile function
    os.system('cls' if os.name=='nt' else 'clear')
    header()

header()
login = input(str("\n\n                      Create a new account('1') or Login('2'): "))
if (login == "1"):
     create_account()
else:
     do_not_create_account()

name = input(str("\nUsername: "))
password = input(str("\nPassword: "))

t1 = threading.Thread(target=outMessage,) 
t2 = threading.Thread(target=inMessage,)

send_name()
cls()

t1.start() 
t2.start() 
  
t1.join() 
t2.join() 
