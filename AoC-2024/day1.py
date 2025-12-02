import numpy as np
from collections import Counter

def part1(input):
    list1, list2 = [], []

    for tuple in input.split("\n")[:-1]:
        tuple = tuple.split("   ")

        list1.append(int(tuple[0]))
        list2.append(int(tuple[1]))

    list1 = np.array(sorted(list1))
    list2 = np.array(sorted(list2))

    diff = [abs(elem) for elem in np.subtract(list1, list2)]

    return np.sum(diff)


def part2(input):
    list1, list2 = [], []

    for tuple in input.split("\n")[:-1]:
        tuple = tuple.split("   ")

        list1.append(int(tuple[0]))
        list2.append(int(tuple[1]))

    list1 = sorted(list1)
    list2 = sorted(list2)

    counts = Counter(list2)

    similarity_score = 0
    
    for elem in list1:
        similarity_score += elem * counts[elem]

    return similarity_score



import time
starttime = time.time()

res1 = part1(open("input1.txt", "r").read())
res2 = part2(open("input1.txt", "r").read())

endtime = time.time()

print(f"Part1 result: {res1}, Part2 result: {res2}")

print(f"Time taken: {(1000*(endtime-starttime)):.3f} ms")