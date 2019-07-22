import sys
n1n = int(input())
ds = []
if n1n == 2:
    print('3')
    print('2 1 2')
    sys.exit()
if n1n == 3:
    print('4')
    print('2 1 3 2')
    sys.exit()
k = n1n//2
for i in range(2, n1n+1, 2):
    ds.append(i)

for i in range(1, n1n, 2):
    ds.append(i)

for i in range(2, n1n+1, 2):
    ds.append(i)
print(len(ds))
print(*ds)
