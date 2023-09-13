#!/usr/bin/python3

def number_keys(a_dictionary):
    num = 0
    list_dic = list(a_dictionary.keys())

    for i in list_dic:
        num += 1
    return (num)
