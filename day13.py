with open("day13input.txt") as f:
    data=f.readlines()
    data=[l.rstrip() for l in data]
lines=[]
output=0
output2=0
temp=[]
for i in range(len(data)):
    if len(data[i])!=0:
        temp.append(data[i])
    else:
        lines.append(temp)
        temp=[]
lines.append(temp)
for i in range(len(lines)):
    temp2=[]
    for j in range(len(lines[i][0])):
        temp2.append([])
        for k in range(len(lines[i])):
            temp2[j].append(lines[i][k][j])
    for j in range(1,len(lines[i][0])):
        lp=j-1
        rp=j
        diff=0
        wrong=0
        while lp>=0 and rp<len(temp2):
            if temp2[lp]!=temp2[rp]:
                diff+=1
                for z in range(len(temp2[lp])):
                    if temp2[lp][z]!=temp2[rp][z]:
                        wrong+=1
            lp-=1
            rp+=1
        if diff==0:
            output+=j
        if wrong==1:
            output2+=j

    for j in range(1,len(lines[i])):
        lp=j-1
        rp=j
        diff=0
        wrong=0
        while lp>=0 and rp<len(lines[i]):
            if lines[i][lp]!=lines[i][rp]:
                for z in range(len(lines[i][lp])):
                    if lines[i][lp][z]!=lines[i][rp][z]:
                        wrong+=1
                diff+=1
            lp-=1
            rp+=1
        if diff==0:
            output+=100*j
        if wrong==1:
            output2+=100*j
print(output)
print(output2)