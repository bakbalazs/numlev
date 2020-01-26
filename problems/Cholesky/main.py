#!/usr/bin/env python3

import math


def choleskyFelbontas(A):
    L = [[0.0] * len(A) for _ in range(len(A))]

    for i, (Ai, Li) in enumerate(zip(A, L)):
        for j, Lj in enumerate(L[:i + 1]):
            s = sum(Li[k] * Lj[k] for k in range(j))
            try:
                Li[j] = math.sqrt(Ai[i] - s) if (i == j) else \
                    (1.0 / Lj[j] * (Ai[j] - s))
            except ZeroDivisionError:
                L = "fail"
                return L
    return L


def main():
    n = int(input())

    A = []
    for i in range(n):
        line = list(map(float, input().strip().split(' ')))
        for j in range(n - 1 - i):
            line.append(float(0.0))

        A.append(line)

    res = choleskyFelbontas(A)

    if type(res) == str:
        print("fail")
    elif res[-1][-1] <= 0.0:
        print("fail")
    else:
        for i in range(n):
            for j in range(n):
                print("{:.12f}".format(res[i][j]))


if __name__ == '__main__':
    main()
