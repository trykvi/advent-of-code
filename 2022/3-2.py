N = open("input3.txt", "r").read().split("\n")[:-1]

sumVal = 0

for i in range(len(N)//3):
    for c in N[i*3]:
        if(c in N[i*3+1] and c in N[i*3+2]):
            if(c.isupper()):
                sumVal += ord(c) - 38
            else:
                sumVal += ord(c) - 96
            break

print(sumVal)