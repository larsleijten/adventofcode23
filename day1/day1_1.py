import os


def find_first_digit(text):
    for character in text:
        if character.isdigit():
            return character
    return 0


def find_last_digit(text):
    for character in reversed(text):
        if character.isdigit():
            return character
    return 0


codefile = open("input.txt", "r")

lines = codefile.readlines()
values = []
for line in lines:
    first_digit = int(find_first_digit(line))
    last_digit = int(find_last_digit(line))
    value = first_digit * 10 + last_digit
    values.append(value)

sum_values = sum(values)


print(sum_values)
