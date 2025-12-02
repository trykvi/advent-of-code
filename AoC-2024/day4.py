import numpy as np
import re

def get_diagonals(matrix):
    diagonals = []
    for i in range(2*len(matrix) - 1):
        diagonal = ""
        for j in range(i+1):
            if(i-j >= len(matrix) or j >= len(matrix)):
                continue
            x = i-j
            y = j
            diagonal += matrix[y][x]

        diagonals.append(diagonal)

    return diagonals


def part1(input):
    matrix = np.char.array([np.char.array(list(line)) for line in input.split("\n")[:-1]])
    tr_matrix = np.transpose(matrix)


    searchspace = ["".join(line) for line in matrix]
    searchspace += ["".join(line) for line in tr_matrix]
    searchspace += get_diagonals(matrix)
    searchspace += get_diagonals(np.flip(matrix, 1))

    result = 0

    for line in searchspace:
        result += len(re.findall("(?=(XMAS))|(?=(SAMX))", line))

    print(result)

def conv2d_count(mask, matrix):
    mask_delta = (len(mask)-1)//2
    matches = 0
    for y in range(mask_delta, len(matrix)-mask_delta):
        for x in range(mask_delta, len(matrix)-mask_delta):
            is_match = True
            for m_y in range(len(mask)):
                for m_x in range(len(mask)):
                    if(mask[m_y][m_x] == "."):
                        continue
                    if(mask[m_y][m_x] != matrix[y+(m_y-mask_delta)][x+(m_x-mask_delta)]):
                        is_match = False
            if(is_match):
                matches+=1
    
    return matches

            


def part2(input):
    matrix = np.char.array([np.char.array(list(line)) for line in input.split("\n")[:-1]])
    masks = [
        np.char.array([list("M.M"),
                        list(".A."),
                        list("S.S")]),
        np.char.array([list("S.S"),
                        list(".A."),
                        list("M.M")]),
        np.char.array([list("M.S"),
                        list(".A."),
                        list("M.S")]),
        np.char.array([list("S.M"),
                        list(".A."),
                        list("S.M")])
    ]

    result = 0
    for mask in masks:
        result += conv2d_count(mask, matrix)
    
    print(result)


part1(open("input4.txt", "r").read())
part2(open("input4.txt", "r").read())