#!/usr/bin/python3

def to_subt(list_num):
    to_sub = 0
    max_list = max(list_num)

    for i in list_num:
        if max_list > i:
            to_sub += i
    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    romanin = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(romanin)

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for num in list_keys:
            if num == ch:
                if romanin.get(ch) <= last_rom:
                    num += to_subt(list_num)
                    list_num = [romanin.get(ch)]
                else:
                    list_num.append(romanin.get(ch))
                last_rom = romanin.get(ch)
        num += to_subt(list_num)
        return (num)
