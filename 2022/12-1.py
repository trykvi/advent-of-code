grid = open("input12.txt", "r").read().split("\n")[:-1]

for i in range(len(grid)):
    grid[i] = list(grid[i])
    if("S" in grid[i]):
        Spos = [i, grid[i].index("S")]
        grid[i][grid[i].index("S")] = "a"

    if("E" in grid[i]):
        Epos = [i, grid[i].index("E")]
        grid[i][grid[i].index("E")] = "z"

queue = [Spos]

steps = 0

usedPos = [Spos]

while(Epos not in queue and len(queue) != 0):
    print(queue)
    tempQueue = queue.copy()
    queue = []
    for pos in tempQueue:
        x, y = pos
        #Left
        if(x != 0):
            if(abs(ord(grid[x - 1][y]) - ord(grid[x][y]) <= 1) and ([x - 1, y] not in usedPos)):
                queue.append([x - 1, y])
                usedPos.append([x - 1, y])
        #Right
        if(x != len(grid) - 1):   
            if(abs(ord(grid[x + 1][y]) - ord(grid[x][y]) <= 1) and ([x + 1, y] not in usedPos)):
                queue.append([x + 1, y])
                usedPos.append([x + 1, y])
        #Up
        if(y != 0):
            if(abs(ord(grid[x][y - 1]) - ord(grid[x][y]) <= 1) and ([x, y - 1] not in usedPos)):
                queue.append([x, y - 1])
                usedPos.append([x, y - 1])
        #Down
        if(y != len(grid[0]) - 1):
            if(abs(ord(grid[x][y + 1]) - ord(grid[x][y]) <= 1) and ([x, y + 1] not in usedPos)):
                queue.append([x, y + 1])
                usedPos.append([x, y + 1])
    
    steps += 1

print(steps)