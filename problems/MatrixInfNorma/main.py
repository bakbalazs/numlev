#!/usr/bin/env python3


def main():
    matrix = list()
    n = int(input())
    result = list()
    for i in range(n):
        matrix.append(list(map(float, input().strip().split(" "))))

    for i in matrix:
        result.append(sum(list(map(abs, i))))

    print("{:.12f}".format(round(max(result), 8)))


if __name__ == '__main__':
    main()
