tiy,sy = map(int,input().split())
v = list(map(int,input().split()))
b,n = 0,[]
for i in range(0,len(v)):
  tiy = i
  for p in range(0,len(v)):
    for l in range(0,sy):
      if l == sy-1:
        try:
          b += v[p+i]
        except IndexError:
            tiy = ti-1
            b +=v[tiy]
      else:
        b += v[i]
    n.append(b)
    b = 0
for i in range(0,len(v),sy):
  b = sum(v[i:i+sy])
  n.append(b)
print(*sorted(set(n)))
