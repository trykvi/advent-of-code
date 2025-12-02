def mix(secret_num, value):
    return secret_num ^ value

def prune(secret_num):
    return secret_num % 16777216

def calc_next_num(secret_num):
    secret_num = prune(mix(secret_num, secret_num * 64))
    secret_num = prune(mix(secret_num, secret_num//32))
    secret_num = prune(mix(secret_num, secret_num*2048))

    return secret_num


def part1(input):
    secret_nums = [int(num) for num in input.split("\n")[:-1]]

    result = 0

    for secret_num in secret_nums:
        for _ in range(2000):
            secret_num = calc_next_num(secret_num)

        #print(secret_num)
        result += secret_num
    #print("")
    return result

def part2(input):
    secret_nums = [int(num) for num in input.split("\n")[:-1]]

    sequences = []
    

    for secret_num in secret_nums:
        sequence = [secret_num % 10]
        for i in range(2000):
            secret_num = calc_next_num(secret_num)
            sequence.append(secret_num % 10)

        sequences.append(sequence)


    change_sequences = []

    for sequence in sequences:
        change_sequence = []
        for i in range(len(sequence)-1):
            change_sequence.append(sequence[i+1] - sequence[i])

        change_sequences.append(change_sequence)

    bananas = dict()

    for i in range(len(change_sequences)):
        haveused = set()
        for j in range(len(change_sequences[i])-3):
            key = (change_sequences[i][j], change_sequences[i][j+1], change_sequences[i][j+2], change_sequences[i][j+3])
            if key not in bananas:
                bananas[key] = 0
            if(key not in haveused):
                bananas[key] += sequences[i][j+4]
                haveused.add(key)

    best_banana_count = sorted(bananas.items(), key=lambda item: item[1], reverse=True)[0][1]

    return best_banana_count

print(part1(open("input22.txt", "r").read()))
print(part2(open("input22.txt", "r").read()))