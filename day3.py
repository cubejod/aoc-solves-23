with open("day3input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
digits=["1","2","3","4","5","6","7","8","9","0"]
output=0
curNum=""
symbols=[]
nums=[]
using=[]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=="*":
            symbols.append([i,j])
            nums.append([])
for i in range(len(data)):
    if curNum!="":
        if symbol:
            for k in range(len(symbols)):
                    if symbols[k]==using[0]:
                        nums[k].append(curNum)
            output+=int(curNum)
            curNum=""
            symbol=False
        else:
            curNum=""
            symbol=False
            using=[]
    curNum=""
    symbol=False
    for j in range(len(data[i])):
        if data[i][j] in digits:
            curNum+=str(data[i][j])
            if i!=0:
                if j!=0:
                    if (data[i-1][j-1] not in digits) and data[i-1][j-1]!=".":
                        symbol=True
                        if [i-1,j-1] not in using:
                            using.append([i-1,j-1])
                if (data[i-1][j] not in digits) and data[i-1][j]!=".":
                    symbol=True
                    if [i-1,j] not in using:
                        using.append([i-1,j])
                if j+1!=len(data[i]):
                    if (data[i-1][j+1] not in digits) and data[i-1][j+1]!=".":
                        symbol=True
                        if [i-1,j+1] not in using:
                            using.append([i-1,j+1])
            if j!=0:
                if (data[i][j-1] not in digits) and data[i][j-1]!=".":
                        symbol=True
                        if [i,j-1] not in using:
                            using.append([i,j-1])
            if j+1!=len(data[i]):

                if (data[i][j+1] not in digits) and data[i][j+1]!=".":
                        symbol=True
                        if [i,j+1] not in using:
                            using.append([i,j+1])
            if i+1!=len(data):
                if j!=0:
                    if (data[i+1][j-1] not in digits) and data[i+1][j-1]!=".":
                        symbol=True
                        if [i+1,j-1] not in using:
                            using.append([i+1,j-1])
                if (data[i+1][j] not in digits) and data[i+1][j]!=".":
                    symbol=True
                    if [i+1,j] not in using:
                        using.append([i+1,j])
                if j+1!=len(data[i]):
                    if (data[i+1][j+1] not in digits) and data[i+1][j+1]!=".":
                        symbol=True
                        if [i+1,j+1] not in using:
                            using.append([i+1,j+1])
        else:
            if curNum!="":
                if symbol:
                    for k in range(len(symbols)):
                        if symbols[k]==using[0]:
                            nums[k].append(curNum)
                    output+=int(curNum)
                    curNum=""
                    symbol=False
                else:
                    curNum=""
                    symbol=False
            using=[]
if curNum!="":
    if symbol:
        for k in range(len(symbols)):
            if symbols[k]==using[0]:
                nums[k].append(curNum)
        output+=int(curNum)
        curNum=""
        symbol=False
    else:
        curNum=""
        symbol=False
output2=0
for i in range(len(nums)):
    if len(nums[i])==2:
        output2+=int(nums[i][0])*int(nums[i][1])
print(output)
print(output2)