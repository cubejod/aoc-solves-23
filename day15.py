with open("day15input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
strings=[]
temp=""
data=data[0]
for i in range(len(data)):
    if data[i]!=",":
        temp+=data[i]
    else:
        strings.append(temp)
        temp=""
strings.append(temp)
output=0
hMap={}
for i in range(len(strings)):
    value=0
    for j in range(len(strings[i])):
        value+=ord(strings[i][j])
        value*=17
        value=value%256
        if strings[i][j]=="=":
            hMap[strings[i][0:j]]=int(strings[i][j+1:])
        if strings[i][j]=="-":
            if strings[i][0:j] in hMap:
                del hMap[strings[i][0:j]]
    output+=value
print(output)
output2=0
def hasher(thing):
    value=0
    for i in range(len(thing)):
        value+=ord(thing[i])
        value*=17
        value=value%256
    return value
boxes = [[] for _ in range(256)]
for key,value in hMap.items():
    boxes[hasher(key)].append(value)
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        output2+=(i+1)*(j+1)*int(boxes[i][j])
print(output2)