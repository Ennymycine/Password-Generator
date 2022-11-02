#To import necessary modules necessary for a password generator

import secrets
import string
import random

#To define the necessary parameters in the password (alphabets, digits and special characters)
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

#To assign one value to the passwords
password_combination = letters+digits+special_chars

password_length = 15

#To generate a password string

password = ''
for i in range(password_length):
  password+= ''.join(secrets.choice(password_combination))

            
print("The random password is " + "". join(password))
        
       
