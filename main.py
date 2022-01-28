from math import sqrt

points = [
    [0, 2],
    [2, 5],
    [5, 2],
    [6, 6],
    [8, 3]]


def dist(a, b):
    d = [a[0] - b[0], a[1] - b[1]]
    return sqrt(d[0] * d[0] + d[1] * d[1])


def distances_matrix(points_cords):
    dm = []
    i = 0
    while i < len(points_cords):
        dm_line = []
        a = points_cords[i]
        for b in points_cords:
            dm_line.append(dist(a, b))
        dm.append(dm_line)
        i += 1
    return dm


if __name__ == '__main__':
    for line in distances_matrix(points):
        print(line)
