numbers=[1,2,2,2,2,3,1,2]
count = {}
i =0
while i<len(numbers):
          if numbers[i] in count:
            count[numbers[i]] +=1
          else:
             count[numbers[i]]=1
          i+=1   
print( "the number appears:", count)
