N = open("input10.txt", "r").read().split("\n")[:-1]

sumA = []
sum = 0
cycle = 1
X = 1

for line in N:
    line = line.split()

    if(cycle % 40 == 20):
        signal = X*cycle
        sumA.append(signal)
        sum += signal
    elif((cycle + 1) % 40 == 20 and line[0] == "addx"):
        signal = X*(cycle + 1)
        sumA.append(signal)
        sum += signal

    if(line[0] == "noop"):
        cycle += 1
    else:
        cycle += 2  
        X += int(line[1])

print(sum)