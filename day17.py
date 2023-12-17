from heapq import heappush, heappop
grid=[list(map(int,line.strip())) for line in open("day17input.txt")]

seen=set()
pq=[(0,0,0,0,0,0)]

while pq:
    hl,r,c,dr,dc,n=heappop(pq)
    if r==len(grid)-1 and c==len(grid[0])-1 and n>=4:
        print(hl)
        break
    
    if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
        continue
    if (r,c,dr,dc,n) in seen:
        continue
    seen.add((r,c,dr,dc,n))

    if n<10 and (dr,dc)!=(0,0):
        nr=r+dr
        nc=c+dc
        if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]):
            heappush(pq,(hl+grid[nr][nc],nr,nc,dr,dc,n+1))
    if n>=4 or (dr,dc)==(0,0):
        for ndr,ndc in [(0,1),(1,0),(-1,0),(0,-1)]:
            if (ndr,ndc)!=(dr,dc) and (ndr,ndc)!=(-dr,-dc):
                nr=r+ndr
                nc=c+ndc
                if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]):
                    heappush(pq,(hl+grid[nr][nc],nr,nc,ndr,ndc,1))