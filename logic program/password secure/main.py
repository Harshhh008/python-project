SECURE=(('s','$'),('a','@'),('i','!'),('o','*'),('and','&'),('p','?'),('1','L'),('h','#'))

def passwordsecure(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

password = input("Enter your password:")
new_password = passwordsecure(password)
print("your secure password is :")
print(new_password)


with open("passwordsecure.txt","a") as ps:
    ps.write(password+" : "+new_password+"\n")