import numpy as np
import re

def get_matrices(input, adjustment):
    A_line, B_line, prize_line = input.split("\n")

    a1, a2 = re.findall("\d+", A_line)
    b1, b2 = re.findall("\d+", B_line)
    ans1, ans2 = re.findall("\d+", prize_line)

    A = np.array([[int(a1), int(b1)],
                   [int(a2), int(b2)]])
    ans = np.array([int(ans1) + adjustment, int(ans2) + adjustment])

    return A, ans

def part1(input):
    answerstrings=input.split("\n\n")

    result = 0

    for line in answerstrings:
        A, B = get_matrices(line, 0)

        a_presses, b_presses = np.linalg.solve(A, B)

        if(abs(round(a_presses) - a_presses) < 0.00001 and abs(round(b_presses) - b_presses) < 0.00001):
            result += round(a_presses)*3 + round(b_presses)

    return result

def part2(input):
    answerstrings=input.split("\n\n")

    result = 0

    for line in answerstrings:
        A, B = get_matrices(line, 10000000000000)

        a_presses, b_presses = np.linalg.solve(A, B)

        if(abs(round(a_presses) - a_presses) < 0.01 and abs(round(b_presses) - b_presses) < 0.01):
            result += round(a_presses)*3 + round(b_presses)

    return result

    


print(part1(open("input13.txt", "r").read()))
print(part2(open("input13.txt", "r").read()))

