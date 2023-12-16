import sys
with open("day16input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
    sys.setrecursionlimit(100000)


seen=[]
dupes=[]
output=0
def traverse(x,y,direction):
    global output
    if [x,y] not in seen:
        seen.append([x,y])
        output+=1
    if [x,y,direction] in dupes:
        return 0
    else:
        dupes.append([x,y,direction])
    if data[x][y]==".":
        if direction=="E":
            if y+1<len(data[x]):
                traverse(x,y+1,direction)
        elif direction=="W":
            if y-1>=0:
                traverse(x,y-1,direction)
        elif direction=="S":
            if x+1<len(data):
                traverse(x+1,y,direction)
        elif direction=="N":
            if x-1>=0:
                traverse(x-1,y,direction)

    elif data[x][y]=="/":
        if direction=="E":
            if x-1>=0:
                traverse(x-1,y,"N")
        elif direction=="W":
            if x+1<len(data):
                traverse(x+1,y,"S")
        elif direction=="N":
            if y+1<len(data[x]):
                traverse(x,y+1,"E")
        elif direction=="S":
            if y-1>=0:
                traverse(x,y-1,"W")

    elif data[x][y]=="\\":
        if direction=="E":
            if x+1<len(data):
                traverse(x+1,y,"S")
        elif direction=="W":
            if x-1>=0:
                traverse(x-1,y,"N")
        elif direction=="N":
            if y-1>=0:
                traverse(x,y-1,"W")
        elif direction=="S":
            if y+1<len(data[x]):
                traverse(x,y+1,"E")

    elif data[x][y]=="|":
        if direction=="E":
            if x-1>=0:
                traverse(x-1,y,"N")
            if x+1<len(data):
                traverse(x+1,y,"S")
        elif direction=="W":
            if x-1>=0:
                traverse(x-1,y,"N")
            if x+1<len(data):
                traverse(x+1,y,"S")
        elif direction=="N":
            if x-1>=0:
                traverse(x-1,y,direction)
        elif direction=="S":
            if x+1<len(data):
                traverse(x+1,y,direction)

    elif data[x][y]=="-":
        if direction=="E":
            if y+1<len(data[x]):
                traverse(x,y+1,direction)
        elif direction=="W":
            if y-1>=0:
                traverse(x,y-1,direction)
        elif direction=="N":
            if y-1>=0:
                traverse(x,y-1,"W")
            if y+1<len(data[x]):
                traverse(x,y+1,"E")
        elif direction=="S":
            if y-1>=0:
                traverse(x,y-1,"W")
            if y+1<len(data[x]):
                traverse(x,y+1,"E")

traverse(0,0,"E")
print(output)
maxE=output
for i in range(len(data[0])):
    output=0
    seen=[]
    dupes=[]
    traverse(0,i,"S")
    if output>maxE:
        maxE=output
    output=0
    seen=[]
    dupes=[]
    traverse(len(data)-1,i,"N")
    if output>maxE:
        maxE=output
for i in range(len(data)):
    output=0
    seen=[]
    dupes=[]
    traverse(i,0,"E")
    if output>maxE:
        maxE=output
    output=0
    seen=[]
    dupes=[]
    traverse(i,len(data[0])-1,"W")
    if output>maxE:
        maxE=output
print(maxE)