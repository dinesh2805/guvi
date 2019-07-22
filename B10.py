bbb,s=map(str,input().split("|"))
c=input()
if  len(bbb)>len(s):
    if len(bbb)==len(s)+len(c):
        print(bbb+"|"+s+c)
elif len(bbb)<len(s):
     if len(s)==len(bbb)+len(c):
        print(bbb+c+"|"+s)
elif len(bbb)==len(s) and len(c)>1 or (len(s) or len(bbb)):
    print("impossible")
