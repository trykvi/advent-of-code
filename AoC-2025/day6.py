import re

def transpose(list2d):
    transposed = []
    for x in range(len(list2d[0])):
        line = []
        for y in range(len(list2d)):
            line.append(list2d[y][x])
        transposed.append(line)

    return transposed

def part1(input):
    input = re.sub(" +", " ", input)
    equations = transpose([line.rstrip().lstrip().split(" ") for line in input.split("\n")])

    total = 0

    for eq in equations:
        if(eq[-1] == '+'):
            for val in eq[:-1]:
                total += int(val)
        else:
            temp_total = 1
            for val in eq[:-1]:
                temp_total *= int(val)
            
            total += temp_total
    
    return total

def part2(input):
    raw_eqs = input.split("\n")

    true_equations = []

    for x in range(len(raw_eqs[0])):
        if(x < len(raw_eqs[-1]) and raw_eqs[-1][x] != ' '):
            true_equation = []
            for i in range(5):
                if(x+i >= len(raw_eqs[0])):
                    break
                true_num = []
                for j in range(len(raw_eqs)-1):
                    if(raw_eqs[j][x+i] != ' '):
                        true_num.append(raw_eqs[j][x+i])

                if(len(true_num) == 0):
                    break

                true_equation.append(int("".join(true_num)))
            
            true_equation.append(raw_eqs[-1][x])
            true_equations.append(true_equation)

    total = 0

    for eq in true_equations:
        if(eq[-1] == '+'):
            for val in eq[:-1]:
                total += int(val)
        else:
            temp_total = 1
            for val in eq[:-1]:
                temp_total *= int(val)
            
            total += temp_total
    
    return total



input = open("./AoC-2025/input6.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))