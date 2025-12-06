import time

memo = {}

def count_stones_after_blinks(n, stoneNum):
    #print(stoneNum)
    hash = str(n) + ":" + str(stoneNum)
    if hash in memo:
        return memo[hash]
    
    if n == 0:
        memo[hash] =  1
    elif stoneNum == 0:
        memo[hash] = count_stones_after_blinks(n-1, 1)
    elif len(str(stoneNum)) % 2 == 0:
        i = len(str(stoneNum)) // 2
        memo[hash] = count_stones_after_blinks(n-1, int(str(stoneNum)[:i])) + count_stones_after_blinks(n-1, int(str(stoneNum)[i:]))
    else:
        memo[hash] = count_stones_after_blinks(n-1, stoneNum*2024)
    
    return memo[hash]

def part1(input):
    stones = input.split("\n")[0].split(" ")
    result = 0
    for stone in stones:
        result += count_stones_after_blinks(25, int(stone))
    
    return result

def part2(input):
    stones = input.split("\n")[0].split(" ")
    result = 0
    for stone in stones:
        result += count_stones_after_blinks(75, int(stone))
    
    return result

t0 = time.time()
print(part1(open("./AoC-2024/input11.txt", "r").read()))
print(part2(open("./AoC-2024/input11.txt", "r").read()))
t1 = time.time()

#print(len(memo.keys()))

print(f"{(t1-t0)*1000:.2f}ms")