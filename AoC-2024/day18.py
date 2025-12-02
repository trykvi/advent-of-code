import heapq

def find_element(e, map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == e):
                return (x, y)
            
    return (-1, -1)

def add_tuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

d_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def is_in_bounds(pos, map):
    if(pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(map[0]) and pos[1] < len(map)):
        return True

    return False


def BFS(map, startpos, endpos):
    visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    visited[startpos[1]][startpos[0]] = True

    nodes_to_search = [startpos]

    iteration = 0

    while(len(nodes_to_search) > 0 and endpos not in nodes_to_search):
        new_nodes_to_search = []
        #print(nodes_to_search)
        for node in nodes_to_search:
            for d in d_list:
                new_pos = add_tuples(d, node)
                if(not is_in_bounds(new_pos, map)):
                    continue
                x = new_pos[0]
                y = new_pos[1]
                if(map[y][x] != '#' and not visited[y][x]):
                    visited[y][x] = True
                    new_nodes_to_search.append(new_pos)
        
        iteration += 1
        
        nodes_to_search = new_nodes_to_search

    if(endpos in nodes_to_search):
        return iteration
    else:
        return -1

def print_map(map):
    print("\n".join("".join(line) for line in map))

def part1(input):
    n = 1024
    width = 71
    height = 71
    falling_bits = [tuple(int(e) for e in line.split(',')) for line in input.split("\n")[:n]]
    map = [['.' for _ in range(width)] for _ in range(height)]
    for bit in falling_bits:
        map[bit[1]][bit[0]] = '#'


    #print_map(map)
    return BFS(map, (0,0), (width-1, height-1))

def part2(input):
    width = 71
    height = 71
    falling_bits = [tuple(int(e) for e in line.split(',')) for line in input.split("\n")[:-1]]
    map = [['.' for _ in range(width)] for _ in range(height)]
    for bit in falling_bits:
        map[bit[1]][bit[0]] = '#'
        if(BFS(map, (0,0), (width-1, height-1)) == -1):
            #print_map(map)
            return bit



    


print(part1(open("input18.txt", "r").read()))
print(part2(open("input18.txt", "r").read()))