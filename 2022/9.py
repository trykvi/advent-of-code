def checkAdj(x, y):
    #UL
    if(grid[x-1][y-1] == "T"):
        return True
    #U
    if(grid[x][y-1] == "T"):
        return True
    #UR
    if(grid[x+1][y-1] == "T"):
        return True
    #R
    if(grid[x+1][y] == "T"):
        return True
    #DR
    if(grid[x+1][y+1] == "T"):
        return True
    #D
    if(grid[x][y+1] == "T"):
        return True
    #DL
    if(grid[x-1][y+1] == "T"):
        return True
    #L
    if(grid[x-1][y] == "T"):
        return True
    if(grid[x][y] == "T"):
        return True

    return False

N = open("input9.txt", "r").read().split("\n")[:-1]

grid = [["."]*1000 for x in range(1000)]


path = [["."]*1000 for x in range(1000)]


x, y = 500, 500
xt, yt = 500, 500
for line in N:
    line = line.split(" ")
    line[1] = int(line[1])

    for i in range(line[1]):
        if(line[0] == "R"):
            grid[x][y] = "."
            x += 1
            if(not checkAdj(x, y)):
                print(line, x-1, y)
                grid[xt][yt] = "."
                xt, yt = x-1, y
                grid[xt][yt] = "T"
                path[xt][yt] = "#"
            
        elif(line[0] == "L"):
            grid[x][y] = "."
            x -= 1
            if(not checkAdj(x, y)):
                print(line, x+1, y)
                grid[xt][yt] = "."
                xt, yt = x+1, y
                grid[xt][yt] = "T"
                path[xt][yt] = "#"
        
        elif(line[0] == "U"):
            grid[x][y] = "."
            y -= 1
            if(not checkAdj(x, y)):
                print(line, x, y+1)
                grid[xt][yt] = "."
                xt, yt = x, y+1
                grid[xt][yt] = "T"
                path[xt][yt] = "#"

        elif(line[0] == "D"):
            grid[x][y] = "."
            y += 1
            if(not checkAdj(x, y)):
                print(line, x, y-1)
                grid[xt][yt] = "."
                xt, yt = x, y-1
                grid[xt][yt] = "T"
                path[xt][yt] = "#"
 
        grid[x][y] = "H"

sum = 0

for i in range(len(path[0])):
    for j in range(len(path)):
        print(path[j][i], end="")
    print()

print("\n")

for line in path:
    for part in line:
        if(part == "#"):
            sum += 1

print(sum)