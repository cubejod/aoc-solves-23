import copy
with open("day14input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
    
for i in range(len(data)):
    data[i]=list(data[i])
def north(data):
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i]=="O":
                for k in range(j-1,-1,-1):
                    if data[k][i]==".":
                        data[k+1][i]="."
                        data[k][i]="O"
                    else:
                        break
def south(data):
    for i in range(len(data[0])):
        for j in range(len(data)-1,-1,-1):
            if data[j][i]=="O":
                for k in range(j+1,len(data)):
                    if data[k][i]==".":
                        data[k-1][i]="."
                        data[k][i]="O"
                    else:
                        break
def east(data):
    for i in range(len(data)):
        for j in range(len(data[i])-1,-1,-1):
            if data[i][j]=="O":
                for k in range(j+1,len(data[i])):
                    if data[i][k]==".":
                        data[i][k-1]="."
                        data[i][k]="O"
                    else:
                        break
def west(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=="O":
                for k in range(j-1,-1,-1):
                    if data[i][k]==".":
                        data[i][k+1]="."
                        data[i][k]="O"
                    else:
                        break
output=0
storage=[]
loops=0
storage.append(copy.deepcopy(data))
north(data)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="O":
            output+=len(data)-i 
print(output)

west(data)
south(data)
east(data)
loops+=1
if data in storage:
    print(f"loops after {loops} times!")
# 1 cycle already done
for i in range(10000):
    north(data)
    west(data)
    south(data)
    east(data)
    loops+=1
    if data in storage:
        a=storage.index(data)
        b=loops-a-1
        break
    else:
        storage.append(copy.deepcopy(data))
output2=0
mod=(1000000000-(a+1))%b
for i in range(mod):
    north(data)
    west(data)
    south(data)
    east(data)

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="O":
            output2+=len(data)-i 
print(output2)