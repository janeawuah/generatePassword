#Author: Jane Awuah
# Date: Thursday 29th July, 2021.
#
# This is a code to find the product of two numbers from a give csv file that will add up to 2020.

#HOW I WILL GO ABOUT IT#
#  First I will load the file 
#Get the size of the numbers
# loop through the file with the number of numbers
# find the key and value pair and use another loop to go through the file
# add the two values from the loops and find the one that adds up to 2020
#nultiply these two and output the value



#
# Future Word
# 
# Ask for the user to inter the file name
# then ask for the sum that is to be expected
# 
# 
# My very first for fun code, I am Happy erh!!!!!!!!!!!##

import random
#import string

#a function to shuffle all characters

def shuffle(string):
    temps = list(string)
    random.shuffle(temps)
    return ''.join(temps)


#the main 
upperCase1 =chr(random.randint(65,90)) # this generates an upper case randomly using ASCII code
upperCase2 =chr(random.randint(65,90)) # this generates an upper case randomly using ASCII code
upperCase3 =chr(random.randint(65,90)) # this generates an upper case randomly using ASCII code
upperCase4 =chr(random.randint(65,90)) # this generates an upper case randomly using ASCII code


numb1 = random.randint(0,9) # this generates digits
numb2 =random.randint(0,9) # this generates digits
numb3 =random.randint(0,9) # this generates digits

lowerCase1 =chr(random.randint(97,123)) # this generates an lower case randomly using ASCII code
lowerCase2 =chr(random.randint(97,123)) # this generates an lower case randomly using ASCII code
lowerCase3 =chr(random.randint(97,123)) # this generates an lower case randomly using ASCII code
lowerCase4 =chr(random.randint(97,123)) # this generates an lower case randomly using ASCII code



otherChar1 =chr(random.randint(48,58)) # this generates an lower case randomly using ASCII code
otherChar2 =chr(random.randint(48,58)) # this generates an lower case randomly using ASCII code

#from here, I will now generate the password
passWord = upperCase1 + upperCase2 + upperCase3 + upperCase4 + str(numb1) + str(numb2) + str(numb3) + lowerCase1 + lowerCase2 + lowerCase3 + lowerCase4 + otherChar1 + otherChar2
passWord = shuffle(passWord)

#my expected output
print(passWord)