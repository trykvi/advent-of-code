def checkPoint(i):
    if(X-1 <= i <= X+1):
        return "#"
    else:
        return " "

N = open("input10.txt", "r").read().split("\n")[:-1]


cycle = 0
X = 1

pixels = ""

for line in N:
    line = line.split()

    if(line[0] == "noop"):
        pixels += checkPoint(cycle % 40)
        cycle += 1

    else:
        pixels += checkPoint(cycle % 40) + checkPoint((cycle + 1) % 40)
        X += int(line[1])
        cycle += 2  
        
    if(len(pixels) > 40):
        print(pixels[:-1], len(pixels)-1)
        pixels = pixels[-1]

    elif(len(pixels) == 40):
        print(pixels, len(pixels))
        pixels = ""

    #print(pixels, cycle)
print(sum)