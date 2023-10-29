# Password generator

#import modules
import random
import string

#asking the user for lenght
length = int(input("\n Enter the Length of the password : "))


#data 

lower = "abcdefghijklmnopqrstuvwxyz"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

digits = "1234567890"

symbols = "!@#$%^&*()_"

all_combine = lower + upper + digits + symbols


#shuffling
temp = random.sample(all_combine,length)


#creating password
password = "".join(temp)


print(f"Password :{password}n")

