from math import sqrt
from itertools import permutations

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

    min_path_length = 0
    min_path = ()
    dm = distances_matrix(points)
    transitional_points = points.copy()
    transitional_points.pop(start)
    transitional_paths = permutations(transitional_points.keys(), len(transitional_points))

    for path in transitional_paths:
        path = (start,) + path + (start,)
        path_length = 0
        i = 0
        while i < len(path) - 1:
            point1 = path[i]
            point2 = path[i + 1]
            path_length += dm[point1][point2]
            i += 1
        if min_path_length == 0 or path_length < min_path_length:
            min_path_length = path_length
            min_path = path

    print(min_path_length)
    print(min_path)

