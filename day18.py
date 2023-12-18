from collections import Counter
import matplotlib.path as pth
import numpy as np
with open("day18input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]


#MORONIC GARBAGE THAT TAKES FOREVER TO RUN AND HAS NO CHANCE OF BRUTE FORCING P2
""" d=0
r=0
maxD=0
maxR=0
minD=0
minR=0
for i in range(len(data)):
    data[i]=data[i].split(" ")
    if data[i][0]=="R":
        r+=int(data[i][1])
    elif data[i][0]=="D":
        d+=int(data[i][1])
    elif data[i][0]=="U":
        d-=int(data[i][1])
    elif data[i][0]=="L":
        r-=int(data[i][1])
    maxD=max(maxD,d)
    maxR=max(maxR,r)
    minD=min(minD,d)
    minR=min(minR,r)
print(maxD,maxR)
print(minD,minR)
arr=[]
for i in range(1000):
    arr.append(["."] * (1000))

arr[500][500]="#"
x=500
y=500
path=[]
path.append((x,y))
for i in range(len(data)):
    if data[i][0]=="R":
        for j in range(int(data[i][1])):
            arr[x][y+1]="#"
            path.append((x,y+1))
            y+=1
    elif data[i][0]=="L":
        for j in range(int(data[i][1])):
            arr[x][y-1]="#"
            path.append((x,y-1))
            y-=1
    elif data[i][0]=="U":
        for j in range(int(data[i][1])):
            arr[x-1][y]="#"
            path.append((x-1,y))
            x-=1
    else:
        for j in range(int(data[i][1])):
            arr[x+1][y]="#"
            path.append((x+1,y))
            x+=1


output2=0
polygon=pth.Path(path)
points=[]

for i in range(1000):
    for j in range(1000):
        if (i,j) not in path:
            points.append((i,j))

inPoly = polygon.contains_points(points)
for i in range(len(inPoly)):
    if inPoly[i]==True:
        output2+=1
for i in range(len(arr)):
    c=Counter(arr[i])
    output2+=c["#"]


for i in range(len(arr)):
    left=99999
    right=99999
    for j in range(len(arr[i])-1):
        if arr[i][j]=="#" and arr[i][j+1]!="#":
            left=j
            break
    for j in range(len(arr[i])-1,0,-1):
        if arr[i][j]=="#" and arr[i][j-1]!="#":
            right=j
            break
    if left!=99999 and j!=99999:
        for j in range(left,right):
            arr[i][j]="#"
output=0
for i in range(len(arr)):
    c=Counter(arr[i])
    output+=c["#"]
print(output)
print(output2) """
#ACTUALLY VIABLE CODE (you can tell bc i had to steal something)

# https://stackoverflow.com/a/30408825
def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
instructions=[]
main=[]
for i in range(len(data)):
    data[i]=data[i].split(" ")
    if data[i][2][-2]=="0":
        instructions.append(("R",int(data[i][2][2:7],16)))
    elif data[i][2][-2]=="1":
        instructions.append(("D",int(data[i][2][2:7],16)))
    elif data[i][2][-2]=="2":
        instructions.append(("L",int(data[i][2][2:7],16)))
    elif data[i][2][-2]=="3":
        instructions.append(("U",int(data[i][2][2:7],16)))
    main.append((data[i][0],int(data[i][1])))

xVals=[0]
yVals=[0]
loc=[0,0]
it=0
b=0
for i in range(len(main)):
    b+=main[i][1]
    if main[i][0]=="R":
        loc[1]+=main[i][1]
    elif main[i][0]=="L":
        loc[1]-=main[i][1]
    elif main[i][0]=="U":
        loc[0]-=main[i][1]
    elif main[i][0]=="D":
        loc[0]+=main[i][1]
    xVals.append(loc[0])
    yVals.append(loc[1])
xVals=np.array(xVals, dtype=np.float64)
yVals=np.array(yVals, dtype=np.float64)

it+=int(PolyArea(xVals,yVals))
#a+1-(b/2)=i
i=it+1-(b/2)
print(int(i+b))

xVals=[0]
yVals=[0]
loc=[0,0]
it=0
b=0
for i in range(len(instructions)):
    b+=instructions[i][1]
    if instructions[i][0]=="R":
        loc[1]+=instructions[i][1]
    elif instructions[i][0]=="L":
        loc[1]-=instructions[i][1]
    elif instructions[i][0]=="U":
        loc[0]-=instructions[i][1]
    elif instructions[i][0]=="D":
        loc[0]+=instructions[i][1]
    xVals.append(loc[0])
    yVals.append(loc[1])
xVals=np.array(xVals, dtype=np.float64)
yVals=np.array(yVals, dtype=np.float64)


it+=int(PolyArea(xVals,yVals))
#a+1-(b/2)=i
i=it+1-(b/2)
print(int(i+b))