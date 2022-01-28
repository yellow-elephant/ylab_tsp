from math import sqrt

points = {
    'point1': [0, 2],
    'point2': [2, 5],
    'point3': [5, 2],
    'point4': [6, 6],
    'point5': [8, 3]}
start = 'point1'


def dist(a, b):
    d = [a[0] - b[0], a[1] - b[1]]
    return sqrt(d[0] * d[0] + d[1] * d[1])


def distances_matrix(points_cords):
    dm = {}
    for point1, cords1 in points_cords.items():
        dm[point1] = {}
        for point2, cords2 in points_cords.items():
            dm[point1][point2] = dist(cords1, cords2)
    return dm


if __name__ == '__main__':
