#!/usr/bin/env python3


def main():
    k, m, n = list(map(int, input().strip().split(" ")))

    A = list()
    B = list()

    for i in range(k):
        A.append(list(map(float, input().strip().split(' '))))

    for i in range(m):
        B.append(list(map(float, input().strip().split(' '))))

    result = [[0.0 for i in range(len(B[0]))] for j in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for u in range(len(A[0])):
                result[i][j] += A[i][u] * B[u][j]

    for i in range(len(result)):
        for j in range(len(result[0])):
            value = result[i][j]
            if int(value) == float(value):
                print(f"{result[i][j]:.0f} ")
            else:
                print(f"{result[i][j]:.12f} ")


if __name__ == '__main__':
    main()
