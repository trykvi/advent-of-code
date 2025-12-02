import re

numpad_coords = {'A': (2, 3),
                 '0': (1, 3),
                 '1': (0, 2),
                 '2': (1, 2),
                 '3': (2, 2),
                 '4': (0, 1),
                 '5': (1, 1),
                 '6': (2, 1),
                 '7': (0, 0),
                 '8': (1, 0),
                 '9': (2, 0),}

arrowpad_coords = {'A': (2, 0),
                   '^': (1, 0),
                   '<': (0, 1),
                   'v': (1, 1),
                   '>': (2, 1)}

def shortest_paths_from_to(startpos, endpos, keypad):
    paths = [[startpos]]
    keys_to_type = [[]]

    """ if(startpos == endpos):
        return [['A']] """

    while paths[0][-1] != endpos:
        new_paths = []
        new_keys_to_type = []

        for i in range(len(paths)):
            pos = paths[i][-1]

            for adjpos in keypad[pos]:
                if(abs(pos[0] - endpos[0]) > abs(adjpos[0] - endpos[0]) or
                   abs(pos[1] - endpos[1]) > abs(adjpos[1] - endpos[1])):

                    new_paths.append(paths[i] + [adjpos])
                    new_keys_to_type.append(keys_to_type[i].copy())

                    if(adjpos[1] < pos[1]):
                        new_keys_to_type[-1] += '^'
                    elif(adjpos[0] > pos[0]):
                        new_keys_to_type[-1] += '>'
                    elif(adjpos[1] > pos[1]):
                        new_keys_to_type[-1] += 'v'
                    elif(adjpos[0] < pos[0]):
                        new_keys_to_type[-1] += '<'

        paths = new_paths
        keys_to_type = new_keys_to_type

    return [''.join(keys) + 'A' for keys in keys_to_type]

def find_permutations_from(i, segmented_paths):
    if(i == len(segmented_paths) - 1):
        return segmented_paths[i]
    else:
        result = []
        next_result = find_permutations_from(i+1, segmented_paths)
        for segment in segmented_paths[i]:
            for combined_segment in next_result:
                result.append(segment + combined_segment)

        return result

def shortest_paths_to_type(code, keypad, type):
    code = 'A' + code
    segmented_paths = []

    for i in range(len(code)-1):
        if(type == 'number'):
            path_segments = shortest_paths_from_to(numpad_coords[code[i]], numpad_coords[code[i+1]], keypad)
        elif(type == 'arrow'):
            path_segments = shortest_paths_from_to(arrowpad_coords[code[i]], arrowpad_coords[code[i+1]], keypad)

        segmented_paths.append(path_segments)

    return find_permutations_from(0, segmented_paths)

def replace_with_coords(dict1, mapdict):
    converted_dict = {}

    for key in dict1.keys():
        converted_dict[mapdict[key]] = []

        for elem in dict1[key]:
            converted_dict[mapdict[key]].append(mapdict[elem])

    return converted_dict

def get_numeric_part(code):
    return int(re.findall('[0-9]+', code)[0])

def part1(input):
    codes = input.split("\n")[:-1]

    numpad = {'A': ['0', '3'],
              '0': ['A', '2'],
              '1': ['4', '2'],
              '2': ['0', '1', '3', '5'],
              '3': ['A', '2', '6'],
              '4': ['1', '5', '7'],
              '5': ['2', '4', '6', '8'],
              '6': ['3', '5', '9'],
              '7': ['4', '8'],
              '8': ['5', '7', '9'],
              '9': ['6', '8']
              }

    arrowpad = {'A': ['^', '>'],
                '^': ['A', 'v'],
                '<': ['v'],
                'v': ['<', '^', '>'],
                '>': ['v', 'A']
                }

    coord_numpad = replace_with_coords(numpad, numpad_coords)
    coord_arrowpad = replace_with_coords(arrowpad, arrowpad_coords)

    result = 0

    for code in codes:

        min_length = 999_999_999
        best_entry = ""

        robot1_entries = shortest_paths_to_type(code, coord_numpad, 'number')

        for rob1entry in robot1_entries:
            robot2_entries = shortest_paths_to_type(rob1entry, coord_arrowpad, 'arrow')

            for rob2entry in robot2_entries:
                robot3_entries = shortest_paths_to_type(rob2entry, coord_arrowpad, 'arrow')

                for rob3entry in robot3_entries:
                    if(len(rob3entry) < min_length):
                        min_length = len(rob3entry)
                        best_entry = rob3entry

        result += get_numeric_part(code) * min_length
        #print(code, get_numeric_part(code), ': ', best_entry)

    return result

memo = dict()

prev_letters = [""]*26
def get_final_code_length(code, num_robots, keypad, is_beginning, just_split=False):
    if(len(code) > 2):
        result = 0
        for i in range(len(code) - 1):
            if code[i] == code[i+1]:
                result += 1
            else:
                if(i == 0 and is_beginning):
                    result += get_final_code_length(code[i] + code[i+1], num_robots, keypad, True, True)
                else:
                    result += get_final_code_length(code[i] + code[i+1], num_robots, keypad, False, True)

        #print(num_robots, code, result, is_beginning)
        return result
    if((code, num_robots, is_beginning, "".join(prev_letters[:(num_robots+1)])) not in memo):
        min_length = 999_999_999_999
        #min_path = None
        min_paths = shortest_paths_from_to(arrowpad_coords[code[0]], arrowpad_coords[code[1]], keypad)
        if(num_robots == 1):
            result = len(min_paths[0])
            #print("test", result)
        else:
            #print(min_paths, code)
            for path in min_paths:
                final_code_length = 0
                if(is_beginning):
                    path = 'A' + path
                final_code = ''
                for i in range(len(path) - 1):
                    if path[i] == path[i+1]:
                        if(i == 0 and is_beginning):
                            final_code_length += get_final_code_length(path[i], num_robots-1, keypad, True)
                        elif(i == 0):
                            final_code_length += get_final_code_length(prev_letters[num_robots] + path[i], num_robots-1, keypad, True)
                        final_code_length += 1
                    else:
                        if(i == 0 and is_beginning):
                            final_code_length += get_final_code_length(path[i] + path[i+1], num_robots-1, keypad, True)
                        elif(i == 0):
                            final_code_length += get_final_code_length(prev_letters[num_robots] + path[i] + path[i+1], num_robots-1, keypad, False)
                        else:
                            final_code_length += get_final_code_length(path[i] + path[i+1], num_robots-1, keypad, False)


                        #print(i, final_code, num_robots, 'aa')
                if(final_code_length < min_length):
                    min_path = path
                    min_length = final_code_length

            result = min_length
            prev_letters[num_robots] = min_path[-1]
        #print(num_robots, code, result, is_beginning)
        memo[(code, num_robots, is_beginning, "".join(prev_letters[:(num_robots+1)]))] = result
    return memo[(code, num_robots, is_beginning, "".join(prev_letters[:(num_robots+1)]))]

def part2(input):
    codes = input.split("\n")[:-1]

    numpad = {'A': ['0', '3'],
              '0': ['A', '2'],
              '1': ['4', '2'],
              '2': ['0', '1', '3', '5'],
              '3': ['A', '2', '6'],
              '4': ['1', '5', '7'],
              '5': ['2', '4', '6', '8'],
              '6': ['3', '5', '9'],
              '7': ['4', '8'],
              '8': ['5', '7', '9'],
              '9': ['6', '8']
              }

    arrowpad = {'A': ['^', '>'],
                '^': ['A', 'v'],
                '<': ['v'],
                'v': ['<', '^', '>'],
                '>': ['v', 'A']
                }

    coord_numpad = replace_with_coords(numpad, numpad_coords)
    coord_arrowpad = replace_with_coords(arrowpad, arrowpad_coords)

    result = 0

    #return get_final_code_length("A>A", 2, coord_arrowpad, True)

    for code in codes:

        min_length = 999_999_999_999_999_999

        robot1_entries = shortest_paths_to_type(code, coord_numpad, 'number')
        #best_path = ''
        for rob1entry in robot1_entries:
            #rob1entry = "<v<A>^>A<A>AvA<^AA>A<vAAA^>A"
            final_code_length = get_final_code_length("A" + rob1entry, 25, coord_arrowpad, True)
            if(final_code_length < min_length):
                min_length = final_code_length
                #best_path = final_code_length
        
        #print(best_path)

        print(code, min_length)
        
        result += get_numeric_part(code) * min_length
        #print(min_length)


    return result


print(part1(open('input21.txt', 'r').read()))
print(part2(open('input21.txt', 'r').read()))