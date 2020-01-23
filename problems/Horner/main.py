#!/usr/bin/env python3


def main():
    n = int(input())
    p = list(map(float, input().strip().split(' ')))
    m = int(input())
    x = list()

    for i in range(0, m):
        x.append(float(input()))

    for i in x:
        result = p[0]
        for j in range(1, len(p)):
            result = result * i + p[j]
        print("{:.12f}".format(result))


if __name__ == '__main__':
    main()
