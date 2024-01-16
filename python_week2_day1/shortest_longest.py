def shortest(list_of_strings):
    # This is our starting placeholder value
    # We'll start with the first item in the list
    # and compare every other item against it
    shortest = list_of_strings[0]
    i = 0
    while i < len(list_of_strings):
        if (len(list_of_strings[i]) <= len(shortest)):
            shortest = list_of_strings[i]
        i += 1
    return shortest

def longest(list_of_strings):
    # This is our starting placeholder value
    longest = list_of_strings[0]
    i = 0
    while i < len(list_of_strings):
        if (len(list_of_strings[i]) >= len(longest)):
            longest = list_of_strings[i]
        i += 1
    return longest

some_strings = ['of', 'crackle', 'foo', 'a', 'bard', 'fizzle']

print(shortest(some_strings))
print(longest(some_strings))
