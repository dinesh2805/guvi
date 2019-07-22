p=[]
for i in range(4):
	d1,d2=input().split()
	p.append(int(d1))
	p.append(int(d2))
if len(set(p))>2:
	print("no")
else:
	print("yes")
