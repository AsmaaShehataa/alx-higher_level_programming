#!/usr/bin/python3
"""Text Indentation"""


def text_indentation(text):
    """
    unction that prints a text with 2 new lines
    """
    if isinstance(text, str) is False:
        raise TypeError('text must be a string')
    TT_punc = text.replace('.', '.\n\n')
    TT_punc = TT_punc.replace('?', '?\n\n')
    TT_punc = TT_punc.replace(':', ':\n\n')
    Nline = TT_punc.split('\n')

    for line in range(len(Nline)):
        print("{}".format(Nline[line].strip()),
              end=("" if (line == (len(Nline) - 1)) else '\n'))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
