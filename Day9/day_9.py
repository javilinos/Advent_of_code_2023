import numpy as np
from dataclasses import dataclass


def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def generateDifferences(sequence: list[int]):
    res = []
    for i, number in enumerate(sequence):
        if (i != len(sequence) - 1):
            res.append(sequence[i+1] - number)
    if all(value == 0 for value in res):
        return sequence[-1]
    return sequence[-1] + generateDifferences(res)


def generateDifferencesFirst(sequence: list[int]):
    res = []
    for i, number in enumerate(sequence):
        if (i != len(sequence) - 1):
            res.append(number - sequence[i+1])
    if all(value == 0 for value in res):
        return sequence[0]
    return sequence[0] + generateDifferencesFirst(res)


if __name__ == "__main__":
    lines = readLines("input.txt")
    for i, line in enumerate(lines):
        lines[i] = [int(number.replace('\n', '')) for number in line.split()]
    sum = 0
    for line in lines:
        sum += generateDifferences(line)

    print(f"part1: {sum}")

    sum = 0
    for line in lines:
        sum += generateDifferencesFirst(line)

    print(f"part2: {sum}")


