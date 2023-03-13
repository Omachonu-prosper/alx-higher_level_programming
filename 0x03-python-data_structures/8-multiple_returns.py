#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)

    sentence_length = len(sentence)
    first_char = sentence[0]

    return (sentence_length, first_char)
