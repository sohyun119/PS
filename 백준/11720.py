n=int(input())

a=int(input())
b=0
for i in range(0, n):
    b+=(a%10**(i+1)-(a%10**i))/(10**(i))
print(int(b))
