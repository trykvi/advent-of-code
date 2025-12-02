def checkNext(j):
    if(j >= len(N)):
        return
    elif(N[j][0] != "$"):
        if(N[j][:3] == "dir"):
            fileSystem["/".join(currentPath)].append("/".join(currentPath) + "/" + N[j][4:])
        else:
            fileSystem["/".join(currentPath)].append(N[j])

        checkNext(j + 1)   
        skip[0] += 1     

N = open("input7.txt", "r").read().split("\n")[:-1]


fileSystem = dict()

i = 0

currentPath = []

while(i < len(N)):
    if(N[i][0] == "$"):
        if(N[i][2] == "c"):
            if(N[i][5:] == "/"):
                currentPath = [""]
            elif(N[i][5:] == ".."):
                currentPath = currentPath[:-1]
            else:
                currentPath.append(N[i][5:])
        elif(N[i][2] == "l"):
            fileSystem["/".join(currentPath)] = [len(currentPath)]
            skip = [1]
            checkNext(i + 1)
            i += skip[0] - 1
    
    
    i += 1
    
dirSizes = dict()

fileSystem = dict(sorted(fileSystem.items(), key=lambda x:x[1][0], reverse=True))

for dir in fileSystem:
    dirSizes[dir] = 0
    for file in fileSystem[dir][1:]:      
        if(file[0] == "/"):
            if(file in dirSizes.keys()):
                dirSizes[dir] += dirSizes[file]
        else:
            dirSizes[dir] += int(file.split()[0])

result1 = 0

for size in dirSizes.values():
    if(size <= 100000):
        result1 += size

print(result1)

dirSizes = dict(sorted(dirSizes.items(), key=lambda x:x[1]))

for dir in dirSizes.keys():
    if(dirSizes[dir] >= dirSizes[""] - 40_000_000):
        print(dirSizes[dir])
        break
