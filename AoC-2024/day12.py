def BFS(pos, visited, farm):
    x = pos[0]
    y = pos[1]
    result = {pos}
    visited[y][x] = True

    total_adj = set()
    total_sides = set()

    if y > 0 and not visited[y-1][x] and farm[y][x] == farm[y-1][x]:
        this_result, adj, sides = BFS((x, y-1), visited, farm)
        result.update(this_result)
        total_adj.update(adj)
        total_adj.add(frozenset([pos, (x, y-1)]))
        total_sides.update(sides)
    elif y > 0 and farm[y][x] == farm[y-1][x]:
        total_adj.add(frozenset([pos, (x, y-1)]))
    else:
        total_sides.add((pos, (x, y-1)))
    if x < len(farm[0])-1 and not visited[y][x+1] and farm[y][x] == farm[y][x+1]:
        this_result, adj, sides = BFS((x+1, y), visited, farm)
        result.update(this_result)
        total_adj.update(adj)
        total_adj.add(frozenset([pos, (x+1, y)]))
        total_sides.update(sides)
    elif x < len(farm[0])-1 and farm[y][x] == farm[y][x+1]:
        total_adj.add(frozenset([pos, (x+1, y)]))
    else:
        total_sides.add((pos, (x+1, y)))
    if y < len(farm)-1 and not visited[y+1][x] and farm[y][x] == farm[y+1][x]:
        this_result, adj, sides = BFS((x, y+1), visited, farm)
        result.update(this_result)
        total_adj.update(adj)
        total_adj.add(frozenset([pos, (x, y+1)]))
        total_sides.update(sides)
    elif y < len(farm)-1 and farm[y][x] == farm[y+1][x]:
        total_adj.add(frozenset([pos, (x, y+1)]))
    else:
        total_sides.add((pos, (x, y+1)))
    if x > 0 and not visited[y][x-1] and farm[y][x] == farm[y][x-1]:
        this_result, adj, sides = BFS((x-1, y), visited, farm)
        result.update(this_result)
        total_adj.update(adj)
        total_adj.add(frozenset([pos, (x-1, y)]))
        total_sides.update(sides)
    elif x > 0 and farm[y][x] == farm[y][x-1]:
        total_adj.add(frozenset([pos, (x-1, y)]))
    else:
        total_sides.add((pos, (x-1, y)))

    return (result, total_adj, total_sides)

def get_regions(farm):
    regions = {}
    adjacencies = {}
    sides = {}
    visited = [[False for _ in range(len(farm[0]))] for _ in range(len(farm))]
    for y in range(len(farm)):
        for x in range(len(farm[y])):
            if not visited[y][x]:
                regions[f"{farm[y][x]} {y} {x}"], adjacencies[f"{farm[y][x]} {y} {x}"], sides[f"{farm[y][x]} {y} {x}"] = BFS((x, y), visited, farm)

    return (regions, adjacencies, sides)

def count_sides(sides):
    sideList = list(sides)
    haveUsed = [False]*len(sideList)
    count = 0
    for i in range(len(sideList)):
        if not haveUsed[i]:
            count += 1
            haveUsed[i] = True

            queue = [sideList[i]]
            while(len(queue) > 0):
                currentSide = queue.pop()
                x0 = currentSide[0][0]
                x1 = currentSide[1][0]
                y0 = currentSide[0][1]
                y1 = currentSide[1][1]
                if x0 == x1 and abs(y0-y1) == 1:
                    west = ((x0-1, y0), (x1-1, y1))
                    east = ((x0+1, y0), (x1+1, y1))
                    if west in sides and not haveUsed[sideList.index(west)]:
                        queue.append(west)
                        haveUsed[sideList.index(west)] = True
                    if east in sides and not haveUsed[sideList.index(east)]:
                        queue.append(east)
                        haveUsed[sideList.index(east)] = True
                elif abs(x0-x1) == 1 and y0 == y1:
                    north = ((x0, y0-1), (x1, y1-1))
                    south = ((x0, y0+1), (x1, y1+1))
                    if north in sides and not haveUsed[sideList.index(north)]:
                        queue.append(north)
                        haveUsed[sideList.index(north)] = True
                    if south in sides and not haveUsed[sideList.index(south)]:
                        queue.append(south)
                        haveUsed[sideList.index(south)] = True
    
    return count



def part1(input):
    farm = [list(line) for line in input.split("\n")[:-1]]

    regions, adjacencies, _ = get_regions(farm)

    total_cost = 0

    for region in regions.keys():
        area = len(regions[region])
        perimeter = area*4-len(adjacencies[region])*2

        total_cost += area*perimeter

    return total_cost

def part2(input):
    farm = [list(line) for line in input.split("\n")[:-1]]

    regions, adjacencies, sides = get_regions(farm)

    total_cost = 0

    for region in regions.keys():
        area = len(regions[region])
        num_sides = count_sides(sides[region])

        total_cost += area*num_sides

    return total_cost



print(part1(open("input12.txt", "r").read()))
print(part2(open("input12.txt", "r").read()))
