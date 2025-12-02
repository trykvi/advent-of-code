import re

def part1(input):
    corr_mem = input.replace("\n", "")

    instructions = re.findall("mul\([\d]*,[\d]*\)", corr_mem)

    sum = 0

    for instruction in instructions:
        num1 = int(instruction.split(",")[1][:-1])
        num2 = int(instruction.split(",")[0][4:])

        sum += num1*num2

    print(sum)

def part2(input):
    corr_mem = input.replace("\n", "")

    instructions = re.findall("mul\([\d]*,[\d]*\)|do\(\)|don't\(\)", corr_mem)

    sum = 0

    todo = True

    for instruction in instructions:
        if(instruction == "do()"):
            todo = True
        elif(instruction == "don't()"):
            todo = False
        elif(todo):
            num1 = int(instruction.split(",")[1][:-1])
            num2 = int(instruction.split(",")[0][4:])

            sum += num1*num2

    print(sum)

data = open("input3.txt", "r").read()

part1(data)
part2(data)
