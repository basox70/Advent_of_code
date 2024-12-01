#!/usr/bin/env python3
# -*- coding: utf8 -*-

import re 

inputs = "2024/inputs/day_1.txt"


def parsing_data():
    left, right = [], []
    pattern = r"^([\d]*)\s*([\d]*)"
    left, right = [], []
    with open(inputs, "r", encoding="UTF-8") as f:
        data_input = f.readlines()
        for data in data_input:
            match = re.match(pattern, data)
            if match:
                left.append(int(match.group(1)))
                right.append(int(match.group(2)))
    left.sort()
    right.sort()

    return left, right

def part_one(left, right):
    total_distance = 0
    for i in range(len(left)):
        distance = left[i] > right[i] and left[i] - right[i] or right[i] - left[i]
        total_distance += distance

    print(f"{total_distance=}")

def part_two(left, right):
    similarity_score = 0
    for i in left:
        similarity_score += i * right.count(i)
    
    print(f"{similarity_score=}")

def main():
    left, right = parsing_data()
    part_one(left, right)
    part_two(left, right)

if __name__ == "__main__":
    main()
