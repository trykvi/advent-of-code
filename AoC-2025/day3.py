def part1(input):
    banks = input.split("\n")
    total_joltage = 0

    for bank in banks:
        first_battery = 0
        first_battery_idx = 0

        for i in range(len(bank)-1):
            if(int(bank[i]) > first_battery):
                first_battery = int(bank[i])
                first_battery_idx = i

        second_battery = 0
        
        for i in range(first_battery_idx+1, len(bank)):
            if(int(bank[i]) > second_battery):
                second_battery = int(bank[i])

        total_joltage += int(str(first_battery) + str(second_battery))
        
    return total_joltage

def part2(input):
    banks = input.split("\n")
    total_joltage = 0

    for bank in banks:
        batteries = []
        prev_battery_idx = -1

        for i in range(12):
            batteries.append(0)
            for j in range(prev_battery_idx+1, len(bank)-11+i):
                if(int(bank[j]) > batteries[-1]):
                    batteries[-1] = int(bank[j])
                    prev_battery_idx = j

        total_joltage += int("".join([str(battery) for battery in batteries]))
        
    return total_joltage


input = open("./AoC-2025/input3.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))