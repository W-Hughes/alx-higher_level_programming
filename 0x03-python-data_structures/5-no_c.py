#!/usr/bin/python3

def no_c(my_string):
    temp_string = ""

    for char in my_string:
        if (char != "c" and char != "C"):
            temp_string += char
    return (temp_string)
