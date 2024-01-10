# To draw a triangle, start with a rectangle
# that is twice as wide as it is tall.
# Also, it has
# one star in the first row
# three stars in the second row
# five stars in the third row
# etc.


# You can think about it in a number of different
# ways. Here are two of them:
# - Increase the number of stars per row
# - Decrease the number of spaces per row

# Option #1: increase the number of stars per row.
# As we draw each row, we need to determine
# how much to draw.

# The first row of a triangle is a single
# star in the very middle.
# ___*___
# This is equivalent to 
# The second row adds a star to either side.
# __***__
# 

# Option #2: increase the number of spaces per row.
# The first row of a triangle 3 spaces, a star, and 3 spaces 
# ___*___
# The second row is 2 spaces, 3 stars, and 2 spaces
# __***__

# The solution below is a mix of both options.

# Our triangle needs to have a "size" that is odd.
# (Otherwise, we can't center the stars.)

# Prompt the user until they enter an odd value.
# Default to an even one, 
size = 2 
while (size % 2) == 0:
    size = int(input("Please enter an odd number: "))



# let's use 2 nested loops:
# - an outer loop that draws rows
# - an inner loop that draws columns

# Our "outer loop" determines how many rows to draw
# of our triangle.
y = 0

# The height of our triangle will be half the "size"
while y < size/2:

    # Our "inner loop" draws a row at a time
    x = 0

    # Let's keep track of the number of stars
    # and the number of spaces

    # This starts our number of stars at 1.
    # For each row, we add 2 more stars.
    stars = 1 + (y * 2) 

    # The number of spaces is the size of the
    # triangle minus however many stars we
    # are drawing for this row
    spaces = size - stars

    # Technically, it's the size/2 minus the 
    # number of stars, but this code draws
    # each star with extra an space....because
    # it's prettier that way :)

    while x < size:

        # print(x, end='')
        if spaces > 0:
            print(' ', end='')

            # We drew a space, so 
            # we have one fewer to draw
            spaces = spaces - 1
        elif stars > 0:
            print('⭐️ ', end='')

            # We drew a star, so 
            # we have one fewer to draw
            stars = stars - 1

        # Move our inner loop closer to the end    
        x = x + 1

    # When the inner loop is finished, that means it
    # drew a row. We print() to make it start a new line.
    print()


    # Move our outer loop closer to the end
    y = y + 1