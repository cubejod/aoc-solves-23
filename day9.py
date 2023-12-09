with open("day9input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]

def zeroCheck(data):
    for i in range(len(data)):
        if data[i]!=0:
            return False
    return True

output=0
output2=0
realDiff=[]
for i in range(len(data)):
    differences=[]
    differences.append(list(map(int,data[i].split(" "))))
    flag=True
    times=0
    while flag==True:
        temp=[]
        for j in range(1,len(differences[times])):
            temp.append(differences[times][j]-differences[times][j-1])
        times+=1
        differences.append(temp)
        if zeroCheck(differences[times])==True:
            flag=False
    realDiff.append(differences)

realDiff2=realDiff.copy()

for i in range(len(realDiff)):
    num=0
    for j in range(len(realDiff[i])-2,-1,-1):
        realDiff[i][j].append(realDiff[i][j][-1]+num)
        num=realDiff[i][j][-1]
    output+=realDiff[i][0][-1]

for i in range(len(realDiff2)):
    num=0
    for j in range(len(realDiff2[i])-2,-1,-1):
        realDiff[i][j].insert(0,realDiff2[i][j][0]-num)
        num=realDiff2[i][j][0]
    output2+=realDiff2[i][0][0]

print(output)
print(output2)