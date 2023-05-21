n=int(input())
c=list(map(int,input().split()))
s=""
for i in c:
    i=str(i)
    s=s+i
s=int(s)+1
s=str(s)
for i in s:
    print(i,end=" ")