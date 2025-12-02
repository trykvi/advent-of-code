def isBetween(y1, y2, row):
    if(y1 <= row <= y2):
        return True
    elif(y2 <= row <= y1):
        return True
    else:
        return False

def dist(points):
    x1, y1, x2, y2 = points
    return abs(x1 - x2) + abs(y1 - y2)

N = open("input15.txt", "r").read().split("\n")[:-1]

Yrow = 2_000_000

map = ["."]*15_000_000

for i in range(len(N)):
    N[i] =  N[i].split("=")[1:]
    N[i][0] = int(N[i][0][:-3])
    N[i][1] = int(N[i][1][:-24])
    N[i][2] = int(N[i][2][:-3])
    N[i][3] = int(N[i][3])
    
    if(N[i][3] == Yrow):
        map[N[i][2] + 2_000_000] = "B"    

#Sx, SY, Bx, By




for pair in N:
    print(pair)
    for i in range(-2_000_000, 13_000_000):
        if(dist(pair) >= dist([pair[0], pair[1], i, Yrow])):
            if(map[i] == "."):
                map[i + 2_000_000] = "#"

#for i in range(20, 60):
    #print(i-25, map[i])

print(map.count("#"))