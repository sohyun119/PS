n = int(input())

q=1

for _ in range(n):
    stack=[]
    index = 0
    c=input()
    while 1:
        if c[index]=='(':
            stack.append(c)
        elif c[index] ==')':
            if not stack :
                q=-1
                break
            else :
                stack.pop()

        index += 1
        if index>=len(c) :
            break
        print(stack)
    
    if stack:
        q=-1
    if q==1 : print('YES')
    else : print('NO')
    






