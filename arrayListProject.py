numDays = int(input('Enter the number of days: '))
count = 0
tempList = []
while (count < numDays):
    count += 1
    temp = int(input('Enter %d day\'s temperature' % count))
    tempList.append(temp)


avg = (sum(tempList) / numDays)
print(avg)

days = 0
for i in tempList:
    if (i>avg):
       days+=1

print(' %d Days above average temp' %days)
