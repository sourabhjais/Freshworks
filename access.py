#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import Thread 
import code as data 
#importing the main file("code" is the name of the file I have used) as a library 


data.create("hello",45)
#to create a key with key_name,value given and with no time-to-live property


data.create("hey",90,3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


data.read("hello")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


data.read("hey")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


data.create("hello",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


data.modify("hello",55)
#it replaces the initial value of the respective key with new value 

 
data.delete("hello")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like



key_name="Hello";value=25;timeout=0
t1=Thread(target=(data.create),args=(key_name,value,timeout))

t1.start()
t2=Thread(target=(data.read),args=(key_name,)) 
t2.start()

t3=Thread(target=(data.delete),args=(key_name,))
t3.start()


#and so on upto tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
