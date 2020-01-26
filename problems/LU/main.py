#!/usr/bin/env python3


def main():
    n = int(input())
    A = list()

    for i in range(n):
        A.append(list(map(float, input().strip().split(' '))))

    try:
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                res = (A[j][i] / A[i][i]) * -1
                for k in range(i, len(A)):
                    A[j][k] = A[j][k] + (res * A[i][k])
                A[j][i] = res * -1
    except ZeroDivisionError as e:
        print("fail")
    else:
        for i in range(len(A)):
            for j in range(len(A[0])):
                print("{:.12f}".format(A[i][j]))


if __name__ == '__main__':
    main()
