def optimal_value(capacity, loot):
    if (capacity <= 0):
        return 0
    
    value = 0.
    index = 0
    length = len(loot)
    
    while capacity > 0 and index < length:
        if loot[index][1] <= capacity:
            value += loot[index][0]
            capacity -= loot[index][1]
            index += 1
        else:
            value += loot[index][0] * capacity / loot[index][1]
            capacity = 0

    return value


if __name__ == "__main__":
    n, W = [int(i) for i in input().split()]
    loot = []
    
    for i in range(n):
        values, capacity = [int(i) for i in input().split()]
        if values >= 0 and capacity >= 0:
            loot.append((values, capacity))
    
    loot.sort(key = lambda x: x[0] / x[1], reverse = True)
    opt_value = optimal_value(W, loot)
    print("{:.10f}".format(opt_value))
