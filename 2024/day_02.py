#!/usr/bin/env python3
# -*- coding: utf8 -*-

import re 

inputs = "2024/inputs/day_02.txt"

def parsing_data() -> list[list]:
    reports = []
    with open(inputs, "r", encoding="UTF-8",) as f:
        data_input = f.readlines()
        for data in data_input:
            data = data.replace("\n", "")
            reports.append([int(i) for i in data.split(" ")])
    return reports


def part_one(reports:list[list]):
    total_safe = 0
    for levels in reports:
        print(f"{levels=} | {reports.index(levels)+1}/{len(reports)}")
        differences = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
        print(f"{differences=}")
        if (max(differences) > 0 and min(differences) > 0) or (max(differences) < 0 and min(differences) < 0):
            abs_diff = [abs(i) for i in differences]
            print(f"{abs_diff=}")
            if (max(abs_diff) <= 3 and min(abs_diff) >= 1):
                print("Safe!")
                total_safe += 1
        
        print(f"levels {total_safe=}")
        print("="*50)

    print(f"{total_safe=}")
    
    print("="*50)
    print("="*50)
    print("="*50)

def part_two(reports:list[list]):
    total_safe = 0

    def is_safe(levels) -> bool:
        print(f"new_{levels=}")
        differences = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
        print(f"{differences=}")
        if (max(differences) > 0 and min(differences) > 0) or (max(differences) < 0 and min(differences) < 0):
            abs_diff = [abs(i) for i in differences]
            print(f"{abs_diff=}")
            if (max(abs_diff) <= 3 and min(abs_diff) >= 1):
                print("Safe!")
                return True
        return False
        
    for levels in reports:
        print(f"{levels=} | {reports.index(levels)+1}/{len(reports)}")
        if is_safe(levels):
            total_safe += 1
            print(f"levels {total_safe=}")
            continue
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i+1:]
            if is_safe(new_levels):
                total_safe += 1

        print(f"levels {total_safe=}")
        print("="*50)

    print(f"{total_safe=}")


def is_safe_with_one_removal(levels):
    # Fonction pour vérifier si une suite est "Safe" sans suppression
    def is_safe(levels):
        increasing = all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1))
        decreasing = all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))
        return (increasing or decreasing) and all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

    # Vérification directe si la suite est déjà "Safe"
    if is_safe(levels):
        return True

    # Vérification en supprimant un élément à chaque position
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    
    return False

def count_safe_suites(suites):
    return sum(1 for suite in suites if is_safe_with_one_removal(suite))

def main():
    reports = parsing_data()
    part_one(reports)
    part_two(reports)

    results_with_removal = {tuple(suite): is_safe_with_one_removal(suite) for suite in reports}
    safe_count = count_safe_suites(reports)
    print(f"{results_with_removal=}")
    print(f"{safe_count=}")



if __name__ == "__main__":
    main()
