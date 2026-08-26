numbers = [10, 25, 7, 30, 25, 18, 25]
a=int(input("enter the value :"))
last_index=-1
for i in range (len(numbers)):
                     if numbers[i]==a:
                                 last_index=i
print(last_index)  
