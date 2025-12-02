def add_tuples(t1, t2):
    return tuple(map(lambda x, y: x+y, t1, t2))

def does_fit_in(key, lock):
    for elem in add_tuples(key, lock):
        if(elem > 5):
            return False
    
    return True

def part1(input):
    keys = []
    locks = []

    for candidate in input.split("\n\n"):
        candidate_map = candidate.split("\n")
        counts = [-1, -1, -1, -1, -1]
        for x in range(len(candidate_map[0])):
            for y in range(len(candidate_map)):
                if(candidate_map[y][x] == '#'):
                    counts[x] += 1

        if(candidate_map[0] == '#####' and candidate_map[6] == '.....'):
            locks.append(tuple(counts))
        else:
            keys.append(tuple(counts))
        

    unique_pairs = set()

    #print(keys)
    #print(locks)

    for key in keys:
        for lock in locks:
            #print(add_tuples(key, lock), key, lock)
            if(does_fit_in(key, lock)):
                unique_pairs.add((key, lock))

    return len(unique_pairs)

print(part1(open("input25.txt", "r").read()))
