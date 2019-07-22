ypp,yqq=input().split()
ypp=int(ypp)
yqq=int(yqq)
s3=''
u3=2
if(ypp+yqq<=3):
    for i in range(0,ypp+yqq):
        if(i%2!=0):
            s3=s3+'0'
        else:
            s3=s3+'1'
else:    
    for i in range(0,ypp+yqq):
        if(i==u3):
            s3=s3+'0'
            if(u3==yqq):
                u3=u3+2
            else:
                u3=u3+3
        else:
            s3=s3+'1'
x=len(s3)-1
if(int(s3[x])==0):
    print('-1') 
elif ypp==1 and yqq==2: 
     print("011")
else:
    print(s3)
