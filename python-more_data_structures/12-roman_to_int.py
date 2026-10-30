#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, last = 0, 0

    for c in reversed(roman_string):
        val = d.get(c, 0)
        if val < last:
            total -= val
        else:
            total += val
            last = val

    return total
