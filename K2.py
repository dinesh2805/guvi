def mr(lh, nh, kh):
    if kh == 1:
        return min(lh)
    if kh == 2:
        return max(lh[0], lh[nh - 1])
    return max(lh)


nh, kh = input().split()
n,k = int(nh), int(kh)
l = [int(x) for x in input().split()]
n = len(l)
ans = mr(l, n, k)
print(ans)
