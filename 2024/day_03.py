#!/usr/bin/env python3
# -*- coding: utf8 -*-

import re 

inputs = "2024/inputs/day_03.txt"

def parsing_data() -> list:
    datas = []
    with open(inputs, "r", encoding="UTF-8",) as f:
        data_input = f.readlines()
        for data in data_input:
            data = data.replace("\n", "")
            datas.append(data)
    return datas

def part_one(datas):
    pattern = r"mul\((\d+),(\d+)\)"
    result = 0
    for data in datas:
        matches = re.findall(pattern, data)
        for match in matches:
            result += int(match[0]) * int(match[1])
        # print(f"{matches=}")
    print(f"{result=}")


def part_two(datas):
    pattern = r"(don't\(\))|(do\(\))|mul\((\d+),(\d+)\)"
    do = True
    result = 0
    for data in datas:
        matches = re.findall(pattern, data)
        for match in matches:
            if match[0]:
                do = False
            if match[1]:
                do = True
            if match[2] and match[3] and do:
                result += int(match[2]) * int(match[3])
        # print(f"{matches=}")
    print(f"{result=}")

def part_two_2(datas):
    pattern = r"mul\((\d+),(\d+)\)"
    donts = []
    for data in datas:
        donts.append(data.split("don't()")[1:])
    dos = []
    for dont in donts:
        dos.append([phrase.split("do()")[1:] for phrase in dont])
    result = 0
    for data in datas:
        matches = re.findall(pattern, data.split("don't()")[:1][0])
        for match in matches:
            result += int(match[0]) * int(match[1])
    for do in dos:
        for do_list in do:
            matches = [re.findall(pattern, do_str) for do_str in do_list]
            for match in matches:
                result += sum(int(x) * int(y) for x, y in match)
    print(f"{result=}")

def main():
    datas = parsing_data()
    part_one(datas)
    part_two(datas)
    part_two_2(datas)

if __name__ == "__main__":
    main()
