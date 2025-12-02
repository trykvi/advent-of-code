import itertools
import concurrent.futures

def eval(equation):
    result = 0
    operation = '+'
    for i in range(len(equation)):
        if(i % 2 == 0):
            if(operation == '+'):
                result += int(equation[i])
            elif(operation == '*'):
                result *= int(equation[i])
            elif(operation == '||'):
                result = int(str(result) + equation[i])
        else:
            operation = equation[i]

    return result
            

def test_equation(equation, operators):
    result = int(equation.split(": ")[0])
    elements = equation.split(": ")[1].split(" ")

    permutations = list(itertools.product(operators, repeat=len(elements)-1))

    for permutation in permutations:
        operation = elements + list(permutation)
        operation[::2] = elements
        operation[1::2] = list(permutation)

        this_result = eval(operation)
        if(this_result == result):
            return this_result

    
    return 0






def part1(input):
    equations = input.split("\n")[:-1]
    result = 0
    operators = ["*", "+"]
    for equation in equations:
        result += test_equation(equation, operators)

    return result

def part2(input):
    equations = input.split("\n")[:-1]
    result = 0
    operators = ["*", "+", "||"]

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=24)

    submit = {executor.submit(test_equation, equation, operators): equation for equation in equations}

    for future in concurrent.futures.as_completed(submit):
        result += future.result()

    return result

print(part1(open("input7.txt", "r").read()))
print(part2(open("input7.txt", "r").read()))

