from collections import Counter
with open("day7input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
ranks=[]
five=[]
four=[]
full=[]
three=[]
tp=[]
op=[]
hc=[]
for i in range(len(data)):
    data[i]=data[i].split(" ")


for i in range(len(data)):
    c=Counter(data[i][0])
    best=0
    jokers=c["J"]

    for j, value in enumerate(c.values()):
        
        if value==5:
            best=6
        elif value==4:
            if best<5:
                best=5
        elif value==3 and len(c)==2:
            if best<4:
                best=4
        elif value==3:
            if best<3:
                best=3
        elif value==2 and len(c)==3:
            if best<2:
                best=2
        elif value==2:
            if best<1:
                best=1
        else:
            if best<0:
                best=0
    if jokers==5:
        best=6
    if jokers==4:
        best=6
    if jokers==3:
        if len(c)==3:
            best=5
        else:
            best=6
    if jokers==2:
        if best==1:
            best=3
        elif best==2:
            best=5
        elif best==4:
            best=6
    if jokers==1:
        if best==0:
            best=1
        elif best==1:
            best=3
        elif best==2:
            best=4
        elif best==3:
            best=5
        elif best==5:
            best=6

    if best==6:
        five.append(data[i])
    elif best==5:
        four.append(data[i])
    elif best==4:
        full.append(data[i])
    elif best==3:
        three.append(data[i])
    elif best==2:
        tp.append(data[i])
    elif best==1:
        op.append(data[i])
    else:
        hc.append(data[i])

cardToRank={
    "J":0,
    "2":1,
    "3":2,
    "4":3,
    "5":4,
    "6":5,
    "7":6,
    "8":7,
    "9":8,
    "T":9,
    "Q":11,
    "K":12,
    "A":13
}

for i in range(len(five) - 1):
    for j in range(len(five) - i - 1):
        for k in range(5):
            if cardToRank[five[j][0][k]]<cardToRank[five[j+1][0][k]]:
                five[j],five[j+1]=five[j+1],five[j]
                break
            if cardToRank[five[j][0][k]]>cardToRank[five[j+1][0][k]]:
                break
for i in range(len(four) - 1):
    for j in range(len(four) - i - 1):
        for k in range(5):
            if cardToRank[four[j][0][k]]<cardToRank[four[j+1][0][k]]:
                four[j],four[j+1]=four[j+1],four[j]
                break
            if cardToRank[four[j][0][k]]>cardToRank[four[j+1][0][k]]:
                break
for i in range(len(full) - 1):
    for j in range(len(full) - i - 1):
        for k in range(5):
            if cardToRank[full[j][0][k]]<cardToRank[full[j+1][0][k]]:
                full[j],full[j+1]=full[j+1],full[j]
                break
            if cardToRank[full[j][0][k]]>cardToRank[full[j+1][0][k]]:
                break

for i in range(len(three) - 1):
    for j in range(len(three) - i - 1):
        for k in range(5):
            if cardToRank[three[j][0][k]]<cardToRank[three[j+1][0][k]]:
                three[j],three[j+1]=three[j+1],three[j]
                break
            if cardToRank[three[j][0][k]]>cardToRank[three[j+1][0][k]]:
                break
for i in range(len(tp) - 1):
    for j in range(len(tp) - i - 1):
        for k in range(5):
            if cardToRank[tp[j][0][k]]<cardToRank[tp[j+1][0][k]]:
                tp[j],tp[j+1]=tp[j+1],tp[j]
                break
            if cardToRank[tp[j][0][k]]>cardToRank[tp[j+1][0][k]]:
                break
for i in range(len(op) - 1):
    for j in range(len(op) - i - 1):
        for k in range(5):
            if cardToRank[op[j][0][k]]<cardToRank[op[j+1][0][k]]:
                op[j],op[j+1]=op[j+1],op[j]
                break
            if cardToRank[op[j][0][k]]>cardToRank[op[j+1][0][k]]:
                break
for i in range(len(hc) - 1):
    for j in range(len(hc) - i - 1):
        for k in range(5):
            if cardToRank[hc[j][0][k]]<cardToRank[hc[j+1][0][k]]:
                hc[j],hc[j+1]=hc[j+1],hc[j]
                break
            if cardToRank[hc[j][0][k]]>cardToRank[hc[j+1][0][k]]:
                break
            
output=0

for i in range(len(hc)-1,-1,-1):
    ranks.append(int(hc[i][1]))
for i in range(len(op)-1,-1,-1):
    ranks.append(int(op[i][1]))
for i in range(len(tp)-1,-1,-1):
    ranks.append(int(tp[i][1]))
for i in range(len(three)-1,-1,-1):
    ranks.append(int(three[i][1]))
for i in range(len(full)-1,-1,-1):
    ranks.append(int(full[i][1]))
for i in range(len(four)-1,-1,-1):
    ranks.append(int(four[i][1]))
for i in range(len(five)-1,-1,-1):
    ranks.append(int(five[i][1]))

for i in range(len(ranks)):
    output+=ranks[i]*(i+1)
p2=output


ranks=[]
five=[]
four=[]
full=[]
three=[]
tp=[]
op=[]
hc=[]


for i in range(len(data)):
    c=Counter(data[i][0])
    best=0

    for j, value in enumerate(c.values()):
        
        if value==5:
            best=6
        elif value==4:
            if best<5:
                best=5
        elif value==3 and len(c)==2:
            if best<4:
                best=4
        elif value==3:
            if best<3:
                best=3
        elif value==2 and len(c)==3:
            if best<2:
                best=2
        elif value==2:
            if best<1:
                best=1
        else:
            if best<0:
                best=0
   


    if best==6:
        five.append(data[i])
    elif best==5:
        four.append(data[i])
    elif best==4:
        full.append(data[i])
    elif best==3:
        three.append(data[i])
    elif best==2:
        tp.append(data[i])
    elif best==1:
        op.append(data[i])
    else:
        hc.append(data[i])









cardToRank={
    "2":1,
    "3":2,
    "4":3,
    "5":4,
    "6":5,
    "7":6,
    "8":7,
    "9":8,
    "T":9,
    "J":10,
    "Q":11,
    "K":12,
    "A":13
}

for i in range(len(five) - 1):
    for j in range(len(five) - i - 1):
        for k in range(5):
            if cardToRank[five[j][0][k]]<cardToRank[five[j+1][0][k]]:
                five[j],five[j+1]=five[j+1],five[j]
                break
            if cardToRank[five[j][0][k]]>cardToRank[five[j+1][0][k]]:
                break
for i in range(len(four) - 1):
    for j in range(len(four) - i - 1):
        for k in range(5):
            if cardToRank[four[j][0][k]]<cardToRank[four[j+1][0][k]]:
                four[j],four[j+1]=four[j+1],four[j]
                break
            if cardToRank[four[j][0][k]]>cardToRank[four[j+1][0][k]]:
                break
for i in range(len(full) - 1):
    for j in range(len(full) - i - 1):
        for k in range(5):
            if cardToRank[full[j][0][k]]<cardToRank[full[j+1][0][k]]:
                full[j],full[j+1]=full[j+1],full[j]
                break
            if cardToRank[full[j][0][k]]>cardToRank[full[j+1][0][k]]:
                break

for i in range(len(three) - 1):
    for j in range(len(three) - i - 1):
        for k in range(5):
            if cardToRank[three[j][0][k]]<cardToRank[three[j+1][0][k]]:
                three[j],three[j+1]=three[j+1],three[j]
                break
            if cardToRank[three[j][0][k]]>cardToRank[three[j+1][0][k]]:
                break
for i in range(len(tp) - 1):
    for j in range(len(tp) - i - 1):
        for k in range(5):
            if cardToRank[tp[j][0][k]]<cardToRank[tp[j+1][0][k]]:
                tp[j],tp[j+1]=tp[j+1],tp[j]
                break
            if cardToRank[tp[j][0][k]]>cardToRank[tp[j+1][0][k]]:
                break
for i in range(len(op) - 1):
    for j in range(len(op) - i - 1):
        for k in range(5):
            if cardToRank[op[j][0][k]]<cardToRank[op[j+1][0][k]]:
                op[j],op[j+1]=op[j+1],op[j]
                break
            if cardToRank[op[j][0][k]]>cardToRank[op[j+1][0][k]]:
                break
for i in range(len(hc) - 1):
    for j in range(len(hc) - i - 1):
        for k in range(5):
            if cardToRank[hc[j][0][k]]<cardToRank[hc[j+1][0][k]]:
                hc[j],hc[j+1]=hc[j+1],hc[j]
                break
            if cardToRank[hc[j][0][k]]>cardToRank[hc[j+1][0][k]]:
                break
            





output=0


for i in range(len(hc)-1,-1,-1):
    ranks.append(int(hc[i][1]))

for i in range(len(op)-1,-1,-1):
    ranks.append(int(op[i][1]))

for i in range(len(tp)-1,-1,-1):
    ranks.append(int(tp[i][1]))

for i in range(len(three)-1,-1,-1):
    ranks.append(int(three[i][1]))

for i in range(len(full)-1,-1,-1):
    ranks.append(int(full[i][1]))

for i in range(len(four)-1,-1,-1):
    ranks.append(int(four[i][1]))

for i in range(len(five)-1,-1,-1):
    ranks.append(int(five[i][1]))


for i in range(len(ranks)):
    output+=ranks[i]*(i+1)

print(output)
print(p2)