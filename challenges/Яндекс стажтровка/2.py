n, x, t = map(int, input().split())
a = tuple(map(int, input().split()))

res = []
mid = []

for i in range(n):
    cur = abs(a[i] - x)
    if cur == 0:
        res.append(i + 1)
        continue

    if cur < t:
        mid.append((cur, i + 1))

mid.sort(key=lambda x: x[0])

count = i = 0

while i < len(mid) and count + mid[i][0] <= t:
    res.append(mid[i][1])
    count += mid[i][0]
    i += 1

res.sort()

print(len(res))
print(*res)
