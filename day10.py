import matplotlib.path as pth
with open("day10input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        if data[i][j]=="S":
            s=[i,j]
starts=[]
length=1
up=data[s[0]-1][s[1]]
down=data[s[0]+1][s[1]]
left=data[s[0]][s[1]-1]
right=data[s[0]][s[1]+1]
dir1=""
dir2=""
if up=="|" or up=="7" or up== "F":
    starts.append([s[0]-1,s[1]])
if down=="|" or down=="L" or down=="J":
    starts.append([s[0]+1,s[1]])
if left=="-" or left=="L" or left=="F":
    starts.append([s[0],s[1]-1])
if right=="-" or right=="7" or right=="J":
    starts.append([s[0],s[1]+1])

direction="down"
path=[(s[0],s[1])]
while starts[0]!=s:
    a=starts[0].copy()
    path.append((a[0],a[1]))
    cur=data[starts[0][0]][starts[0][1]]
    if cur=="|":
        if direction=="down":
            starts[0][0]+=1
            direction="down"
        else:
            starts[0][0]-=1
            direction="up"
    elif cur=="-":
        if direction=="right":
            starts[0][1]+=1
            direction="right"
        else:
            starts[0][1]-=1
            direction="left"
    elif cur=="L":
        if direction=="down":
            starts[0][1]+=1
            direction="right"
        else:
            starts[0][0]-=1
            direction="up"
    elif cur=="J":
        if direction=="right":
            starts[0][0]-=1
            direction="up"
        else:
            starts[0][1]-=1
            direction="left"
    elif cur=="7":
        if direction=="right":
            starts[0][0]+=1
            direction="down"
        else:
            starts[0][1]-=1
            direction="left"
    elif cur=="F":
        if direction=="left":
            starts[0][0]+=1
            direction="down"
        else:
            starts[0][1]+=1
            direction="right"
    length+=1

print(length//2)

output2=0
polygon=pth.Path(path)
points=[]

for i in range(140):
    for j in range(140):
        if (i,j) not in path:
            points.append((i,j))

inPoly = polygon.contains_points(points)

for i in range(len(inPoly)):
    if inPoly[i]==True:
        output2+=1

print(output2)