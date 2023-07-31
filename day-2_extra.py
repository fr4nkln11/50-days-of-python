# Day 2 Extra - Duplicate Names

fruits = ['apple', 'orange', 'banana', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicates(list_arg: list[str]) -> str | list[str]:
    """
    check_duplicates - check for duplicates in a list
    @list_arg: the list that will be checked for duplicates

    Return: {string} 'No duplicates' when there are no duplicates
    {list} of duplicates if there are any
    """
    duplicates = []
    unique = set(list_arg)

    if len(unique) == len(list_arg):
        return "No duplicates"
    else:
        for el in unique:
            if list_arg.count(el) > 1:
                duplicates.append(el)
        
        return duplicates

print(check_duplicates(fruits))
print(check_duplicates(names))