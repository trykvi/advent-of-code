N = open("input3.txt", "r").read().split("\n")[:-1]

sumValue = 0

for line in N:
    comp1 = line[:len(line)//2]
    comp2 = line[len(line)//2:]

    for c in comp1:
        if(c in comp2):
            if(c.isupper()):
                sumValue += ord(c) - 38
            else:
                sumValue += ord(c) - 96
            break

print(sumValue)