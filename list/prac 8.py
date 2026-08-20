numbers = [4, 7, 12, 9, 20, 15, 2]
largest =0
second_largest=numbers[0]
for i in numbers:
                 if i>largest :
                    second_largest=largest
                    largest=i
                  
                   
                 elif i<largest and i>second_largest:
                    second_largest=i
print(second_largest)
