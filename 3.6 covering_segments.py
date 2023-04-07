def optimal_points(segments):
    n = len(segments)
    index = 0
    points = []
    
    while index < n:
        last_point = segments[index][1]
        while index < n - 1 and last_point >= segments[index + 1][0]:
            index += 1
        points.append(last_point)
        index += 1
    
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        segments.append([int(x) for x in input().split()])
    
    segments.sort(key = lambda x: x[1])
    
    points = optimal_points(segments)
    print(len(points))
    print(*points)
