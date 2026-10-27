num=int(input("enter a number:"))   
sum=0          
while num>0:
             i=num % 10
             sum=sum+ i
             num=num //10
print("the sum is:", sum)  
