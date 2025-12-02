def unrollFile(file):
    unrolled_file = []
    for i in range(len(file)):
        if i % 2 == 0:
            unrolled_file += [str(i//2)]*int(file[i])
        else:
            unrolled_file += ['.']*int(file[i])

    return unrolled_file

def calc_checksum(file):
    result = 0
    for i in range(len(file)):
        if(file[i] != '.'):
            result += int(file[i])*i

    return result

def part1(input):
    unrolled = unrollFile(input.split("\n")[0])

    i = 0
    while i < len(unrolled):
        if(unrolled[i] == '.'):
            for j in range(1, len(unrolled) + 1):
                if(j+i >= len(unrolled)):
                    unrolled = unrolled[:i]
                    break
                if(unrolled[-j] != '.'):
                    unrolled[i] = unrolled[-j]
                    unrolled = unrolled[:-j]
                    break

        i += 1
    #print("".join(unrolled))
    checksum = calc_checksum(unrolled)
            
    return checksum


def part2(input):
    unrolled = unrollFile(input.split("\n")[0])
    #file = input.split("\n")[0]
    i = len(unrolled)-1
    #print(unrolled)
    while i >= 0:
        if(unrolled[i] != '.'):
            blocksize_num = 0
            val = unrolled[i]
            while(unrolled[i] == val):
                blocksize_num += 1
                i -= 1
            
            i += 1
            
            k = 0
            while k < i:
                if(unrolled[k] == '.'):
                    blocksize_space = 0
                    while(unrolled[k] == '.'):
                        blocksize_space += 1
                        k += 1

                    if(blocksize_space >= blocksize_num):
                        #print(blocksize_space, blocksize_num)
                        for j in range(blocksize_num):
                            index = k - blocksize_space + j
                            #print(index, unrolled[i+j])
                            unrolled[index] = unrolled[i+j]
                            unrolled[i+j] = '.'
                        #print("".join(unrolled))
                        break
                
                k += 1

        i -= 1

    #print(")(".join(unrolled))
    checksum = calc_checksum(unrolled)
    return checksum
    




print(part1(open("input9.txt", "r").read()))
print(part2(open("input9.txt", "r").read()))