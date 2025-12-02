N = open("input1.txt", "r").read().split("\n")[:-1]

foodCounts = [0]


for line in N:
    if(line == ""):
        foodCounts.append(0)
        continue
    else:
        foodCounts[-1] += int(line)

foodCounts.sort()
print(foodCounts[-1] + foodCounts[-2] + foodCounts[-3])