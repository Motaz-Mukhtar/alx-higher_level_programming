#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char = sentence[0]
    if sentence == "":
        return (0, None)
    return length, char
