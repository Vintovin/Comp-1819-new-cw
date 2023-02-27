import math

def generate_circle_coordinates(radius, origin, line_start, line_end):
    x_coords = []
    y_coords = []
    for x in range(int((origin[0]-radius)*1000), int((origin[0]+radius)*1000)+1):
        x = x / 1000.0
        if abs(x - origin[0]) <= radius:
            y = origin[1] + math.sqrt(radius**2 - (x-origin[0])**2)
            x_coords.append(x)
            y_coords.append(y)
    for x in range(int((origin[0]+radius)*1000), int((origin[0]-radius)-1)*1000, -1):
        x = x / 1000.0
        if abs(x - origin[0]) <= radius:
            y = origin[1] - math.sqrt(radius**2 - (x-origin[0])**2)
            x_coords.append(x)
            y_coords.append(y)

    # Check if the line intercepts the circle
    dx = line_end[0] - line_start[0]
    dy = line_end[1] - line_start[1]
    intercepts = []
    for i in range(len(x_coords)):
        x = x_coords[i]
        y = y_coords[i]
        dist_to_line = abs(dy*x - dx*y + line_end[0]*line_start[1] - line_end[1]*line_start[0]) / math.sqrt(dx**2 + dy**2)
        if dist_to_line <= radius:
            intercept_x = x
            intercept_y = y
            delta_x = line_end[0] - line_start[0]
            delta_y = line_end[1] - line_start[1]
            t = ((intercept_x - line_start[0]) * delta_x + (intercept_y - line_start[1]) * delta_y) / (delta_x**2 + delta_y**2)
            if t >= 0 and t <= 1:
                intercepts.append((intercept_x, intercept_y))

    return (intercepts)

# Example usage
radius = 5
origin = (0, 0)
line_start = (-10, -10)
line_end = (10, 10)
intercepts = generate_circle_coordinates(radius, origin, line_start, line_end)
if len(intercepts) > 0:
    print("Line intercepts circle at:")
    for intercept in intercepts:
        print(f"({intercept[0]}, {intercept[1]})")
else:
    print("Line does not intercept circle")
