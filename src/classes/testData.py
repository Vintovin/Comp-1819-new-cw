
class TestCase:

    # circle.radius = 0
    # circle.origin = (0,0)

    # line.a = 0
    # line.b = 0
    # line.c = 0

    def __init__(self, data):
        self.line = dict(a=0, b=0, c=0)
        self.circle = dict(radius=0, origin=(0, 0))
        self.circle["radius"] = data[0]
        self.circle["origin"] = (data[1], data[2])
        self.line["a"] = data[3]
        self.line["b"] = data[4]
        self.line["c"] = data[5]

    def get_data(self):
        print(self.circle)
        print(self.line)

