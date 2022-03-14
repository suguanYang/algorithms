val = {
    1: 1,
    2: 10,
    3: 13,
    4: 18,
    5: 20,
    6: 31,
    7: 32
}
count = 0
def rod_cutting(n):
    dp = []
    for _ in range(n + 1):
        dp.append(0)

    for l in range(1, n + 1):
        max = 0
        for i in range(1, l + 1):
            value = val[i] if (val.get(i) != None) else 0
            cur_val = value + dp[l - i]
            if max < cur_val:
                max = cur_val
        dp[l] = max

    return dp[n]

print(rod_cutting(10000))
print(count)
