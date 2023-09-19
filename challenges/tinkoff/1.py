n, s = map(int, input().split())
a = map(int, input().split())

target = 0

for price in a:
    if s - price >= 0 and target < price:
        target = price
print(target)
