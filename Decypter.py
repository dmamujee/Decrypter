#-------------------------------------------------------------------------------
#Name:Decrypter.py
#Purpose: A program that will encrypt a message and allow the user to decrypt it
#
#Author: Mamujee. D
#
#Created: 31/10/2013
#-------------------------------------------------------------------------------

import random

#Creates the class Message
class Message():
    #Allows the user to enter sting when instance is created
    def __init__(self,message = ""):
        #Makes the passkey "password" and encapsulates it
        self.__key = "password"
        List = []
        i = 0
        #Add the string into a list and encrypts it by adding 1 to the ASCII value
        while i < len(message):
            temp = ord(message[i]) + 1
            List.append(chr(temp))
            i += 1
        #Encapsulates the encrypted string
        self.__message = List

    #Method that outputs the encrypted string
    def __str__ (self):
        output = ""
        message = self.get_Message()
        i = 0
        while i < len(message):
            output = output + message[i]
            i += 1
        return "The message is: " + output
            
    #Method that decrypts message           
    def decrypt(self,key = ""):
        #If key given is correct, the message is decrypted and outputed
        if key == self.get_Key():
            i = 0
            message = self.get_Message()
            output = ""
            while i < len(message):
                temp = ord(message[i]) - 1
                output = output + chr(temp)
                i += 1
            return output
        #If key is incorrect, then message is outputed as random characters
        else:
            i = 0
            message = self.get_Message()
            output = ""
            while i < len(message):
                temp = random.randint(32,126)
                output = output + chr(temp)
                i += 1
            return output
        
    #Method that returns encapsulated message
    def get_Message(self):
        return self.__message

    #Method that returns encapsulated passcode key
    def get_Key(self):
        return self.__key

#Testing Log
a = Message("Testing1")
print(a)
print(a.decrypt("password"))
print(a.decrypt("incorrectPassword"))


b = Message("Characters:;.,!?[]{}\|@#$%^&*()_-=+/*`~")
print(b)
print(b.decrypt("password"))
print(b.decrypt("incorrectPassword"))
print(b.decrypt(123))
print(b.decrypt(True))
print(b.decrypt())


