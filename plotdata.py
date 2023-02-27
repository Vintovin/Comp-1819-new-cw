from matplotlib import pyplot as plt

class plot:
    c_points = []
    l_points = []

    def __init__(self):
        print("Ready")

    def add_c_point(self, tup_points):
        self.c_points.append((tup_points[0], tup_points[1]))

    def add_l_point(self, tup_points):
        self.l_points.append((tup_points[0], tup_points[1]))

    def plot(self):
        for i in self.c_points:
            plt.plot(i[0], i[1], '.')

        for i in self.l_points:
            plt.plot(i[0], i[1], '.')

        plt.show()
