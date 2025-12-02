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

def find_combos(nodes, max_cheat):
    combos = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            x1,y1 = nodes[i]
            x2,y2 = nodes[j]
            cheat_size = abs(x1-x2) + abs(y1-y2)
            if(cheat_size <= max_cheat):
                combos.append((nodes[i], nodes[j], cheat_size))

    return combos

def BFS_lengths_from_end(map, startpos, endpos):
    visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    visited[startpos[1]][startpos[0]] = True

    nodes_to_search = [startpos]

    length_to_end = BFS(map, startpos, endpos)

    lengths_from_end = {}

    lengths_from_end[endpos] = 0

    iteration = 0

    while(len(nodes_to_search) > 0 and endpos not in nodes_to_search):
        new_nodes_to_search = []
        #print(nodes_to_search)
        for node in nodes_to_search:
            lengths_from_end[node] = length_to_end
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
        length_to_end -= 1
        
        nodes_to_search = new_nodes_to_search

    return lengths_from_end

def part1(input):
    racetrack = [list(line) for line in input.split("\n")[:-1]]
    startpos = find_element('S', racetrack)
    endpos = find_element('E', racetrack)

    base_time = BFS(racetrack, startpos, endpos)
    lengths_from_end = BFS_lengths_from_end(racetrack, startpos, endpos)
    path_combos = find_combos(list(lengths_from_end.keys()), 2)

    good_cheats = 0

    print("num path combos:", len(path_combos), "base time:", base_time)
    for combo in path_combos:
        diff = abs(lengths_from_end[combo[0]] - lengths_from_end[combo[1]])
        if(diff - combo[2] >= 100):

            good_cheats += 1

    return good_cheats

def part2(input):
    racetrack = [list(line) for line in input.split("\n")[:-1]]
    startpos = find_element('S', racetrack)
    endpos = find_element('E', racetrack)

    base_time = BFS(racetrack, startpos, endpos)
    lengths_from_end = BFS_lengths_from_end(racetrack, startpos, endpos)
    path_combos = find_combos(list(lengths_from_end.keys()), 20)

    good_cheats = 0

    print("num path combos:", len(path_combos), "base time:", base_time)
    for combo in path_combos:
        diff = abs(lengths_from_end[combo[0]] - lengths_from_end[combo[1]])
        if(diff - combo[2] >= 100):

            good_cheats += 1

    return good_cheats


print(part1(open("input20.txt", "r").read()))
print(part2(open("input20.txt", "r").read()))