def get_count_words(s: str) -> int:
    if len(s) < 7:
        return 0

    shef_dict = {sym: 0 for sym in 'sherif'}

    for sym in s:
        if sym in shef_dict:
            shef_dict[sym] += 1
    shef_dict['f'] //= 2

    return min(shef_dict.values())


s = input()
print(get_count_words(s))
