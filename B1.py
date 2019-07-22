Niy1=int(input())
Li=list(map(int,input().split()))
Ni2=[]
Ni3=1
for X in range(Niy1):
  V=Li[X:]
  ans=len(V)
  for Y in range(ans-1):
    if V[Y]>0 and V[Y+1]<0:
      Ni3=Ni3+1
    elif V[Y]<0 and V[Y+1]>0:
      Ni3=Ni3+1
    else:
      break
  Ni2.append(str(Ni3))
  Ni3=1
print(" ".join(Ni2))
