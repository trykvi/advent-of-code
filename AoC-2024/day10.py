def set_count_trails_starting_from(point, map):
    currentVal = int(map[point[1]][point[0]])
    result = set()
    #print(point, len(map), currentVal)
    if currentVal == 9:
        result.add(point)
    else:
        if point[1] > 0 and int(map[point[1]-1][point[0]]) == currentVal + 1:
            result.update(set_count_trails_starting_from((point[0], point[1]-1), map))
        if point[0] < len(map[0])-1 and int(map[point[1]][point[0]+1]) == currentVal + 1:
            result.update(set_count_trails_starting_from((point[0]+1, point[1]), map))
        if point[1] < len(map)-1 and int(map[point[1]+1][point[0]]) == currentVal + 1:
            result.update(set_count_trails_starting_from((point[0], point[1]+1), map))
        if point[0] > 0 and int(map[point[1]][point[0]-1]) == currentVal + 1:
            result.update(set_count_trails_starting_from((point[0]-1, point[1]), map))

    #print(result)

    return result

def count_trails_starting_from(point, map):
    currentVal = int(map[point[1]][point[0]])
    result = 0
    #print(point, len(map), currentVal)
    if currentVal == 9:
        result += 1
    else:
        if point[1] > 0 and int(map[point[1]-1][point[0]]) == currentVal + 1:
            result += count_trails_starting_from((point[0], point[1]-1), map)
        if point[0] < len(map[0])-1 and int(map[point[1]][point[0]+1]) == currentVal + 1:
            result += count_trails_starting_from((point[0]+1, point[1]), map)
        if point[1] < len(map)-1 and int(map[point[1]+1][point[0]]) == currentVal + 1:
            result += count_trails_starting_from((point[0], point[1]+1), map)
        if point[0] > 0 and int(map[point[1]][point[0]-1]) == currentVal + 1:
            result +=count_trails_starting_from((point[0]-1, point[1]), map)

    #print(result)

    return result

def find_trailheads(map):
    trailheads = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '0':
                trailheads.append((x, y))

    return trailheads

def part1(input):
    map = [list(line) for line in input.split("\n")[:-1]]
    trailheads = find_trailheads(map)
    total_score = 0
    for trailhead in trailheads:
        #print(trailhead)
        total_score += len(set_count_trails_starting_from(trailhead, map))

    return total_score

def part2(input):
    map = [list(line) for line in input.split("\n")[:-1]]
    trailheads = find_trailheads(map)
    total_score = 0
    for trailhead in trailheads:
        #print(trailhead)
        total_score += count_trails_starting_from(trailhead, map)      

    return total_score



print(part1(open("input10.txt", "r").read()))
print(part2(open("input10.txt", "r").read()))

