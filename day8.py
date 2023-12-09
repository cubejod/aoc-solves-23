import math
with open("day8input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
steps=data[0]
output=0
nodes={}
for i in range(2,len(data)):
    nodes[data[i][0:3]]=[data[i][7:10],data[i][12:15]]
current="AAA"
while True:
    for i in range(len(steps)):
        thing=nodes.get(current)
        if steps[i]=="L":
            current=thing[0]
        else:
            current=thing[1]
        output+=1
        if current=="ZZZ":
            break
    if current=="ZZZ":
        break
print(output) 

output2=1
def stepCounter(current):
    temp=0
    while True:
        for i in range(len(steps)):
            thing=nodes.get(current)
            if steps[i]=="L":
                current=thing[0]
            else:
                current=thing[1]
            temp+=1
            if current[2]=="Z":
                break
        if current[2]=="Z":
            break
    return temp
currents=[]
for i in range(2,len(data)):
    if data[i][2]=="A":
        currents.append(data[i][0:3])
for i in range(len(currents)):
    output2=math.lcm(output2,stepCounter(currents[i]))
print(output2)