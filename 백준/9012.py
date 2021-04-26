n = int(input())

for _ in range(n):
    q=1
    stack=[]
    c = input()
    for i in c :
        if i=='(':
            stack.append(i)
        else :
            if not stack:
                q=-1
            else :
                stack.pop()
    if stack :
        q=-1
    if q==1:
        print("YES")
    else :
        print("NO")


# ------- 아래는 처음 풀었던 틀린 풀이 --------(위는 맞음)
# n = int(input())

# q=1

# for _ in range(n):
#     stack=[]
#     index = 0
#     c=input()
#     while 1:
#         if c[index]=='(':
#             stack.append(c)
#         elif c[index] ==')':
#             if not stack :
#                 q=-1
#                 break
#             else :
#                 stack.pop()

#         index += 1
#         if index>=len(c) :
#             break
#         print(stack)
    
#     if stack:
#         q=-1
#     if q==1 : print('YES')
#     else : print('NO')
    






