def isSafe(list):
    if(list[0] > list[1]):
        for i in range(len(list) - 1):
            if(list[i] < list[i+1]):
                return False
            absdiff = abs(list[i] - list[i+1])
            if(absdiff == 0 or absdiff > 3):
                return False
    else:
        for i in range(len(list) - 1):
            if(list[i] > list[i+1]):
                return False
            absdiff = abs(list[i] - list[i+1])
            if(absdiff == 0 or absdiff > 3):
                return False
              
    return True

def part1(reports):
    return sum(1 for report in reports if(isSafe(report)))

def part2(reports):

    return sum(1 for report in reports if(isSafe(report) or any([isSafe(report[:i] + report[i+1:]) for i in range(len(report))])))

import time
starttime = time.time()

input = open("input2.txt", "r").read()
reports = [[int(val) for val in report.split(" ")] for report in input.split("\n")[:-1]]

res1 = part1(reports)
res2 = part2(reports)

endtime = time.time()

print(f"Part1 result: {res1}, Part2 result: {res2}")

print(f"Time taken: {(1000*(endtime-starttime)):.3f} ms")
