a =int(input("enter the number:"))
original=a
rev =0
while a>0:
         digit = a%10
         rev= rev*10+digit
         a=a//10
if original==rev:
    print("pallindrome")
else:
    print("not a palliindrome") 
