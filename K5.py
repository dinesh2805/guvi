tyi3,tyi4,tyi5,tyi6=map(int,input().split())
li3=list(map(int,input().split()))
xi3=[]
for i in range(0,len(li3)):
    for j in range(i,len(li3)):
        for k in range(j,len(li3)):
            xi3.append(tyi4*li3[i]+tyi5*li3[j]+tyi6*li3[k])
print(max(xi3))
