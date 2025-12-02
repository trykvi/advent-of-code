N = open("testInput.txt", "r").read().split("\n")[:-1]

graph = dict()

for line in N:
    graph[line[6:][:2]] = [int(line.split(";")[0][23:])] + line.split(";")[1][24:].split(",")

sortedValves = sorted(graph.values(), key=lambda x: x[0], reverse=True)

print(graph)

print(sortedValves)
