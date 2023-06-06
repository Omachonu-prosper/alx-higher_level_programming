#!/usr/bin/python3

"""Text indentation"""


def text_indentation(text):
    """Text indentition function
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print('{}\n'.format(text[i]))
        elif not (text[i] == ' ' and text[i - 1] in ['.', '?', ':', ' ']):
            print(text[i], end='')
