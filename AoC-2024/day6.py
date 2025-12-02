import re

def iteratemap(map, guardpos):
    match map[guardpos[1]][guardpos[0]]:
        case '^':
            if(guardpos[1] == 0):
                return (map, True, guardpos)
            elif(map[guardpos[1]-1][guardpos[0]]  == '#'):
               map[guardpos[1]][guardpos[0]] = '>'
            else:
                map[guardpos[1]][guardpos[0]] = 'X'
                map[guardpos[1]-1][guardpos[0]] = '^'
                guardpos[1] -= 1

        case '>':
            if(guardpos[0] == len(map[0])-1):
                return (map, True, guardpos)
            elif(map[guardpos[1]][guardpos[0]+1]  == '#'):
               map[guardpos[1]][guardpos[0]] = 'v'
            else:
                map[guardpos[1]][guardpos[0]] = 'X'
                map[guardpos[1]][guardpos[0]+1] = '>'
                guardpos[0] += 1

        case 'v':
            if(guardpos[1] == len(map)-1):
                return (map, True, guardpos)
            elif(map[guardpos[1]+1][guardpos[0]]  == '#'):
               map[guardpos[1]][guardpos[0]] = '<'
            else:
                map[guardpos[1]][guardpos[0]] = 'X'
                map[guardpos[1]+1][guardpos[0]] = 'v'
                guardpos[1] += 1

        case '<':
            if(guardpos[0] == 0):
                return (map, True, guardpos)
            elif(map[guardpos[1]][guardpos[0]-1]  == '#'):
               map[guardpos[1]][guardpos[0]] = '^'
            else:
                map[guardpos[1]][guardpos[0]] = 'X'
                map[guardpos[1]][guardpos[0]-1] = '<'
                guardpos[0] -= 1
        
    return (map, False, guardpos)

def find_guard(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(re.match("[\^\>v\<]", map[y][x]) != None):
                return [x, y]
            
    return None

def count_visited(map):
    visited = 0
    for line in map:
        visited += len(re.findall("X", "".join(line)))

    if(find_guard(map) != None):
        visited += 1

    return visited


def part1(input):
    map = [list(line) for line in input.split("\n")[:-1]]

    guardpos = find_guard(map)
    while(True):
        (map, isComplete, guardpos) = iteratemap(map, guardpos)
        if(isComplete):
            break
    
    result = count_visited(map)

    print(result)

def causes_loop(map, guardpos, obstruction):
    past_positions = [(guardpos.copy(), map[guardpos[1]][guardpos[0]])]
    guardpos = guardpos.copy()
    map[obstruction[1]][obstruction[0]] = "#"
    isloop = False
    (map, isComplete, guardpos) = iteratemap(map, guardpos)
    while(not isComplete):
        if((guardpos, map[guardpos[1]][guardpos[0]]) in past_positions):
            #print(past_positions)
            #print(guardpos, map[guardpos[1]][guardpos[0]])
            #print("\n".join(["".join(line) for line in map]))
            
            isloop = True
            break
        past_positions.append((guardpos.copy(), map[guardpos[1]][guardpos[0]]))

        (map, isComplete, guardpos) = iteratemap(map, guardpos)
        
    return isloop
    

def part2(input):
    map = [list(line) for line in input.split("\n")[:-1]]

    guardpos = find_guard(map)

    possible_positions = 0

    map_copy = [[elem for elem in line] for line in map]
    guardpos_copy = guardpos.copy()

    while(True):
        (map_copy, isComplete, guardpos_copy) = iteratemap(map_copy, guardpos_copy)
        if(isComplete):
            break

    standard_path_positions = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map_copy[y][x] != "." and map_copy[y][x] != "#"):
                standard_path_positions.append((x, y))

    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == '.' and (x, y) in standard_path_positions):
                new_map = [[elem for elem in line] for line in map]
                if(causes_loop(new_map, guardpos, [x, y])):
                    possible_positions += 1
                    print(f"Found loop in test {x+y*(len(map[0]))}/{len(map[0])*len(map)}")
    
    print(possible_positions)


part1(open("input6.txt", "r").read())
part2(open("input6.txt", "r").read())