a=int(input("enter the number:"))
smallest=9
while a>0:
          digit=a%10
          if digit<smallest:
                  smallest=digit
          a=a//10
print(smallest)                              
