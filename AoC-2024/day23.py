def part1(input):
    connections = [(line.split("-")[0], line.split("-")[1]) for line in input.split("\n")[:-1]]

    neighbors = dict()

    for connection in connections:
        if(connection[0] not in neighbors):
            neighbors[connection[0]] = set()
        if(connection[1] not in neighbors):
            neighbors[connection[1]] = set()

        neighbors[connection[0]].add(connection[1])
        neighbors[connection[1]].add(connection[0])

    sets = set()

    for client in neighbors.keys():
        if(client[0] == 't'):
            for neighbor1 in neighbors[client]:
                for neighbor2 in neighbors[neighbor1]:
                    if neighbor2 in neighbors[client]:
                        sets.add(frozenset([client, neighbor1, neighbor2]))

    return len(sets)


def find_maximal_clique(startnode, graph):
    clique = [startnode]
    stack = [startnode]
    
    while(len(stack) > 0):
        current_node = stack.pop()
        for adj_node in graph[current_node]:
            if(adj_node not in clique):
                add = True
                for node in clique:
                    if adj_node not in graph[node]:
                        add = False
                        break
                if(add):
                    clique.append(adj_node)
                    stack.append(adj_node)
                    
    return set(clique)
        


def part2(input):
    connections = [(line.split("-")[0], line.split("-")[1]) for line in input.split("\n")[:-1]]

    neighbors = dict()

    for connection in connections:
        if(connection[0] not in neighbors):
            neighbors[connection[0]] = set()
        if(connection[1] not in neighbors):
            neighbors[connection[1]] = set()

        neighbors[connection[0]].add(connection[1])
        neighbors[connection[1]].add(connection[0])

    
    nodes_left = set(neighbors.keys())
    biggest_clique = set()
    i = 0
    while(len(nodes_left) > 0):
        selected_node = nodes_left.pop()
        nodes_left.add(selected_node)
        clique = find_maximal_clique(selected_node, neighbors)

        if(len(clique) > len(biggest_clique)):
            biggest_clique = clique

        nodes_left = nodes_left - clique

        i += 1

    password = ",".join(sorted(list(biggest_clique)))

    return password


print(part1(open("input23.txt", "r").read()))
print(part2(open("input23.txt", "r").read()))