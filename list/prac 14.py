numbers = [4, 0, 7, 0, 12, 9, 0, 20]
result=[]
zero_count=0
for  i in numbers:
                if i!=0:
                        result.append(i)
for i in numbers:
                   if i==0:
                           zero_count=zero_count+1
for i in range(zero_count):
                          result.append(0)
print(result)     
