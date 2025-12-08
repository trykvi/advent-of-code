import math

def dist2(p1, p2):
    v_x = p2[0] - p1[0]
    v_y = p2[1] - p1[1]
    v_z = p2[2] - p1[2]

    return v_x*v_x + v_y*v_y + v_z*v_z

def bruteforce_circuits_in_n_closest(n, junctions, start, end):
    pairs = []
    for i in range(start, end-1):
        for j in range(i+1, end):
            pairs.append((i, j, dist2(junctions[i], junctions[j])))

    sorted_pairs = sorted(pairs, key=lambda p: p[2])

    circuits = []

    used_pairs = []

    connected_pairs = 0

    for i in range(len(sorted_pairs)):
        junc0 = sorted_pairs[i][0]
        junc0set = -1
        junc1 = sorted_pairs[i][1]
        junc1set = -1

        for j in range(len(circuits)):
            if(junc0 in circuits[j]):
                junc0set = j
            if(junc1 in circuits[j]):
                junc1set = j

        #print(i, junc0, junc0set, junc1, junc1set)
        
        if(junc0set == -1 and junc1set == -1):
 
            circuits.append({junc0, junc1})
        elif(junc0set != junc1set):
            if(junc0set >= 0 and junc1set == -1):
                circuits[junc0set].add(junc1)
            elif(junc0set == -1 and junc1set >= 0):
                circuits[junc1set].add(junc0) 
            elif(junc0set >= 0 and junc1set >= 0):
                circuits[junc0set] = circuits[junc0set].union(circuits[junc1set])
                circuits.pop(junc1set)

        connected_pairs += 1
        used_pairs.append(sorted_pairs[i])
                 
        if(connected_pairs >= n):
            break

    return circuits

def part1(input):
    junctions = [tuple(int(val) for val in point.split(",")) for point in input.split("\n")]

    circuits = bruteforce_circuits_in_n_closest(1000, junctions, 0, len(junctions))
    
    circuits = sorted(circuits, key=lambda c: len(c), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])
            
def part2(input):
    junctions = [tuple(int(val) for val in point.split(",")) for point in input.split("\n")]


    connections = []
    for i in range(0, len(junctions)):
        for j in range(i+1, len(junctions)):
            connections.append((i, j, dist2(junctions[i], junctions[j])))

    sorted_pairs = sorted(connections, key=lambda p: p[2])

    connected_junctions = set()

    last_x_prod = 1

    for pair in sorted_pairs:
        connected_junctions.add(pair[0])
        connected_junctions.add(pair[1])

        if(len(connected_junctions) == len(junctions)):
            last_x_prod *= junctions[pair[0]][0]
            last_x_prod *= junctions[pair[1]][0]
            break


    return last_x_prod

input = open("./AoC-2025/input8.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))