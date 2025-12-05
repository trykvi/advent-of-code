def part1(input):
    ranges = [line.split("-") for line in input.split("\n\n")[0].split("\n")]
    ingredient_ids = [int(line) for line in input.split("\n\n")[1].split("\n")]

    for i in range(len(ranges)):
        ranges[i] = (int(ranges[i][0]), int(ranges[i][1]))

    fresh = 0

    for id in ingredient_ids:

        for r in ranges:
            if(id >= r[0] and id <= r[1]):
                fresh += 1
                break

    return fresh

def part2(input):
    ranges = [line.split("-") for line in input.split("\n\n")[0].split("\n")]

    for i in range(len(ranges)):
        ranges[i] = (int(ranges[i][0]), int(ranges[i][1]))

    ranges = sorted(ranges)

    cleaned_ranges = []
    current_start = ranges[0][0]
    current_end = ranges[0][1]
    for i in range(len(ranges)):
        if(i >= len(ranges)-1):
            cleaned_ranges.append((current_start, ranges[i][1]))
            break
        elif(current_end >= ranges[i+1][1]):
            continue
        elif(current_end >= ranges[i+1][0]):
            current_end = ranges[i+1][1]
        else:
            cleaned_ranges.append((current_start, current_end))
            current_start = ranges[i+1][0] 
            current_end = ranges[i+1][1]

    total_fresh = 0

    for r in cleaned_ranges:
       total_fresh += r[1]-r[0]+1

    return total_fresh

input = open("./AoC-2025/input5.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))