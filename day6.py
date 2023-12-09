with open("day6input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]


data[0]=data[0][7:].split(" ")
data[1]=data[1][10:].split(" ")
times=[]
distances=[]
times2=""
distances2=""
for i in range(len(data[0])):
    if data[0][i]!="":
        times.append(int(data[0][i]))
        times2+=data[0][i]
for i in range(len(data[1])):
    if data[1][i]!="":
        distances.append(int(data[1][i]))
        distances2+=data[1][i]



output=1
for i in range(len(times)):
    temp=0
    for j in range(0,int(times[i])):
        if (int(times[i])-j)*j>int(distances[i]):
            temp+=1
    output*=temp
print(output)
output=0

for i in range(0,int(times2)):
    if(int(times2)-i)*i>int(distances2):
        output+=1



print(output)
    