import math
import src.plotdata

def circle_y_coordinates(x, origin, radius):
    h, k = origin
    y1 = k + math.sqrt(radius ** 2 - (x - h) ** 2)
    y2 = k - math.sqrt(radius ** 2 - (x - h) ** 2)
    return y1, y2

def line_y_coordinates(x,a,b,c):
    # y = ax + c
    # ax + b - c = 0
    y = (a*x) + b
    return y

def solution(testData):
    #print(testData.circle)
    circle_origin = (int(testData.circle["origin"][0]), int(testData.circle["origin"][1]))
    x_limit_lower = int(circle_origin[0]) - int(testData.circle["radius"])
    x_limit_upper = int(circle_origin[0]) + int(testData.circle["radius"])
    matches = []
    line_a = int(testData.line["a"])
    line_b = int(testData.line["b"])
    line_c = int(testData.line["c"])

    step = 0.001
    for i in range(x_limit_lower*1000, (x_limit_upper*1000)+1):
        x = round(i * step, 3)
        #print(x)
        circle_y = x
        # do something with x

        y1, y2 = circle_y_coordinates(x, circle_origin, int(testData.circle["radius"]))
        #y = mx+c
        y = round(line_y_coordinates(x, line_a, line_b, line_c),3)

        # Print the result

        if round(y1,3) == y:
            #print("match")
            matches.append((x, y))
            # print(f"At x = {round(x, 3)}, the y-coordinate of the line is {y}.")
            # print(f"At x = {round(x, 3)}, the y-coordinates of the circle are {round(y1, 3)} and {round(y2, 3)}.")
        if round(y2,3) == y:
            #print("match")
            matches.append((x, y))
            # print(f"At x = {round(x, 3)}, the y-coordinate of the line is {y}.")
            # print(f"At x = {round(x, 3)}, the y-coordinates of the circle are {round(y1, 3)} and {round(y2, 3)}.")
    #print(testData.line)
    #print(matches)

    return matches










