Ah,Bh=map(int,input().split())
if Ah%10==0:
  Ah=str(Ah)
  C=0
  for X in range(len(Ah)-1,-1,-1):
    if Ah[X]=='0':
      C+=1
  if Bh<=C:
    print(Ah)
  else:
    Ah=Ah[:-C]
    Ah=Ah+'0'*Bh
    print(Ah)
elif 10%(Ah%10)==0:
  no=int('1'+'0'*Bh)
  while True:
    if no%Ah==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*Bh)
else:
  print(str(Ah)+Bh*'0')
