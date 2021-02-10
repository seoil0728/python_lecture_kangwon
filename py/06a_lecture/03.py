import string
def Check_passwd(pwd):
    if(len(pwd) < 8):
        print("password should be at least 8")
    elif(pwd[0] not in string.ascii_lowercase):
        print("first letter should be a lower letter")
    elif(pwd[-1] not in string.digits or pwd[-2] not in string.digits):
        print("last two letters should be numbers")
    else:
        print("Nice Password!")

passwd = input("Enter your Password: ")
Check_passwd(passwd)