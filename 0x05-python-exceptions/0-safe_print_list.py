#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    my_index = 0

    while my_index < x:
        try:
            print("{}".format(my_list[my_index]), end="")
            my_index += 1
        except IndexError:
            break

    print()
    return(my_index)
