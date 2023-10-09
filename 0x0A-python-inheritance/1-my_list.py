#!/usr/bin/python3

"""
contains MyList class 
"""



class MyList(list):
    """a subclass of the list"""
    def __init__(self):
        """object initializing"""
        super().__init__()



    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
