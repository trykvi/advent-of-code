
def countSplits(tachyonPoint, manifold, visited):
    visited[tachyonPoint[1]][tachyonPoint[0]] = True
    if(tachyonPoint[1]+1 >= len(manifold)):
        return 0
    
    if(manifold[tachyonPoint[1]+1][tachyonPoint[0]] == '.' and not visited[tachyonPoint[1]+1][tachyonPoint[0]]):
        return countSplits((tachyonPoint[0], tachyonPoint[1]+1), manifold, visited)
    
    splits = 0
    if(manifold[tachyonPoint[1]+1][tachyonPoint[0]] == '^' and not visited[tachyonPoint[1]+1][tachyonPoint[0]]):
        
        did_split = False

        if(tachyonPoint[0] > 0 and not visited[tachyonPoint[1]+1][tachyonPoint[0]-1]):
            splits += countSplits((tachyonPoint[0]-1, tachyonPoint[1]+1), manifold, visited)
            did_split = True

        if(tachyonPoint[0] < len(manifold[0])-1 and not visited[tachyonPoint[1]+1][tachyonPoint[0]+1]):
            splits += countSplits((tachyonPoint[0]+1, tachyonPoint[1]+1), manifold, visited)
            did_split = True

        if(did_split):
            splits += 1

    return splits


def part1(input):
    manifold = input.split("\n")

    result_map = [list(line) for line in input.split("\n")]

    startpos = (0, 0)
    for i in range(len(manifold[0])):
        if(manifold[0][i] == 'S'):
            startpos = (i, 0)
            break
        
    
    visited = [[False for _ in range(len(manifold[0]))] for _ in range(len(manifold))]

    splits = countSplits(startpos, manifold, visited) 

    for y in range(len(visited)):
        for x in range(len(visited[y])):
            if(visited[y][x] and manifold[y][x] != '^'):
                result_map[y][x] = '|'

    #print("\n".join("".join(line) for line in result_map))

    return splits

memo = {}

def countTimelines(tachyonPoint, manifold):
    if(tachyonPoint not in memo):
        if(tachyonPoint[1]+1 >= len(manifold)):
            memo[tachyonPoint] = 1
        
        elif(manifold[tachyonPoint[1]+1][tachyonPoint[0]] == '.'):
            memo[tachyonPoint] = countTimelines((tachyonPoint[0], tachyonPoint[1]+1), manifold) 

        elif(manifold[tachyonPoint[1]+1][tachyonPoint[0]] == '^'):
            splits = 0    

            if(tachyonPoint[0] > 0):
                splits += countTimelines((tachyonPoint[0]-1, tachyonPoint[1]+1), manifold)

            if(tachyonPoint[0] < len(manifold[0])-1):
                splits += countTimelines((tachyonPoint[0]+1, tachyonPoint[1]+1), manifold)

            memo[tachyonPoint] = splits

    return memo[tachyonPoint]

def part2(input):
    manifold = input.split("\n")

  
    startpos = (0, 0)
    for i in range(len(manifold[0])):
        if(manifold[0][i] == 'S'):
            startpos = (i, 0)
            break
        
    splits = countTimelines(startpos, manifold) 

    return splits


input = open("./AoC-2025/input7.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))
