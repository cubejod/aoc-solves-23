with open("day12input.txt") as f:
    data=f.readlines()
    data = [l.rstrip() for l in data]
cache={}
def solve(springs,groups):
    if springs=="":
        if groups!=():
            return 0
        else:
            return 1
    if groups==():
        if "#" in springs:
            return 0
        else:
            return 1
    if (springs,groups) in cache:
        return cache[(springs,groups)]
    result=0
    if springs[0] in ".?":
        result+=solve(springs[1:],groups)
    if springs[0] in "#?":
        if groups[0]<=len(springs) and "." not in springs[0:groups[0]] and (groups[0]==len(springs) or springs[groups[0]]!="#"):
            result+=solve(springs[groups[0]+1:],groups[1:])
    cache[(springs,groups)]=result
    return result

output=0
output2=0
for i in range(len(data)):
    springs,groups=data[i].split()
    springs2="?".join([springs]*5)
    groups=tuple(map(int,groups.split(",")))
    groups2=groups
    groups2*=5
    output+=solve(springs,groups)
    output2+=solve(springs2,groups2)
print(output)
print(output2)