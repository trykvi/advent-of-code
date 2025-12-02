import re
from PIL import Image
import numpy as np

def find_position_after_seconds(robot, seconds, width, height):
    #print(robot)
    robot_match = re.match("p=(.+),(.+) v=(.+),(.+)", robot)
    x0 = int(robot_match[1])
    y0 = int(robot_match[2])
    v_x = int(robot_match[3])
    v_y = int(robot_match[4])

    x = (x0 + v_x * seconds) % width
    y = (y0 + v_y * seconds) % height

    return (x, y)

def safety_factor(robots, width, height):
    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0

    for robot in robots:
        x = robot[0]
        y = robot[1]
        if(x < width//2 and y < height//2):
            quad1 += 1
        elif(x > width//2 and y < height//2):
            quad2 += 1
        elif(x < width//2 and y > height//2):
            quad3 += 1
        elif(x > width//2 and y > height//2):
            quad4 += 1


    return quad1 * quad2 * quad3 * quad4


def part1(input):
    robots = input.split("\n")[:-1]

    robot_end_positions = []

    for robot in robots:
        x, y = find_position_after_seconds(robot, 100, 101, 103)
        robot_end_positions.append((x, y))

    #print(robot_end_positions)

    return safety_factor(robot_end_positions, 101, 103)


def print_robots_map(robots, width, height):
    robots_map = [["." for _ in range(width)] for _ in range(height)]
    for robot in robots:
        x = robot[0]
        y = robot[1]
        if(robots_map[y][x] == "."):
            robots_map[y][x] = "1"
        else:
            robots_map[y][x] = str(int(robots_map[y][x]) + 1)

    for line in robots_map:
        print("".join(line))

def create_image(robots, width, height, seconds):
    #robots_map = [[255 for _ in range(width)] for _ in range(height)]
    robots_map = np.full((height, width), 255, dtype=np.uint8)
    for robot in robots:
        x = robot[0]
        y = robot[1]
        robots_map[y][x] = 0

    img = Image.fromarray(robots_map, mode='L')
    return img
    #img.save(f"./images/{seconds}.png")
         

def part2(input):
    robots = input.split("\n")[:-1]

    width = 101
    height = 103

    results = []

    for seconds in range(10403):

        robot_end_positions = []

        for robot in robots:
            x, y = find_position_after_seconds(robot, seconds, width, height)
            robot_end_positions.append((x, y))

        #print_robots_map(robot_end_positions, width, height)
        safety_fac = safety_factor(robot_end_positions, width, height)
        img = create_image(robot_end_positions, width, height, seconds)
        results.append((safety_fac, img, seconds))

    sorted_results = sorted(results, key=lambda tup: tup[0])

    for result in sorted_results[:50]:
        result[1].save(f"./images/{result[0]}_{result[2]}.png")
    


    


print(part1(open("input14.txt", "r").read()))
part2(open("input14.txt", "r").read())