def min_refills(distance, tank, stops):
    refils = 0
    current_distance = 0
    last_distance = 0
    stops_index = 0
    stops_n = len(stops)
    
    while distance > current_distance + tank:
        while (stops_index < stops_n and stops[stops_index] <= tank + current_distance):
            stops_index += 1
        stops_index -= 1
        current_distance = stops[stops_index]
        if last_distance == current_distance:
            return -1
        refils += 1
        last_distance = current_distance
    
    return refils


if __name__ == '__main__':
    distance = int(input())
    tank = int(input())
    _ = input()
    stops = [int(i) for i in input().split()]
    stops.sort()
    print(min_refills(distance, tank, stops))
