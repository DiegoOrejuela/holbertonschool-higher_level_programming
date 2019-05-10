#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    num_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if num_rom[roman_string[i]] >= num_rom[roman_string[i + 1]]:
                result += num_rom[roman_string[i]]
            if num_rom[roman_string[i]] < num_rom[roman_string[i + 1]]:
                result -= num_rom[roman_string[i]]
        else:
            result += num_rom[roman_string[i]]
    return result
