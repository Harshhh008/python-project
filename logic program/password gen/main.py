import random
import string

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

length = int(input("Enter your password length: "))
name = input("why u need password:")
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
password = ("".join(s[0:length]))
print("your password is: ")
print(name+" : "+password)

with open("password.txt","a") as ps:
    ps.write(name + " : "+password+"\n")