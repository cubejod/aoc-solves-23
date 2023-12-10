with open("day5input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]

start=0
seeds=[]
for i in range(len(data[0])):
    if data[0][i]==":":
        start=i+2
temp=""
for i in range(start,len(data[0])):
    if data[0][i]==" ":
        seeds.append(int(temp))
        temp=""
    else:
        temp+=data[0][i]
seeds.append(int(temp))
seeds2=seeds.copy()
start=3
maps=[]
for k in range(7):
    maps=[]
    for i in range(start,len(data)):
        tempMap=[]
        if data[i]!="":
            if not (data[i][0].isdigit()):
                start=i+1
                break
            temp=""
            for j in range(len(data[i])):
                if data[i][j]==" ":
                    tempMap.append(temp)
                    temp=""
                else:
                    temp+=data[i][j]
            tempMap.append(temp)
        if len(tempMap)!=0:
            maps.append(tempMap)
    for i in range(0,len(seeds)):
        for j in range(len(maps)):
            if seeds[i]>=int(maps[j][1]) and seeds[i]<=(int(maps[j][1])+int(maps[j][2])-1):
                seeds[i]-=int(maps[j][1])-int(maps[j][0])
                break

print(min(seeds))
ranges=[]
for i in range(0,len(seeds2),2):
    ranges.append([seeds2[i],seeds2[i]+seeds2[i+1]-1])

def solve(num):
    start=3
    maps=[]
    for k in range(7):
        maps=[]
        for i in range(start,len(data)):
            tempMap=[]
            if data[i]!="":
                if not (data[i][0].isdigit()):
                    start=i+1
                    break
                temp=""
                for j in range(len(data[i])):
                    if data[i][j]==" ":
                        tempMap.append(temp)
                        temp=""
                    else:
                        temp+=data[i][j]
                tempMap.append(temp)
            if len(tempMap)!=0:
                maps.append(tempMap)
        for j in range(len(maps)):
            if num>=int(maps[j][1]) and num<=(int(maps[j][1])+int(maps[j][2])-1):
                num-=int(maps[j][1])-int(maps[j][0])
                break
    return num
things=[]
nums=[]
for i in range(len(ranges)):
    for j in range(ranges[i][0],ranges[i][1]+1,100000):
        thing=solve(j)
        things.append(thing)
        nums.append(j)
minIndex=things.index(min(things))
minRange=nums[minIndex]
realNums=[]
for i in range(minRange-100000,minRange+100000):
    thing=solve(i)
    realNums.append(thing)
print(min(realNums))