st1,st2=map(str,input().split())
s=0
for i in range(0,len(st1)):
    for j in range(0,len(st2)):
        if st1[i]==st2[j]:
            s+=1
if s>=2:
    print("yes")
else:
    print("no")
