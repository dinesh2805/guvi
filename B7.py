import sys,string, math, itertools
nu,k = input().split()
nu,k = int(nu),int(k)
L = [ int(x) for x in input().split()]
for i in range(0,nu) :
    if (86400-L[i]) >= k :
        print(i+1)
        sys.exit()
    k -= (86400-L[i])
