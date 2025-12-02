from functools import cmp_to_key

class Graph():
    def __init__(self, raw_input):
        self.relations = {}
        for line in raw_input.split("\n"):
            start, end = line.split("|")
            if start not in self.relations:
                self.relations[start] = []
            if end not in self.relations:
                self.relations[end] = []
            self.relations[start].append(end)

    def compare(self, start, end):
        if(end in self.relations[start]):
            return 1
        else:
            return -1
        
def isCorrectUpdateOrder(update, graph):
    for i in range(len(update)-1):
        if graph.compare(update[i], update[i+1]) == -1:
            return False
    return True

def part1(input):
    graphdata, updates = input.split("\n\n")

    graph = Graph(graphdata)

    sum = 0
    for update in updates.split("\n")[:-1]:
        update = update.split(",")
        if(isCorrectUpdateOrder(update, graph)):
            sum += int(update[len(update)//2])
    
    return sum

def part2(input):
    graphdata, updates = input.split("\n\n")

    graph = Graph(graphdata)

    sum = 0
    for update in updates.split("\n")[:-1]:
        update = update.split(",")
        if not isCorrectUpdateOrder(update, graph):
            corrected_update = sorted(update, key=cmp_to_key(graph.compare))
            sum += int(corrected_update[len(corrected_update)//2])

    return sum




print(part1(open("input5.txt", "r").read()))
print(part2(open("input5.txt", "r").read()))