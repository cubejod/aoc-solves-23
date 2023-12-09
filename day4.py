with open("day4input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]

output=0
originals=[]
for i in range(len(data)):
    winning=[]
    tempNum=""
    start=0
    winCount=0
    for j in range(len(data[i])):
        if data[i][j]==":":
            start=j+1
    for j in range(start,len(data[i])):
        if data[i][j]!=" ":
            tempNum+=data[i][j]
        else:
            if tempNum!="":
                winning.append(tempNum)
            tempNum=""
        if data[i][j]=="|":
            start=j+2
            break
    tempNum=""
    for j in range(start,len(data[i])):
        if data[i][j]!=" ":
            tempNum+=data[i][j]
        else:
            if tempNum in winning:
                winCount+=1
            tempNum=""
    if tempNum in winning:
        winCount+=1
    if winCount>0:
        output+=2**(winCount-1)
    originals.append(int(winCount))

count=[1] * len(originals)
for i in range(len(count)):
    for j in range(i+1,i+1+int(originals[i])):
        count[j]+=count[i]

print(output)
print(sum(count))
