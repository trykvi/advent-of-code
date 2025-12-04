dirs = [(-1, -1),(0, -1),(1, -1),(1, 0),(1, 1),(0, 1),(-1, 1),(-1, 0)]

def addTuples(a, b):
    return (a[0]+b[0], a[1]+b[1])

def inBounds(x, y, map):
    if((x >= 0 and x < len(map[0])) and (y >= 0 and y < len(map))):
        return True
    else:
        return False

def countAdjacent(x, y, paper_map):
    count = 0
    for dir in dirs:
        adj_pos = addTuples(dir, (x, y))
        if(inBounds(adj_pos[0], adj_pos[1], paper_map) and paper_map[adj_pos[1]][adj_pos[0]] == '@'):
            count += 1

    return count
    

def part1(input):
    paper_map = [list(line) for line in input.split("\n")]

    accessible_rolls = 0

    for y in range(len(paper_map)):
        for x in range(len(paper_map[y])):
            if(paper_map[y][x] == '@' and countAdjacent(x, y, paper_map) < 4):
                accessible_rolls += 1

    return accessible_rolls

def part2(input):
    paper_map = [list(line) for line in input.split("\n")]

    total_removed_rolls = 0
    removed_rolls = 1

    while(removed_rolls != 0):
        removed_rolls = 0
        rolls_to_remove = []
        for y in range(len(paper_map)):
            for x in range(len(paper_map[y])):
                if(paper_map[y][x] == '@' and countAdjacent(x, y, paper_map) < 4):
                    #result_map[y][x] = 'x'
                    total_removed_rolls += 1
                    removed_rolls += 1
                    rolls_to_remove.append((x, y))

        for x, y in rolls_to_remove:
            paper_map[y][x] = '.'

    return total_removed_rolls


input = open("./AoC-2025/input4.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))
