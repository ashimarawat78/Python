a= int(input("enter the number:"))
sum=0
while a>0:
          digit= a%10
          if digit%2!=0:
             sum=sum+1
          a=a//10
print(sum)   
