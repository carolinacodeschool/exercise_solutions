def find_smallest(numbers):
    numbers.sort()
    return numbers[0]

def find_smallest_alt(numbers):
    return min(numbers)


def find_largest(numbers):
    numbers.sort()
    return numbers[-1]


def find_largest_alt(numbers):
    return max(numbers)

print(find_smallest([11, 20, 42, 97, 23, 10]))
print(find_smallest_alt([11, 20, 42, 97, 23, 10]))

print(find_largest([11, 20, 42, 97, 23, 10]))
print(find_largest_alt([11, 20, 42, 97, 23, 10]))
