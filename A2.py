sd=input()
b=""
l=[]
a=0
for i in range(0,len(sd)):
  for j in range(i,len(sd)):
    b=b+sd[j]
    if(b[::-1]==b):
      a=len(sd)-len(b)
      l.append(a)
  b=""
print(min(l))
