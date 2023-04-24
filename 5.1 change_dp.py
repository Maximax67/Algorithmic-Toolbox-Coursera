def change(money):
    coins = [1, 3, 4]
    minNumCoins = [float("inf")] * (money + 1)
    minNumCoins[0] = 0
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                numCoins = minNumCoins[m - coin] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins

    return minNumCoins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
