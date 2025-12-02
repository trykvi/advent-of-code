def isValidSimple(id):
    length = len(id)
    if(length % 2 == 1):
        return True
    
    if(id[:(length//2)] == id[(length//2):]):
        return False
    
    return True


def part1(input):
    id_ranges = input.split(",")

    invalid_ids_sum = 0

    for id_range in id_ranges:
        id1 = id_range.split("-")[0]
        id2 = id_range.split("-")[1]

        for id in range(int(id1), int(id2)+1):
            if(not isValidSimple(str(id))):
                invalid_ids_sum += id

    return invalid_ids_sum

def isValidHard(id):
    parts = 2
    length = len(id)
    while(parts <= len(id)):
        if(length % parts == 0):

            isInvalid = True
            startsubstring = id[:(length//parts)]
            for i in range(1, parts):
                if(id[:(length//parts*(i+1))][(length//parts*i):] != startsubstring):
                    isInvalid = False

            if(isInvalid):
                return False
        
        parts += 1
    
    return True

def part2(input):
    id_ranges = input.split(",")

    invalid_ids_sum = 0

    for id_range in id_ranges:
        id1 = id_range.split("-")[0]
        id2 = id_range.split("-")[1]

        for id in range(int(id1), int(id2)+1):
            if(not isValidHard(str(id))):
                invalid_ids_sum += id


    return invalid_ids_sum


input = open("input2.txt", "r").read().rstrip()
print(part1(input))
print(part2(input))

