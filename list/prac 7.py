numbers = [4, 7, 12, 9, 20, 15, 2]
sum=0
avg=0
count=0
for i in numbers:
               if i>10:
                      sum=sum+i
                      count=count+1
                      avg= sum/count
print(avg)
