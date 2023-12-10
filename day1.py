import re

with open("day1input.txt") as f:
    data=f.readlines()
output=0
output2=0
ints=["1","2","3","4","5","6","7","8","9","0"]
things=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in range(len(data)):
    first=""
    last=""
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            first=data[i][j]
            break
    for j in range(len(data[i])-1,-1,-1):
        if data[i][j].isdigit():
            last=data[i][j]
            break
    output+=int(first+last)





for i in range(len(data)):
    findex=999999
    lindex=0
    first=0
    last=0
    temp=""
    for j in range(len(things)):
        if things[j] in data[i]:
            a=data[i].index(things[j])
            if a<findex:
                findex=a
                first=things[j]
            if a>lindex:
                lindex=a
                last=things[j]
    for j in range(len(things)):
        if things[j] in data[i]:
            a=data[i].rfind(things[j])
            if a<findex:
                findex=a
                first=things[j]
            if a>lindex:
                lindex=a
                last=things[j]
    table={
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
           }
    if first!=0:
        first=table[first]
    if last!=0:
        last=table[last]

    useTemp1=True
    useTemp2=True
    for j in range(0,len(data[i])):
        if data[i][j] in ints:
            if j<=findex:
                useTemp1=False
                temp+=data[i][j]
                break
    if useTemp1==True:
        temp+=str(first)
    for j in range(len(data[i])-1,-1,-1):
        if  data[i][j] in ints:
            if j>=lindex:
                useTemp2=False
                temp+=data[i][j]
                break
    if useTemp2==True:
        temp+=str(last)
    output2+=int(temp)
print(output)
print(output2)