# Day 2 - Strings to Integers

def convert_add(strings: list) -> int:
    return sum([int(x) for x in strings])
print(convert_add(['1','3','5']))
