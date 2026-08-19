a= int(input("enter the number:"))
count=0
while a>0:
          digit= a%10
          if digit%2==0:
                   count=count+1
          a=a//10
print(count)  
