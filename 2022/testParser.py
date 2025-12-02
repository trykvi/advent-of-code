N = open("input7.txt", "r").read().split("\n")[:-1]

sum = 0

for line in N:
    if(line[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
        sum += int(line.split()[0])

print(sum)


sum = 49199225