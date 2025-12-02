def getFrequencies(citymap):
    frequencies = {}
    for y in range(len(citymap)):
        for x in range(len(citymap[y])):
            if(citymap[y][x] != '.'):
                if citymap[y][x] not in frequencies:
                    frequencies[citymap[y][x]] = []    
                frequencies[citymap[y][x]].append((x, y))
    
    return frequencies

def findAntinodes(frequencies, maxX, maxY):
    antinodes = set()
    for frequencyType in frequencies.keys():
        for (x1, y1) in frequencies[frequencyType]:
            for (x2, y2) in frequencies[frequencyType]:
                if(x1 == x2 and y1 == y2):
                    continue
                p1 = (x1+(x1-x2), y1+(y1-y2))
                p2 = (x2+(x2-x1), y2+(y2-y1))
                if(p1[0] >= 0 and p1[1] >= 0 and p1[0] <= maxX and p1[1] <= maxY):
                    antinodes.add(p1)

                if(p2[0] >= 0 and p2[1] >= 0 and p2[0] <= maxX and p2[1] <= maxY):
                    antinodes.add(p2)

    return antinodes

def findAntinodesAny(frequencies, maxX, maxY):
    antinodes = set()
    for frequencyType in frequencies.keys():
        for (x1, y1) in frequencies[frequencyType]:
            for (x2, y2) in frequencies[frequencyType]:
                if(x1 == x2 and y1 == y2):
                    antinodes.add((x1, y1))
                    continue

                p1 = (x1+(x1-x2), y1+(y1-y2))
                i = 1
                while(p1[0] >= 0 and p1[1] >= 0 and p1[0] <= maxX and p1[1] <= maxY):
                    #print(f"x={p1[0]}, y={p1[1]}")
                    i += 1
                    antinodes.add(p1)
                    p1 = (x1+(x1-x2)*i, y1+(y1-y2)*i)

                p2 = (x2+(x2-x1), y2+(y2-y1))
                i = 1
                while(p2[0] >= 0 and p2[1] >= 0 and p2[0] <= maxX and p2[1] <= maxY):
                    #print(f"x={p2[0]}, y={p2[1]}")
                    i += 1
                    antinodes.add(p2)
                    p2 = (x2+(x2-x1)*i, y2+(y2-y1)*i)

    return antinodes

def createAntinodeMap(antinodes, width, height):
    amap = [["."]*width for i in range(height)]
    for a in antinodes:
        amap[a[1]][a[0]] = "#"

    return amap
                    

def part1(input):
    citymap = [list(line) for line in input.split("\n")[:-1]]

    frequencies = getFrequencies(citymap)
    antinodes = findAntinodes(frequencies, len(citymap[0])-1, len(citymap)-1)

    #print(frequencies)
    #print(antinodes)
    print(len(antinodes))
    #print("\n".join("".join(line) for line in createAntinodeMap(antinodes, len(citymap[0]), len(citymap))))

def part2(input):
    citymap = [list(line) for line in input.split("\n")[:-1]]

    frequencies = getFrequencies(citymap)
    antinodes = findAntinodesAny(frequencies, len(citymap[0])-1, len(citymap)-1)

    #print(antinodes)
    #print("\n".join("".join(line) for line in createAntinodeMap(antinodes, len(citymap[0]), len(citymap))))
    print(len(antinodes))



part1(open("input8.txt", "r").read())
part2(open("input8.txt", "r").read())

