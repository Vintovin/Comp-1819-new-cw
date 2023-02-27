import random

runs = 500
radius_limit = 15

origin_upper = 15
origin_lower = -15

try:
    f = open("../data/generatedFile.txt", "r")
    existing = f.read()
    f.close()
except:
    print("New File to be created")

toadd = ""
for i in range(0, runs):
    radius = random.randint(1, radius_limit)
    origin_x = random.randint(origin_lower, origin_upper)
    origin_y = random.randint(origin_lower, origin_upper)

    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    newstring = f"{radius}, {origin_x}, {origin_y}, {a}, {b}, {c}\n"
    if newstring not in toadd or newstring not in existing:
        toadd = toadd + newstring

f = open("../data/generatedFile.txt", "w")
f.write(existing + toadd)
f.close()
