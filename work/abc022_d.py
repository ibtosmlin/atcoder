# https://atcoder.jp/contests/abc022/tasks/abc022_d
import numpy as np
from scipy.spatial import cKDTree


def min_nearest_dist(points):
    tree = cKDTree(points)
    min_dist = np.inf
    for point in points:
        ((d1, d2), _) = tree.query(point, k=2)
        if d1 == 0:
            d1 = d2
        min_dist = min(min_dist, d1)
    return min_dist


if __name__ == '__main__':
    N = int(input())
    pts1 = [[int(x) for x in input().split()] for _ in range(N)]
    pts2 = [[int(x) for x in input().split()] for _ in range(N)]

    print(min_nearest_dist(pts2) / min_nearest_dist(pts1))
