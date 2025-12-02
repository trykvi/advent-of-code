import re
import concurrent.futures
import math

def get_combo(operand, regs):
    if(operand == 4):
        return regs[0]
    elif(operand == 5):
        return regs[1]
    elif(operand == 6):
        return regs[2]
    else:
        return [operand]


def part1(input):
    regA, regB, regC = [[int(reg)] for reg in re.findall("\d+", input.split("\n\n")[0])]
    instructions = [int(ins) for ins in re.findall("\d+", input.split("\n\n")[1])] 

    #regA = [117447]  
    regs = [regA, regB, regC]     

       

    #print(regA, regB, regC)
    #print(instructions)
    i = 0
    outputs = []
    while(i < len(instructions)-1):
        opcode = instructions[i]
        operand = instructions[i+1]

        #print(regA[0])

        match opcode:
            case 0: #adv
                numerator = regA[0]
                denominator = 2**get_combo(operand, regs)[0]
                regA[0] = int(numerator/denominator)
            case 1: #bxl
                regB[0] = regB[0] ^ operand
            case 2: #bst
                regB[0] = get_combo(operand, regs)[0] % 8
            case 3: #jnz
                if(regA[0] != 0):
                    i = operand
                    continue
            case 4: #bxc
                regB[0] = regB[0] ^ regC[0]
            case 5: #out
                #print(get_combo(operand, regs)[0], operand)
                outputs.append(get_combo(operand, regs)[0] % 8)
            case 6: #bdv
                numerator = regA[0]
                denominator = 2**get_combo(operand, regs)[0]
                regB[0] = int(numerator/denominator)
            case 7: #cdv
                numerator = regA[0]
                denominator = 2**get_combo(operand, regs)[0]
                regC[0] = int(numerator/denominator)

        i += 2

    return outputs

def testA(a_val, b_val, c_val, instructions):
    return testAs(a_val, a_val+1, b_val, c_val, instructions)

def testAs(a_start, a_end, b_val, c_val, instructions):
    for a_val in range(a_start, a_end):
        regA, regB, regC = [[a_val], [b_val], [c_val]]
        regs = [regA, regB, regC] 
        i = 0
        outputs = []
        while(i < len(instructions)-1):
            opcode = instructions[i]
            operand = instructions[i+1]

            match opcode:
                case 0: #adv
                    numerator = regA[0]
                    denominator = 2**get_combo(operand, regs)[0]
                    regA[0] = int(numerator/denominator)
                case 1: #bxl
                    regB[0] = regB[0] ^ operand
                case 2: #bst
                    regB[0] = get_combo(operand, regs)[0] % 8
                case 3: #jnz
                    if(regA[0] != 0):
                        i = operand
                        continue
                case 4: #bxc
                    regB[0] = regB[0] ^ regC[0]
                case 5: #out
                    outputs.append(get_combo(operand, regs)[0] % 8)
                    #if(regA[0] < 8):
                        #print("a_val", regA[0], outputs[-1], get_combo(operand, regs))

                    """ if(len(outputs) > len(instructions) or outputs[-1] != instructions[len(outputs)-1]):
                        break """
                case 6: #bdv
                    numerator = regA[0]
                    denominator = 2**get_combo(operand, regs)[0]
                    regB[0] = int(numerator/denominator)
                case 7: #cdv
                    numerator = regA[0]
                    denominator = 2**get_combo(operand, regs)[0]
                    regC[0] = int(numerator/denominator)

            i += 2
        
        #print(a_val, outputs)

        if(instructions == outputs):
            return outputs
    
    return outputs

def eval_oct(list_oct):
    string_oct = "".join(str(elem) for elem in list_oct)
    return int(string_oct, 8)

def part2(input):
    _, b_val, c_val = [int(reg) for reg in re.findall("\d+", input.split("\n\n")[0])]
    instructions = [int(ins) for ins in re.findall("\d+", input.split("\n\n")[1])]

    #print(instructions)

    current_a = [0]*(len(instructions))

    i = 0
    while i < len(instructions):
        j = 0
        while j < 8:
            current_a[i] = j
            a_val = eval_oct(current_a)
            result = testA(a_val, b_val, c_val, instructions)
            #print(a_val, current_a, result, i)
            if(len(result) == len(instructions) and result[-(i+1)] == instructions[-(i+1)]):
                break

            while(j == 7):
                current_a[i] = 0
                i -= 1
                j = current_a[i]
                
            j += 1
        
        i += 1

    return eval_oct(current_a)


    
print(part1(open("input17.txt", "r").read()))
print(part2(open("input17.txt", "r").read()))