def part1(input):
    dial = 50
    times_0 = 0

    for instruction in input.split("\n"):
        dir = instruction[0]
        amount = int(instruction[1:])
        if(dir == 'R'):
            dial = (dial + amount) % 100
        else:
            dial = (dial - amount) % 100

        if(dial == 0):
            times_0 += 1

    return times_0

def part2(input):
    dial = 50
    times_0 = 0

    for instruction in input.split("\n"):
        dir = instruction[0]
        amount = int(instruction[1:])
        waszero = dial == 0
        times_0 += amount // 100
        amount = amount % 100

        if(dir == 'R'):
            dial = dial + amount
        else:
            dial = dial - amount

        if((dial <= 0 and not waszero) or dial >= 100):
            times_0 += 1
  
        dial = dial % 100


    return times_0



input = open("input1.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))