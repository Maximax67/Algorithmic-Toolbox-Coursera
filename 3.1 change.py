def change(money):
    if (money <= 0):
        return 0

    counter = money // 10
    money = money - counter * 10
    if money > 5:
        counter += 1
        money -= 5

    return money + counter


if __name__ == '__main__':
    m = int(input())
    print(change(m))
