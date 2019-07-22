Kk1 = int(input())
while Kk1%10==0:
    Kk1=Kk1//10
Kk1=str(Kk1)
N1=Kk1[::-1]
if Kk1==N1:
    print('yes')
else:
    print('no')
