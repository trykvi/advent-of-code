grid = open("input12.txt", "r").read().split("\n")[:-1]

aPoses = []

for i in range(len(grid)):
    grid[i] = list(grid[i])
    for j in range(len(grid[i])):
        if(grid[i][j] == "E"):
            Epos = [i, j]
            grid[i][j] = "z"
        elif(grid[i][j] == "a"):
            aPoses.append([i, j])
pathLenghts = set()

print(len(aPoses))
for aPos in aPoses:

    queue = [aPos]

    steps = 0

    usedPos = [aPos]

    while(Epos not in queue):
        tempQueue = queue.copy()
        queue = []
        for pos in tempQueue:
            x, y = pos
            #Left
            if(x != 0):
                if(abs(ord(grid[x - 1][y]) - ord(grid[x][y]) <= 1) and ([x - 1, y] not in usedPos)):
                    if(grid[x - 1][y] != "a"):    
                        queue.append([x - 1, y])
                        usedPos.append([x - 1, y])
            #Right
            if(x != len(grid) - 1):   
                if(abs(ord(grid[x + 1][y]) - ord(grid[x][y]) <= 1) and ([x + 1, y] not in usedPos)):
                    if(grid[x + 1][y] != "a"):
                        queue.append([x + 1, y])
                        usedPos.append([x + 1, y])
            #Up
            if(y != 0):
                if(abs(ord(grid[x][y - 1]) - ord(grid[x][y]) <= 1) and ([x, y - 1] not in usedPos)):
                    if(grid[x][y - 1] != "a"):
                        queue.append([x, y - 1])
                        usedPos.append([x, y - 1])
            #Down
            if(y != len(grid[0]) - 1):
                if(abs(ord(grid[x][y + 1]) - ord(grid[x][y]) <= 1) and ([x, y + 1] not in usedPos)):
                    if(grid[x][y + 1] != "a"):
                        queue.append([x, y + 1])
                        usedPos.append([x, y + 1])
        
        if(len(queue) == 0):
            steps = 1e50
            break
        steps += 1

    pathLenghts.add(steps)

print(min(pathLenghts))