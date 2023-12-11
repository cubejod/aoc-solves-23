with open("day11input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
data2=data.copy()
for i in range(len(data)):
    data[i]=list(data[i])
col=[]
row=[]
for i in range(len(data[0])):
    flag=True
    for j in range(len(data)):
        if data[j][i]=="#":
            flag=False
            break
    if flag:
        col.append(i-1)
for i in range(len(data)):
    flag=True
    for j in range(len(data[0])):
        if data[i][j]=="#":
            flag=False
            break
    if flag:
        row.append(i-1)

for i in range(len(col)-1,-1,-1):
    for j in range(len(data)):
        data[j].insert(col[i]+1,".")

rowLen=len(data[0])
empty = ["."] * rowLen
for i in range(len(row)-1,-1,-1):
    data.insert(row[i]+1,empty)

num=1
pos=[]
output=0
diffs=[]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="#":
            data[i][j]=str(num)
            num+=1
            pos.append((i,j))
for i in range(0,len(pos)):
    for j in range(i+1,len(pos)):
        output+=abs((pos[j][0]-pos[i][0]))+abs(pos[j][1]-pos[i][1])
        diffs.append(abs((pos[j][0]-pos[i][0]))+abs(pos[j][1]-pos[i][1]))
print(output)


for i in range(len(data2)):
    data2[i]=list(data2[i])

num=1
pos=[]
output2=0
for i in range(len(data2)):
    for j in range(len(data2[i])):
        if data2[i][j]=="#":
            data2[i][j]=str(num)
            num+=1
            pos.append((i,j))

diffs2=[]
for i in range(0,len(pos)):
    for j in range(i+1,len(pos)):
        diffs2.append(abs((pos[j][0]-pos[i][0]))+abs(pos[j][1]-pos[i][1]))
        output2+=abs((pos[j][0]-pos[i][0]))+abs(pos[j][1]-pos[i][1])

trueDiffs=[]
for i in range(len(diffs)):
    trueDiffs.append(diffs[i]-diffs2[i])

print(sum(trueDiffs)*999999+output2)