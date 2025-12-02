moves = {'^': (0, -1), '>':(1, 0), 'v':(0, 1), '<':(-1, 0)}

def add_tuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def perform_move(move, map, robot_pos):
    d = moves[move]

    pos = (robot_pos[0], robot_pos[1])
    while(True):
        #print(pos)
        pos = add_tuples(pos, d)
        if(map[pos[1]][pos[0]] == '.'):
            map[pos[1]][pos[0]] = 'O'
            map[robot_pos[1]][robot_pos[0]] = '.'
            new_robot_pos = add_tuples(robot_pos, d)
            map[new_robot_pos[1]][new_robot_pos[0]] = '@'
            return new_robot_pos
        elif(map[pos[1]][pos[0]] == '#'):
            break

    return robot_pos


def find_robot(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == '@'):
                return (x, y)
            
    return (-1, -1)

def print_map(map):
    print("\n".join("".join(line) for line in map))


def part1(input):
    raw_map, raw_moves = input.split("\n\n")

    map = [list(line) for line in raw_map.split("\n")]
    moves = raw_moves.replace("\n", "")

    robot_pos = find_robot(map)
    for move in moves:
        robot_pos = perform_move(move, map, robot_pos)

    result = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == 'O'):
                result += 100*y + x

    #print_map(map)
    return result

def can_move(move, map, robot_pos):
    d = moves[move]
    if(move in ['<', '>']):
        pos = (robot_pos[0], robot_pos[1])
        while(True):
            #print(pos)
            pos = add_tuples(pos, d)
            if(map[pos[1]][pos[0]] == '.'):
                return True
            elif(map[pos[1]][pos[0]] == '#'):
                return False

    else:
        move1 = add_tuples(robot_pos, d)
        if(map[move1[1]][move1[0]] == '.'):
            return True
        elif(map[move1[1]][move1[0]] == '#'):
            return False
        elif(map[move1[1]][move1[0]] == '['):
            current_boxes = {((move1[0], move1[1]), (move1[0]+1, move1[1]))}
        elif(map[move1[1]][move1[0]] == ']'):
            current_boxes = {((move1[0]-1, move1[1]), (move1[0], move1[1]))}
        
        while(len(current_boxes) > 0):
            #print(pos)
            new_boxes = set()
            for box in current_boxes:
                pos1 = add_tuples(box[0], d)
                pos2 = add_tuples(box[1], d)
                if(map[pos1[1]][pos1[0]] == '#' or map[pos2[1]][pos2[0]] == '#'):
                    return False
                elif(map[pos1[1]][pos1[0]] == '[' and map[pos2[1]][pos2[0]] == ']'):
                    new_boxes.add(((pos1[0], pos1[1]), (pos2[0], pos2[1])))
                if(map[pos1[1]][pos1[0]] == ']'):
                    new_boxes.add(((pos1[0]-1, pos1[1]), (pos1[0], pos1[1])))
                if(map[pos2[1]][pos2[0]] == '['):
                    new_boxes.add(((pos2[0], pos2[1]), (pos2[0]+1, pos2[1])))

                current_boxes = new_boxes

        return True

def perform_move_part2(move, map, robot_pos):
    d = moves[move]
    if(move in ['<', '>']):
        pos = (robot_pos[0], robot_pos[1])
        prev_element = '@'
        map[robot_pos[1]][robot_pos[0]] = '.'
        while(True):
            #print(pos)
            pos = add_tuples(pos, d)
            if(map[pos[1]][pos[0]] == '#'):
                break
            new_element = map[pos[1]][pos[0]]
            map[pos[1]][pos[0]] = prev_element
            prev_element = new_element
            if(prev_element == '.'):
                break

        return add_tuples(robot_pos, d)
    else:
        move1 = add_tuples(robot_pos, d)
        if(map[move1[1]][move1[0]] == '.'):
            map[move1[1]][move1[0]] = '@'
            map[robot_pos[1]][robot_pos[0]] = '.'
            return move1
        elif(map[move1[1]][move1[0]] == '['):
            map[move1[1]][move1[0]] = '@'
            map[move1[1]][move1[0]+1] = '.'
            current_boxes = {((move1[0], move1[1]), (move1[0]+1, move1[1]))}
        elif(map[move1[1]][move1[0]] == ']'):
            map[move1[1]][move1[0]] = '@'
            map[move1[1]][move1[0]-1] = '.'
            current_boxes = {((move1[0]-1, move1[1]), (move1[0], move1[1]))}

        
        map[robot_pos[1]][robot_pos[0]] = '.'

        while(len(current_boxes) > 0):
            #print(pos)
            new_boxes = set()
            for box in current_boxes:
                pos1 = add_tuples(box[0], d)
                pos2 = add_tuples(box[1], d)
                if(map[pos1[1]][pos1[0]] == '#' or map[pos2[1]][pos2[0]] == '#'):
                    return False
                elif(map[pos1[1]][pos1[0]] == '[' and map[pos2[1]][pos2[0]] == ']'):
                    new_boxes.add(((pos1[0], pos1[1]), (pos2[0], pos2[1])))
                if(map[pos1[1]][pos1[0]] == ']'):
                    new_boxes.add(((pos1[0]-1, pos1[1]), (pos1[0], pos1[1])))
                if(map[pos2[1]][pos2[0]] == '['):
                    new_boxes.add(((pos2[0], pos2[1]), (pos2[0]+1, pos2[1])))
                
            for box in new_boxes:
                pos1 = box[0]
                pos2 = box[1]
                map[pos1[1]][pos1[0]] = '.'
                map[pos2[1]][pos2[0]] = '.'

            for box in current_boxes:
                pos1 = add_tuples(box[0], d)
                pos2 = add_tuples(box[1], d)
                map[pos1[1]][pos1[0]] = '['
                map[pos2[1]][pos2[0]] = ']'

            current_boxes = new_boxes
        return add_tuples(robot_pos, d)

def part2(input):
    raw_map, raw_moves = input.split("\n\n")

    map = raw_map.split("\n")
    for y in range(len(map)):
        map[y] = list(map[y].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
    moves = raw_moves.replace("\n", "")

    #print_map(map)

    robot_pos = find_robot(map)
    for move in moves:
        if(can_move(move, map, robot_pos)):
            robot_pos = perform_move_part2(move, map, robot_pos)
            #print_map(map)
            

    result = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == '['):
                result += 100*y + x

    #print_map(map)
    return result


print(part1(open("input15.txt", "r").read()))
print(part2(open("input15.txt", "r").read()))