# 2021.05.01 -다시 시간초과 error
# 1-1 탐색과 정렬 . 1920번 [수 찾기]

if error!=0:
    error=1
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
# 나중에 다시 풀기
a.sort()
b.sort()
count = 0
left = 0
right = n
mid = (n-1)/2
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]> a[mid]:
            left = mid
            mid = (right - left)/2
        elif b[i] < a[mid]:
            right = mid
            mid = (right - left)/2
        if b[i]==a[mid] or b[i]==a[left] or b[i]==a[right]:
            count=1
            break
        if left>right:
            count = -1
            break
    if count==1:
        print(1)
    else :
        print(0)






# 아래는 타임초과 에러 코드
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# for i in range(m) : 
#     count = -1
#     for j in range(n) :
#         if b[i] == a[j] :
#             count = 1
#             break
#     if count<0 :
#         print(0)
#     else :
#         print(1)

