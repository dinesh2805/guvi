ss=input()
r=input()
b=[]
for i in range(len(ss)):
  d=ord(ss[i])-96
  c=ord(r[i])+d
  if(c>122):
    c=c-122
    c=c+96
  b.append(chr(c))
for i in b:
  print(i,end="")
