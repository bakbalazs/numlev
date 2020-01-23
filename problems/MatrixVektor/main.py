#!/usr/bin/env python3
from functools import reduce


def main():
    matrix = list()
    vector = list()
    w = list()
    m, n = list(map(int, input().strip().split(" ")))

    for i in range(m):
        matrix.append(list(map(float, input().strip().split(" "))))

    for i in range(n):
        vector.append(float(input()))

    for i in range(len(matrix)):
        w.append(reduce(lambda x, y: x + y, map(lambda x, y: x * y, matrix[i], vector)))

    for i in w:
        print("{:.12f}".format(i))


if __name__ == '__main__':
    main()
