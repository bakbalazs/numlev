#!/usr/bin/env python3
import numpy as np

def main():

    matrix = []
    for i in range(2):
        a = []
        line_num = list(map(float, input().strip().split(' ')))
        for j in line_num:
            a.append(j)
        matrix.append(a)

    print("{:.12f}".format(np.linalg.norm(matrix, 2)))


if __name__ == '__main__':
    main()