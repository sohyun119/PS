# 1-1 탐색과 정렬 : 2751번 수정렬하기 2
# 2750번과 같은 문제이지만 훨씬 큰 수를 다뤄야 하므로 더 빨리 실행되는 코드 짜야함 

n = int(input())

a = []
for i in range(n):
    num = int(input())
    count = 0
    for j in range(i+1):
        if a[j]>n:
            count+=1
    for k in range(count):
        #다시 하기 