# Start/End
# * Ask the user for a starting number, assign it to a variable.
# * Ask the user for an ending number, assign it to a variable.
# * Write a loop that increments the starting number by `1` until it matches the ending number.

start = int(input("Start from: "))
end = int(input("End on: "))

count = start

while count <= end:
    print(count)
    count += 1

# Bonus
# * Can you write a loop that increments by more than `1`?

while count <= end:
    print(count)
    count += 5

# * Can you create a range of numbers from which the user can choose?
# * Can you let the user know when they choose something out of that range?

def check_in_range(num):
    if num >= 1 and num <= 5:
        return True
    else:
        return False

def throw_error(value_type):
    return "Please choose a different {} value".format(value_type)

running = True
while running == True:
    start = int(input("Pick a number from 1-5 to start from: "))
    end = int(input("Pick a number from 1-5 to end on: "))

    if check_in_range(start) == True and check_in_range(end) == True:
        if end <= start:
            print(throw_error("end"))
        while start <= end:
            print(start)
            start += 1
            if start == end:
                running = False
    else:
        if check_in_range(start) == False:
            print(throw_error("start"))
        if check_in_range(end) == False or end >= start:
            print(throw_error("end"))
