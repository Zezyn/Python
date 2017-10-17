string=str(input('enter a string: ')) 
maxcount=0 
tempMax=0 
maxcharacter = string[0] 
for a in string: 
    for b in string: 
        if a == b: 
            tempMax += 1 
if tempMax > maxcount: 
    maxcount = tempMax 
    maxcharacter = a 
    tempMax=0 
print(maxcharacter, 'came up', str(maxcount), 'times')
