password= "A12390844a"
email ="A1239084a"
if password == "":
     print("password must not be empty")
elif not len(password) >= 8:
       print("password must be atleast 8 characters")
elif not any (ch.isupper() for ch in password )   :
        print("password must contain atleast 1 uppercase")
elif not any (ch.islower() for ch in password ) :
       print("password must be atleast 1 lowercase")
elif password == email:
      print("password must not be equal to email")    
elif " " in  password:
      print("password must not contain spaces")
elif not(password[0].isalnum() and password[-1].isalnum()):
      print("password must start or end with leter or digit")  
else :
      print("password is correct")
