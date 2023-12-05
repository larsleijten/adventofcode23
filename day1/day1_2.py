import os


def get_key_for_value(my_dict, my_value):
    for key, value in my_dict.items():
        if value == my_value:
            return key
    raise (Exception("Mismatch"))


def find_first_digit(text, letter_digits):
    for i, character in enumerate(text):
        if character.isdigit():
            return character
        elif text[i:i+5] in letter_digits.values():
            return get_key_for_value(letter_digits, text[i:i+5])
        elif text[i:i+4] in letter_digits.values():
            return get_key_for_value(letter_digits, text[i:i+4])
        elif text[i:i+3] in letter_digits.values():
            return get_key_for_value(letter_digits, text[i:i+3])
    return 0


def find_last_digit(reversed_text, reversed_letter_digits):
    for i, character in enumerate(reversed_text):
        if character.isdigit():
            return character
        elif reversed_text[i:i+5] in reversed_letter_digits.values():
            return get_key_for_value(reversed_letter_digits, reversed_text[i:i+5])
        elif reversed_text[i:i+4] in reversed_letter_digits.values():
            return get_key_for_value(reversed_letter_digits, reversed_text[i:i+4])
        elif reversed_text[i:i+3] in reversed_letter_digits.values():
            return get_key_for_value(reversed_letter_digits, reversed_text[i:i+3])
    return 0


letter_digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

reversed_letter_digits = {key: value[::-1]
                          for key, value in letter_digits.items()}

codefile = open("input.txt", "r")

lines = codefile.readlines()
values = []
for line in lines:
    first_digit = int(find_first_digit(line, letter_digits))
    last_digit = int(find_last_digit(line[::-1], reversed_letter_digits))
    value = first_digit * 10 + last_digit
    values.append(value)

sum_values = sum(values)


print(sum_values)
