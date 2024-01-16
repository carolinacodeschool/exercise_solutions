# `is_even` function
# Write a function that accepts a number as an argument and returns a Boolean value. Return `True` if the number is even; return `False` if it is not even.

def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(75))

# `is_odd` function
# Write an `is_odd` function that uses your `is_even` function to determine if a number is odd. (That is, do not do the calculation - call a function that does the calculation.)

def is_odd(number):
    if (number % 2) != 0:
        return True
    else:
        return False

print(is_odd(11))
print(is_odd(42))

# `only_evens` function
# Write a function that accepts a List of numbers as an argument.
# Return a new List that includes the only the even numbers.

def only_evens(numbers):
    i = 0
    even_numbers = []
    while i < len(numbers):
        if (numbers[i] % 2) == 0:
            even_numbers.append(numbers[i])
        i = i + 1
    return even_numbers

print(only_evens([11, 20, 42, 97, 23, 10]))

# `only_odds` function
# Write a function that accepts a List of numbers as an argument.
# Return a new List that includes the only the odd numbers.

def only_odds(numbers):
    i = 0
    odd_numbers = []
    while i < len(numbers):
        if (numbers[i] % 2) != 0:
            odd_numbers.append(numbers[i])
        i = i + 1
    return odd_numbers

print(only_odds([11, 20, 42, 97, 23, 10]))
