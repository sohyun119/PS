import heapq
n = int(input())

hq=[]
for _ in range(n):
    heapq.heappush(hq,int(input()))

total=0
if n!=1:
    while hq:
        if len(hq) == 1 :
            break
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        heapq.heappush(hq,a+b)
        total+=a+b

print(total)

