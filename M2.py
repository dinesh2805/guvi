ktr1j=input()
for vt in range(len(ktr1j)):
  if(ktr1j[vt] < ktr1j[vt+1]):
    print(ktr1j[vt+1:])
    break
