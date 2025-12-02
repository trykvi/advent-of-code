def part1(input):
    patterns = input.split("\n\n")[0].split(", ")
    designs = input.split("\n\n")[1].split("\n")[:-1]

    num_possible = 0
    for design in designs:
        is_possible = [False]*len(design)
        for i in range(len(design)):
            if(design[:(i+1)] in patterns):
                is_possible[i] = True
            else:
                for j in range(i, -1, -1):
                    if(is_possible[j] and design[:(i+1)][(j+1):] in patterns):
                        is_possible[i] = True
        if(is_possible[-1]):
            num_possible += 1

    return num_possible
        
def part2(input):
    patterns = input.split("\n\n")[0].split(", ")
    designs = input.split("\n\n")[1].split("\n")[:-1]

    num_possible_ways = 0
    for design in designs:
        ways_possible = [0]*len(design)
        for i in range(len(design)):
            if(design[:(i+1)] in patterns):
                ways_possible[i] += 1
            for j in range(i, -1, -1):
                if(design[:(i+1)][(j+1):] in patterns):
                    ways_possible[i] += ways_possible[j]
        num_possible_ways += ways_possible[-1]

    return num_possible_ways

print(part1(open("input19.txt", "r").read()))
print(part2(open("input19.txt", "r").read()))