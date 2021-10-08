# # 2021.04.28 - 2750번 <수 정렬하기> - 탐색과 정렬

import heapq #heapq 사용시에 import필수 

n = int(input())
hq = []
for _ in range(n) : 
    a = int(input())
    heapq.heappush(hq,a)

for i in range(n):
    b = heapq.heappop(hq)
    print(b)
    
# 반대로 정렬해서 다시 하기 - stack?
