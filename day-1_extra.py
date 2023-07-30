# Day 1 Extra - longest_value

fruits = {
    'fruit': 'apple',
    'color': 'green',
    "shape": "round"
    }

def longest_value(dictionary: dict) -> int:
    longest: int = 0
    longest_val: str = ""

    for value in dictionary.values():
        value_length: int = len(value)
        if value_length != longest and value_length > longest:
            longest = value_length
            longest_val = value
    
    return longest_val

print(longest_value(fruits))