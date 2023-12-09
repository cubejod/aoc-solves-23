with open("day2input.txt") as f:
    data=f.readlines()

output=0
output2=0
start=0
nums=["1","2","3","4","5","6","7","8","9","0"]


for i in range(len(data)):
    maxr=0
    maxg=0
    maxb=0
    flag=True
    for j in range(len(data[i])):
        if data[i][j]==":":
            start=j+1
    for j in range(start,len(data[i])):
        num=""
        rgb=0
        last=0
        if data[i][j]==" ":
            for k in range(j+1,len(data[i])):
                if data[i][k] in nums:
                    num+=data[i][k]
                else:
                    last=k
                    break
            if data[i][last+1]=="r":
                rgb=1
            elif data[i][last+1]=="g":
                rgb=2
            else:
              rgb=3
            if num!="":
                if int(num)>maxr and rgb==1:
                        maxr=int(num)
                if int(num)>maxg and rgb==2:
                        maxg=int(num)
                if int(num)>maxb and rgb==3:
                        maxb=int(num)
                if rgb==1 and int(num)>12:
                    flag=False
                elif rgb==2 and int(num)>13:
                    flag=False
                elif rgb==3 and int(num)>14:
                    flag=False
    if flag:
        output+=i+1
    output2+=maxr*maxg*maxb
    
print(output)
print(output2)
