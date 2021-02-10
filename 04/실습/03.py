admin = "admin"
pw = 1234

def id_pw_check(a,b):
  if(a == admin and b==1234):
    print("Welcome, admin")
  elif(a==admin and b!=1234):
    print("Wrong password")
  else:
    print("You are not admin")


id_pw_check()