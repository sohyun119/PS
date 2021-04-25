n, m = map(int, input().split())

m1 = 0
result=0
for i in range(0,m):
    a, b = map(int, input().split())
    if n/6*a+(n%6*b) > (b*n):
        m1 = b*n
    elif n/6*a+(n%6*b) <= (b*n) :
        m1 = a
    if i==0 :
        result = m1
    if result > m1 :
        result = m1
    
print(result)
