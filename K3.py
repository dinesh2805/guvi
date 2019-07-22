t3,t4=map(int,input().split())
li=list(map(int,input().split()))
if t4==1:
  print(min(li))
elif t4==2:
  print(max(li[0],li[t3-1]))
else:
  print(max(li))
