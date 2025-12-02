def operation(old, eqation):
    n1, op, n2 = eqation.split()
    if(n1 == "old"):
        n1 = old
    else:
        n1 = int(n1)
    if(n2 == "old"):
        n2 = old
    else:
        n2 = int(n2)
    
    if(op == "+"):
        new = n1 + n2 
    elif(op == "-"):
        new = n1 - n2
    elif(op == "*"):
        new = n1 * n2
    elif(op == "/"):
        new = n1 // n2
    
    return new // 3

N = open("input11.txt", "r").read().split("\n")

monkeys = len(N)//7

items = [[]*monkeys for i in range(monkeys)]

inspectedTimes = [0]*monkeys

for i in range(1,len(N),7):
    for item in N[i].split(": ")[1].split(", "):
        items[i//7].append(item)

for i in range(20):
    for j in range(monkeys):
        for k in range(len(items[j])):
            inspectedTimes[j] += 1
            items[j][k] = operation(int(items[j][k]), N[j*7+2].split("= ")[1])

            if(items[j][k] % int(N[j*7+3].split(" ")[-1]) == 0):
                toMonkey = int(N[j*7+4].split(" ")[-1])
            else:
                toMonkey = int(N[j*7+5].split(" ")[-1])
            items[toMonkey].append(items[j][k])
        items[j] = []

inspectedTimes = sorted(inspectedTimes)


monkeyBusiness = inspectedTimes[-1] * inspectedTimes[-2]

print(monkeyBusiness)