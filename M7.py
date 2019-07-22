import sys
nn=int(input())
l=list(map(int,input().split()))
s=0
if nn==1:
    print(1)
    sys.exit()
for i in range(1,nn-1):
    if (l[i]<l[i-1] and l[i]<l[i+1]) or (l[i]>l[i-1] and l[i]>l[i+1]): s=s+1
print(s)
