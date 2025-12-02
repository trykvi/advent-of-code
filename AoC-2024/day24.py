import re

def eval_expression(val1, val2, operation):
    if(operation == "AND"):
        return (val1 and val2)
    elif(operation == "XOR"):
        return (val1 != val2)
    elif(operation == "OR"):
        return (val1 or val2)

def part1(input):
    gates = dict()
    for gate in input.split("\n\n")[0].split("\n"):
        gates[gate.split(": ")[0]] = bool(int(gate.split(" ")[1]))


    operations = [line.replace(" ->", "").split(" ") for line in input.split("\n\n")[1].split("\n")[:-1]]

    max_z = 0
    for operation in operations:
        if(operation[3][0] == 'z'):
            max_z = max(max_z, int(operation[3][1:]))

    did_not_change = False
    binary_number = [None]*(max_z+1)
    result_strings = [None]*(max_z+1)
    while(not did_not_change):
        did_not_change = True
        for operation in operations:
            if operation[0] in gates and operation[2] in gates and operation[3] not in gates:
                did_not_change = False
                gates[operation[3]] = eval_expression(gates[operation[0]], gates[operation[2]], operation[1])
                if(operation[3][0] == 'z'):
                    binary_number[max_z - int(operation[3][1:])] = str(int(gates[operation[3]]))
                    result_strings[max_z - int(operation[3][1:])] = operation[3]+": "+str(int(gates[operation[3]]))

    result = int("".join(binary_number), 2)

    #print(" ".join(reversed(result_strings)))

    return result

def calc_z(gates, max_z):
    binary_number = [None]*(max_z+1)
    for gate in gates.keys():
        if(gate[0] == "z"):
            binary_number[max_z - int(gate[1:])] = str(int(gates[gate]))

    return int("".join(binary_number), 2)

class Expression:
    def __init__(self, e1, operation=None, e2=None, constant=False):
        self.constant = constant
        self.e1 = e1
        self.operation = operation
        self.e2 = e2


    def eval(self):
        if(self.constant):
            return self.e1
        else:
            return eval_expression(self.e1.eval(), self.e2.eval(), self.operation)

    def swap(self, other):
        temp_e1 = self.e1
        temp_e2 = self.e2

        self.e1 = other.e1
        self.e2 = other.e2
        other.e1 = temp_e1
        other.e2 = temp_e2


def swap(gate1, gate2, reverse_map, forward_map):
    reverse_map[gate1], reverse_map[gate2] = reverse_map[gate2], reverse_map[gate1]
    forward_map[reverse_map[gate1]], forward_map[reverse_map[gate2]] = forward_map[reverse_map[gate2]], forward_map[reverse_map[gate1]]


def part2(input):
    XOR = 'XOR'
    AND = 'AND'
    OR = 'OR'

    gate_map = {}
    reverse_gate_map = {}
    minmax = lambda _a, _b: (_a, _b) if _a <= _b else (_b, _a)
    for line in input.split('\n\n')[1].splitlines():
        a, op, b, _, c = line.split()
        a, b = minmax(a, b)
        gate_map[a, b, op] = c
        reverse_gate_map[c] = a, b, op

    
    modified_gates = set()
    c = ''
    for i in range(int(max(reverse_gate_map)[1:])):
        x = f'x{i:02}'
        y = f'y{i:02}'
        z = f'z{i:02}'
        zn = f'z{i + 1:02}'
        xor_result = gate_map[x, y, XOR]
        and_result = gate_map[x, y, AND]
        if not c:
            c = and_result
        else:
            a, b = minmax(c, xor_result)
            gate_key = a, b, XOR
            if gate_key not in gate_map:
                a, b = list(set(reverse_gate_map[z][:2]) ^ set(gate_key[:2]))
                modified_gates.add(a)
                modified_gates.add(b)
                swap(a, b, reverse_gate_map, gate_map)
            elif gate_map[gate_key] != z:
                modified_gates.add(gate_map[gate_key])
                modified_gates.add(z)
                swap(z, gate_map[gate_key], reverse_gate_map, gate_map)
            gate_key = reverse_gate_map[z]
            xor_result = gate_map[x, y, XOR]
            and_result = gate_map[x, y, AND]
            c = gate_map[*minmax(c, xor_result), AND]
            c = gate_map[*minmax(c, and_result), OR]

    return ','.join(sorted(modified_gates))

    


print(part1(open("input24.txt", "r").read()))
print(part2(open("input24.txt", "r").read()))
