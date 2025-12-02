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

""" class Graph:
    graph = {}

    def __init__(self, map):
        queue = Queue()
        queue.put(find_element('S', map))
        visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
        path =
        current_dir = (0, -1)
        while(not queue.empty()):
            current_pos = queue.get()
            x = current_pos[0]
            y = current_pos[1]
            visited[y][x] = True

            if(not visited[y-1][x] and map[y-1][x] != '#'):

                queue.put((y-1, x))
     """

def dijkstra(map, startpos, endpos, start_dir=(1, 0)):
    dist = [[9999999999 for _ in range(len(map[0]))] for _ in range(len(map))]
    dist[startpos[1]][startpos[0]] = 0
    pq = [(0, startpos, start_dir)]
    """ for d in d_list:
        pos = add_tuples(d, startpos)
        if(map[pos[1]][pos[0]] != '#'):
            pq.put() """
    while(len(pq) > 0):
        current_dist, current_node, current_dir = heapq.heappop(pq)

        for d in d_list:
            adj_node = add_tuples(current_node, d)
            if(current_dir == d):
                adj_dist = current_dist + 1
            else:
                adj_dist = current_dist + 1001
            if(map[adj_node[1]][adj_node[0]] != '#' and dist[adj_node[1]][adj_node[0]] > adj_dist):
                dist[adj_node[1]][adj_node[0]] = adj_dist
                heapq.heappush(pq, (adj_dist, adj_node, d))

    return dist[endpos[1]][endpos[0]]

def part1(input):
    map = [list(line) for line in input.split("\n")[:-1]]
    return dijkstra(map, find_element('S', map), find_element('E', map))

def count_shortest_paths(map, min_length, prev_dir, path, current_path_length, endpos, nodes_in_best_path, best):
    #if(random.randint(0, 100) == 100):
        #print(len(path), current_path_length, path[-1])

    if(current_path_length > min_length or current_path_length % 1000 > min_length % 1000):
        return 0
    elif(current_path_length == min_length and path[-1] == endpos):
        nodes_in_best_path.update(set(path))
        return 1
    
    if(current_path_length > best[0]):
        best[0] = current_path_length
        print(len(path), current_path_length, path[-1])
    count = 0
    for d in d_list:
        adj_node = add_tuples(d, path[-1])

        if(d == prev_dir):
            added_dist = 1
        else:
            added_dist = 1001
        
        if((map[adj_node[1]][adj_node[0]]) != '#' and (adj_node not in path)):
            path.append(adj_node)
            count += count_shortest_paths(map, min_length, d, path, current_path_length + added_dist, endpos, nodes_in_best_path, best)
            path.pop()

    return count
            

def dijkstra_get_path(map, startpos, endpos):
    dist = [[9999999999 for _ in range(len(map[0]))] for _ in range(len(map))]
    dist[startpos[1]][startpos[0]] = 0
    pq = [(0, startpos, (-1, 0))]
    paths = {startpos: [(startpos, (-1, 0), 0)]}
    while(len(pq) > 0):
        current_dist, current_node, current_dir = heapq.heappop(pq)

        for d in d_list:
            adj_node = add_tuples(current_node, d)
            if(current_dir == d):
                adj_dist = current_dist + 1
            else:
                adj_dist = current_dist + 1001
            if(map[adj_node[1]][adj_node[0]] != '#' and dist[adj_node[1]][adj_node[0]] > adj_dist):
                dist[adj_node[1]][adj_node[0]] = adj_dist
                paths[adj_node] = paths[current_node] + [(adj_node, d, adj_dist)]
                heapq.heappush(pq, (adj_dist, adj_node, d))

    return paths[endpos]

def print_map(map):
    print("\n".join("".join(line) for line in map))

def prune_duplicates(node_set):
    result = set()
    for node, _, _ in node_set:
        result.add(node)

    return result

def part2(input):
    map = [list(line) for line in input.split("\n")[:-1]]
    startpos = find_element('S', map)
    endpos = find_element('E', map)
    shortest_path_length = dijkstra(map, startpos, endpos)

    shortest_path = dijkstra_get_path(map, startpos, endpos)

    checked = [[[] for _ in range(len(map[0]))] for _ in range(len(map))]

    for node, _, _ in shortest_path:
        checked[node[1]][node[0]] = [node]

    final_nodes = set(shortest_path)

    madechange = True
    while(madechange):
        madechange = False
        new_final_nodes = final_nodes.copy()
        for node, prev_d, dist in final_nodes:
            for d in d_list:
                adj_node = add_tuples(d, node)
            
                if(map[adj_node[1]][adj_node[0]] != '#' and node not in checked[adj_node[1]][adj_node[0]]):
                    adj_dist = dijkstra(map, adj_node, endpos, d) 
                    if(d == prev_d):
                        if(adj_dist + dist + 1 == shortest_path_length):
                            madechange = True
                            new_final_nodes.add((adj_node, d, dist+1))
                    else:
                        if(adj_dist + dist + 1001 == shortest_path_length):
                            madechange = True
                            new_final_nodes.add((adj_node, d, dist+1001))
                   
                    checked[adj_node[1]][adj_node[0]].append(node)

        final_nodes = new_final_nodes

    final_nodes = prune_duplicates(final_nodes)

    

    
    return len(final_nodes)

print(part1(open("input16.txt", "r").read()))
print(part2(open("input16.txt", "r").read()))