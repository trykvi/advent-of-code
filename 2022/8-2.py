def upC(x, y):
    y2 = y - 1 
    result = 0
    while(y2 >= 0):
        result += 1
        if(N[y][x] <= N[y2][x]):
            break
        y2 -= 1
    return result

def downC(x, y):
    y2 = y + 1
    result = 0
    while(y2 < len(N)):
        result += 1
        if(N[y][x] <= N[y2][x]):
            break
        y2 += 1
    return result

def leftC(x, y):
    x2 = x - 1 
    result = 0
    while(x2 >= 0):
        result += 1
        if(N[y][x] <= N[y][x2]):
            break
        x2 -= 1
    return result

def rightC(x, y):
    x2 = x + 1
    result = 0
    while(x2 < len(N)):
        result += 1
        if(N[y][x] <= N[y][x2]):
            break
        x2 += 1
    return result


N = open("input8.txt", "r").read().split("\n")[:-1]

for i in range(len(N)):
    N[i] = [int(x) for x in N[i]]

scenicScores = [[1]*len(N[0]) for x in range(len(N))]


for i in range(len(N)):
    for j in range(len(N)):
        #print(j, i, leftC(i, j))
        #West
        scenicScores[i][j] *= leftC(j, i)
        #East
        scenicScores[i][j] *= rightC(j, i)
        #North
        scenicScores[i][j] *= upC(j, i)
        #South
        scenicScores[i][j] *= downC(j, i)

highestScore = 0

print(scenicScores)

for line in scenicScores:
    for tree in line:
        if(tree > highestScore):
            highestScore = tree

print(highestScore)