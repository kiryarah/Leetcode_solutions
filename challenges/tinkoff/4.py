def get_coins(coins: list, n: int) -> int | list:
    i, j = 0, len(coins) - 1
    summ = sum(coins)

    while summ > n:
        if summ - coins[j] < n:
            summ -= coins[i]
            i += 1
        else:
            summ -= coins[j]
            j -= 1

    if summ == n:
        return coins[i: j + 1]
    return -1


n, m = map(int, input().split())

denom = []
for coin in input().split():
    denom.extend([int(coin)] * 2)

result = get_coins(denom, n)

if isinstance(result, list):
    print(len(result))
    print(*result)
else:
    print(result)
