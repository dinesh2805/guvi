nb,kb=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
	if i + kb <=5:
		c+=1
print(c//3)
