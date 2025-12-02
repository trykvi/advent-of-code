paths = open("input14.txt", "r").read().split("\n")[:-1]

highestY = 0

for i in range(len(paths)):
    paths[i] = paths[i].split(" -> ")
    for j in range(len(paths[i])):
        paths[i][j] = paths[i][j].split(",")
        paths[i][j][0] = int(paths[i][j][0])
        paths[i][j][1] = int(paths[i][j][1])
        if paths[i][j][1] > highestY:
            highestY = paths[i][j][1]

map = [["." for i in range(highestY + 1)] for j in range(1000)]

for path in paths:
    for i in range(1, len(path)):
        if path[i - 1][0] == path[i][0]:
            if(path[i - 1][1] > path[i][1]):
                for j in range(path[i][1], path[i - 1][1] + 1):
                    map[path[i - 1][0]][j] = "#"
            else:      
                for j in range(path[i - 1][1], path[i][1] + 1):       
                    map[path[i - 1][0]][j] = "#"

        elif path[i - 1][1] == path[i][1]:
            print("test1")
            if(path[i - 1][0] < path[i][0]):
                print("test2")
                for j in range(path[i - 1][0], path[i][0] + 1):
                    map[j][path[i - 1][1]] = "#"
            else:
                print("test3")
                for j in range(path[i][0], path[i - 1][0] + 1):
                    map[j][path[i - 1][1]] = "#"
        else:
            print("Error")

restingSand = 0

for y in range(100):
    print(y, end=": ")
    for x in range(475, 525):
        print(map[x][y], end="")

    print()
print("\n")
voiding = False
map[500][0] = "~"
while(not voiding):
    sand = [500, 0]
    while(True):
        if(sand[1] >= highestY):
            voiding = True
            break
        elif(map[sand[0]][sand[1] + 1] == "."):
            sand[1] += 1
        elif(map[sand[0] - 1][sand[1] + 1] == "."):
            sand[0] -= 1
            sand[1] += 1
        elif(map[sand[0] + 1][sand[1] + 1] == "."):
            sand[0] += 1
            sand[1] += 1
        else:
            map[sand[0]][sand[1]] = "O"
            restingSand += 1
            break

for y in range(174):
    print(y, end=": ")
    for x in range(475, 570):
        print(map[x][y], end="")

    print()

print(restingSand)