numbers= [10,20,5,20,15]
largest = numbers[0]
Second_largest = numbers [0]
i=0
while i<len(numbers) :
               if numbers[i] > largest:
                   Second_largest =largest
                   largest = numbers[i]
                   
               elif numbers[i]>Second_largest and numbers[i]<largest:
                      Second_largest = numbers[i]
               i+=1
print(" the second largest numbers is : ",Second_largest ) 
