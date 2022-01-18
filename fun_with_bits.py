#not code wars training
#goal is to transform dec value to bits, bits to hex, and again hex to dec

import math


def int_to_bits(number: int):
    number_bits = []
    while True:
        if number == 0:
            break
        bit = number % 2
        number_bits.append(bit)
        number = int(number / 2)
    number_bits.reverse()
    return number_bits


def get_hex_char(value):
    if value == 10:
        return "a"
    elif value == 11:
        return "b"
    elif value == 12:
        return "c"
    elif value == 13:
        return "d"
    elif value == 14:
        return "e"
    elif value == 15:
        return "f"
    else:
        return str(value)


def bits_to_hex(bits: list):
    hex_chars_list = []
    first_index = 0
    while True:
        if len(bits) % 4 != 0:
            bits.insert(0, 0)
        else:
            break
    hex_chars_amount = int(len(bits) / 4)
    for i in range(1, hex_chars_amount+1):
        value = 0
        hex_chars_range = bits[first_index:4*i]
        hex_chars_range.reverse()
        for j in range(len(hex_chars_range)):
            if hex_chars_range[j] != 0:
                x = int(math.pow(2, j))
                value += x
        hex_chars_list.append(get_hex_char(value))
        first_index = 4*i
    return "0x"+"".join(hex_chars_list)


def hex_to_int(value: str):
    return int(value, 16)


num = 852963
num_bits = int_to_bits(num)
num_hex = bits_to_hex(num_bits)
num_again = hex_to_int(num_hex)
print(num)
print(num_bits)
print(num_hex)
print(num_again)
