# 2021.05.01 - 다시 푼 날짜 : 2021.07.06
# 1-1 탐색과 정렬 . 1920번 [수 찾기]
# 다시풀어서 맞춤 : b는 sort를 하지 않는게 관건?

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

i=0
while(i<m):
    count = 0
    rigth = n-1
    left = 0
    while(1):
        mid = (rigth + left) //2 
        if b[i] == a[mid] or b[i] == a[rigth] or b[i] == a[left]:
            count = 1
            i+=1
            break
        elif b[i] < a[mid]:
            rigth = mid
        elif b[i] > a[mid]:
            left = mid
        if rigth-left<=1:
            i+=1
            break
    print(count)


#if error!=0:
    #error=1
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# # 나중에 다시 풀기
# # 아래코드는 시간초과 에러 코드임
# a.sort()
# b.sort()
# count = 0
# left = 0
# right = n
# mid = (n-1)/2
# for i in range(len(b)):
#     for j in range(len(a)):
#         if b[i]> a[mid]:
#             left = mid
#             mid = (right - left)/2
#         elif b[i] < a[mid]:
#             right = mid
#             mid = (right - left)/2
#         if b[i]==a[mid] or b[i]==a[left] or b[i]==a[right]:
#             count=1
#             break
#         if left>right:
#             count = -1
#             break
#     if count==1:
#         print(1)
#     else :
#         print(0)






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

