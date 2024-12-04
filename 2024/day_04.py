#!/usr/bin/env python3
# -*- coding: utf8 -*-

import re 

inputs = "2024/inputs/day_04.txt"

def parsing_data() -> list:
    datas = []
    with open(inputs, "r", encoding="UTF-8",) as f:
        data_input = f.readlines()
        for data in data_input:
            data = data.replace("\n", "")
            datas.append(data)
    return datas

def part_one(datas):
    words = ("XMAS", "SAMX")
    n_rows = len(datas)
    n_cols = len(datas[0])
    result = [['.' for _ in range(n_cols)] for _ in range(n_rows)]

    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for row in range(n_rows):
        for col in range(n_cols):
            for dr, dc in directions:
                if 0 <= row + 3 * dr < n_rows and 0 <= col + 3 * dc < n_cols:
                    word = ''.join(datas[row + i * dr][col + i * dc] for i in range(4))
                    if word == "XMAS":
                        count += 1
    print(f"XMAS_{count=}")

def part_two(datas):
    n_rows = len(datas)
    n_cols = len(datas[0])

    count = 0
    directions = [((1, 1), (-1, -1)), ((1, -1), (-1, 1))]
    for row in range(n_rows):
        for col in range(n_cols):
            if datas[row][col] == 'A' and 0 < row < n_rows - 1 and 0 < col < n_cols - 1:
                word_cross = []
                for cross in directions:
                    word_cross.append(f"{datas[row + cross[0][0]][col + cross[0][1]]}A{datas[row + cross[1][0]][col + cross[1][1]]}")
                    cross_count = 0
                    for word in word_cross:
                        if word == "MAS" or word == "SAM":
                            cross_count += 1
                    if cross_count == 2:
                        count += 1


    print(f"XMAS_2_{count=}")



def main():
    datas = parsing_data()
    part_one(datas)
    part_two(datas)

if __name__ == "__main__":
    main()
