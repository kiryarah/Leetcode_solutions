n = int(input())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
k = int(input())
s = list(map(int, input().split()))

s_dict = {c[i]: r[i] for i in range(n)}

total = sum(1 for i in range(1, k) if s_dict.get(s[i]) != s_dict.get(s[i - 1]))

print(total)
