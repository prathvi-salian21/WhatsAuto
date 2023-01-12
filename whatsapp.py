import pywhatkit
import pyautogui
#import speech_recognition
import pyttsx3
import time
mr=pyttsx3.init()
vc=mr.getProperty('voices')
mr.setProperty('voice',vc[1].id)

import mysql.connector
from datetime import datetime
#making database coonect to our code
#database: XAMPP
#database name:wtsup
#table name:user1(name varchar,phn varchar)
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wtsup"
)
mycursor=mydb.cursor()
mr.say("Hello. Welcome to Prathvi's  WhatsAuto!")
mr.runAndWait()
while(1):
    #menu
    print("1.add user\n2.send msg\n3.display\n4.exit")
    mr.say("press 1 to add new contact. Press 2 to send a message to a person from your contact list. And Press 3 to display the user and 4 to exit from the terminal")
    mr.runAndWait()
    print("Enter choice")
    ch=int(input())
    if ch==1:
        #adding new contact
        mr.say("Enter the user's name and phone number along with the country code")
        mr.runAndWait()
        print("Enter name :",end=" ")
        name=input()
        print("enter phone no :",end=" ")
        phn=input()
        
        str="insert into user1(name,phn)values('%s','%s')"
        val=(name,phn)
        mycursor.execute(str %val)
        mydb.commit()
        mr.say("contact successfully saved!")
        mr.runAndWait()
    if ch==2:
        #sending message
        mr.say("Enter the recipient's name ")
        mr.runAndWait()
        print("Enter the recipient's name :",end=" ")
        nm=input()
        #accessing user's phone number from database using their name
        str="select phn from user1 where name='"+nm+"'"
        mycursor.execute(str)
        phnno=" "
        
        myval=mycursor.fetchall()
        for x in myval:
            phnno=x[0]
        if phnno!=' ':

            mr.say("Enter the message to be sent ")
            mr.runAndWait() 
            print("Enter the message to be sent :",end=" ")  
            msg=input()
            
            '''tm=datetime.now()
            crmin=tm.strftime("%M")
            finalmin=t1+int(crmin)
            crhr=tm.strftime("%H")
            finalhr=int(crhr)'''
            mr.say("for how many times, the message is to be sent?")
            mr.runAndWait()
            print("enter the no. of times the msg be sent!",end=" ")
            num=int(input())
            mr.say("Enter at what time the message to be sent in 24 hour format ")
            mr.runAndWait()
            print("set the timer:")
            finalhr=int(input('Hour :'))
            finalmin=int(input('Minute :'))
            pywhatkit.sendwhatmsg(phnno,msg,finalhr,finalmin)
            time.sleep(2)
            count=0
            #pyautogui for sending the message multiple times
            while(count<num):
                pyautogui.typewrite(msg)
                pyautogui.press("enter")
                count+=1
            mr.say("Message  "+msg+"  send successfully to "+nm)
            mr.runAndWait()
        else:
            mr.say("no such person exist in your contact list")
            mr.runAndWait()
    if ch==3:
        #showing contacts saved
        mr.say("Here are the list of your contacts.")
        mr.runAndWait()
        str="select *from user1"
        mycursor.execute(str)
        res=mycursor.fetchall()
        for i in res:
            print(i)
    if ch==4:
        #exiting
        mr.say("Thankyou for using Prathvi's WhatsAuto.Till next time.")
        mr.runAndWait()
        break
    if ch<4:
        #invalid choice
        mr.say("The choice value must be between 1 to 4")
        mr.runAndWait()