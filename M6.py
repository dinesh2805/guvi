Ppt = int(input())
Qt = [ int(i) for i in input().split()]
Ppt = len(Qt)
Ut = 0
for Xt in range(0,Ppt-2):
    for Yt in range(Xt+1, Ppt-1):
        for Zt in range(Yt+1, Ppt):
            if Qt[Xt] > Qt[Yt] > Qt[Zt] :
                Ut =Ut+ 1
print(Ut)
