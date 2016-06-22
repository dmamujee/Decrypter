# -------------------------------------------------------------------------------
# Name:Decrypter.py
# Purpose: A program that will encrypt a message and allow the user to decrypt it
#
# Author: Mamujee. D
#
# Created: 31/10/2013
# -------------------------------------------------------------------------------

import random


# Creates the class Message
class Message:
    # Allows the user to enter sting when instance is created
    def __init__(self, message=""):
        # Makes the passkey "password" and encapsulates it
        self.__key = "password"
        temp_list = []
        i = 0
        # Add the string into a list and encrypts it by adding 1 to the ASCII value
        while i < len(message):
            temp = ord(message[i]) + 1
            temp_list.append(chr(temp))
            i += 1
        # Encapsulates the encrypted string
        self.__message = temp_list

    # Method that outputs the encrypted string
    def __str__(self):
        output = ""
        message = self.get_message()
        i = 0
        while i < len(message):
            output = output + message[i]
            i += 1
        return "The message is: " + output

    # Method that decrypts message
    def decrypt(self, key=""):
        # If key given is correct, the message is decrypted and outputed
        if key == self.get_key():
            i = 0
            message = self.get_message()
            output = ""
            while i < len(message):
                temp = ord(message[i]) - 1
                output += chr(temp)
                i += 1
            return output
        # If key is incorrect, then message is outputed as random characters
        else:
            i = 0
            message = self.get_message()
            output = ""
            while i < len(message):
                temp = random.randint(32, 126)
                output += chr(temp)
                i += 1
            return output

    # Method that returns encapsulated message
    def get_message(self):
        return self.__message

    # Method that returns encapsulated pass code key
    def get_key(self):
        return self.__key


# Testing Log
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
