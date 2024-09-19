#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
    }

    number = 0
    last_value = 0

    for ch in roman_string:
        current_value = roman_numerals.get(ch, 0)

        if current_value > last_value:
            number += current_value - 2 * last_value
        else:
            number += current_value

        last_value = current_value

    return (number)
