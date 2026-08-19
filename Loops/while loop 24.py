a=int(input("enter the number:"))
largest=0
while a>0:
          digit=a%10
          if digit>largest:
                  largest=digit
          a=a//10
print(largest)
