#!/usr/bin/env python3


def main():
    result = list()
    d = int(input())
    v = list(map(float, input().strip().split(" ")))
    w = list(map(float, input().strip().split(" ")))

    for i in range(d):
        result.append(v[i] * w[i])

    print("{:.12f}".format(round(sum(result), 8)))


if __name__ == '__main__':
    main()
