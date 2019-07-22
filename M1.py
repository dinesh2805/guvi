nn1r,mm1r=map(int,input().split())
l=[]
for _ in range(nn1r):
	l.append(sorted(list(map(int,input().split()))))
for i in range(nn1r-1):
	for j in range(mm1r):
		for k in range(nn1r-i):
			if(l[i][j]>l[i+k][j]):
				l[i][j],l[i+k][j]=l[i+k][j],l[i][j]
for i in l:
	print(*i,sep=' ')
