N = open("input5.txt", "r").read().split("\n")[:-1]


splitIndex = N.index("") - 1

stacks = [""]*int(N[splitIndex][-2])

for i in range(splitIndex):
    line = N[i]
    for j in range(len(line)):
        if(line[j] == "["):
            stacks[j//4] += line[j+1]

for i in range(splitIndex + 2, len(N)):
    line = N[i].split(" ")
    amount = int(line[1])
    fromStack = int(line[3]) - 1
    toStack = int(line[5]) - 1

    stacks[toStack] = stacks[fromStack][:amount] + stacks[toStack]
    stacks[fromStack] = stacks[fromStack][amount:]

result = ""
for stack in stacks:
    result += stack[0]
print(result)