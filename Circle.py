n=int(input())
i=10
b=0
c=0
while i <=n:
    b = b + 1
    c=c+1
    if b%2 == 0:
        i=i+10
    else:
        i=i+20
print(c)