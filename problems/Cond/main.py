#!/usr/bin/env python3


def main():
    n = int(input())
    A = list()
    normInfA = list()
    normInfR = list()
    norm1A = list()
    norm1R = list()
    R = list()

    for i in range(n):
        A.append(list(map(float, input().strip().split(' '))))

    for _ in range(n):
        li = list()
        for _ in range(n * 2):
            li.append(0.0)
        R.append(li)

    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j]

    for i in range(n):
        for j in range(n, n * 2):
            if i == (j - n):
                R[i][j] = 1

    for i in range(n):
        while R[i][i] == 0:
            R[i], R[i + 2] = R[i + 2], R[i]
        t = R[i][i]
        for j in range(i, 2 * n):
            R[i][j] = R[i][j] / t
        for j in range(n):
            if i != j:
                t = R[j][i]
                for k in range(2 * n):
                    R[j][k] -= t * R[i][k]

    for i in range(n * n):
        R[int(i / n)].pop(0)

    for i in A:
        normInfA.append(sum(list(map(abs, i))))

    for i in R:
        normInfR.append(sum(list(map(abs, i))))

    for i in zip(*A):
        norm1A.append(sum(list(map(abs, i))))

    for i in zip(*R):
        norm1R.append(sum(list(map(abs, i))))

    res_inf = max(normInfA) * max(normInfR)
    res_one = max(norm1A) * max(norm1R)
    print('{:.12f} {:.12f}'.format(round(res_inf, 12), round(res_one, 12)))


if __name__ == '__main__':
    main()
