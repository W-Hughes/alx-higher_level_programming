#!/usr/bin/python3

def multiple_returns(sentence):
    len_sentence = len(sentence)
    first_char = sentence[0] if len_sentence > 0 else None
    return (len_sentence, first_char)
