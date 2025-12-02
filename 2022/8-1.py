N = open("input8.txt", "r").read().split("\n")[:-1]

for i in range(len(N)):
    N[i] = [int(x) for x in N[i]]

visible = [[False]*len(N[0]) for x in range(len(N))]



for i in range(len(N)):
    for j in range(len(N)):
        print(i, j)
        if(i == 0 or i == len(N) - 1 or j == 0 or j == len(N) - 1):
            visible[i][j] = True
        else:
            #West
            if(all([(N[i][j] > x) for x in N[i][:j]])):
                visible[i][j] = True
            #East
            elif(all([(N[i][j] > x) for x in N[i][j+1:]])):
                visible[i][j] = True
            #North
            elif(all([(N[i][j] > x) for x in [N[k][j] for k in range(i)]])):
                visible[i][j] = True
            #South
            elif(all([(N[i][j] > x) for x in [N[k][j] for k in range(i+1, len(N))]])):
                visible[i][j] = True

sum = 0

for line in visible:
    for tree in line:
        if(tree):
            sum += 1

print(sum)
            