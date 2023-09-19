def is_win_hand(a: list, b: list, n: int) -> str:
    i, j = 0, n - 1

    while (a[i] <= b[i] or a[j] >= b[j]) and i <= j:
        if a[i] < b[i] or b[j] < a[j]:
            return 'NO'

        if a[i] == b[i]:
            i += 1

        if a[j] == b[j]:
            j -= 1

    if i > j:
        return 'YES'

    return 'YES' if sorted(a[i: j + 1]) == b[i: j + 1] else 'NO'



n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(is_win_hand(a, b, n))

