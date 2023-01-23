ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)
print("minimmum age in list is:", min(ages))
print("Maximum age in list is: ",max(ages))
ages.append(max(ages))
ages.append(min(ages))
ages.sort()
print(ages)
m=len(ages)//2
if len(ages)%2==1:
    print("median is:",ages[m])
else:
    print("median is:",(ages[m]+ages[m+1])/2)
print("Range is:",max(ages)-min(ages))