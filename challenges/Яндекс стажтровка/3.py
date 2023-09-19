def maxProfit(prices, n):
    if n < 2:
        return []

    profit = [0] * n
    min_left = prices[0]

    for i in range(1, n):
        min_left = min(min_left, prices[i])
        profit[i] = max(profit[i - 1], prices[i] - min_left)

    max_right = prices[n - 1]
    max_profit = 0

    for i in range(n - 2, -1, -1):
        max_right = max(max_right, prices[i])
        profit[i] += max(max_profit, max_right - prices[i])
        max_profit = max(max_profit, max_right - prices[i])

    def get_max_profit(seq):
        left = min_index = 0
        right = max_index = 1
        max_profit = 0

        while right < len(seq):
            currentProfit = seq[right] - seq[left]
            if seq[left] < seq[right]:
                if max_profit < currentProfit:
                    max_profit = currentProfit
                    min_index = left
                    max_index = right
            else:
                left = right
            right += 1

        return min_index + 1, max_index + 1

    if profit[0] == 0:
        return []

    mid_index = profit.index(max(profit))
    res = []

    if not mid_index:
        res.append(get_max_profit(prices))
        return res

    res.append(get_max_profit(prices[:mid_index + 1]))
    min2, max2 = get_max_profit(prices[mid_index + 1:])
    res.append((min2 + mid_index + 1, max2 + mid_index + 1))
    return res


n = int(input())
p = list(map(int, input().split()))
res = maxProfit(p, n)

if len(res) == 0:
    print(0)
else:
    print(len(res))
    for item in res:
        print(*item)


# 1 9 2 7 3 5 1 9
# 1 9 2 10 3 5 1 9
# 1 9 2 10 1 5 3 9
# 1 9 2 10 3 5 3 9
# 1 7 1 7 1 7 1 7

