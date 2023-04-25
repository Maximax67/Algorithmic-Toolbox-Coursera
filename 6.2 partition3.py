def search_partition(values, index, partitions, W):
    if index >= len(values):
        return 1
    
    for i in range(len(partitions)):
        if partitions[i] + values[index] <= W:
            partitions[i] += values[index]
            
            if search_partition(values, index + 1, partitions, W):
                return 1
            
            partitions[i] -= values[index]
    
    return 0


def partition3(values):
    W = sum(values)
    if len(values) < 3 or W % 3 != 0 or max(*values) > W / 3:
        return 0
    
    values.sort(reverse = True)
    partitions = [0] * 3
    return search_partition(values, 0, partitions, W / 3)


if __name__ == '__main__':
    n = int(input())
    values = [int(x) for x in input().split()]
    assert n == len(values)
    values.sort()
    print(partition3(values))
