# Vesion 3 - prints the finished triangle all at once

# -----------------------------------------------------------------
# configuration
max_height = 4  # default to 4 rows tall
max_width = 7   # default to 7 columns wide
triangle = ""

# -----------------------------------------------------------------
# process


# get a height from the user
max_height = int(input("Height? "))

# calculate the width of our triangle
max_width = (max_height * 2) - 1

# calculate the number of blanks to the left and right
number_of_blanks = max_height - 1

# start creating that triangle!
for height_count in range(max_height):

    # create an identifier for a string that represents our row
    row = ""

    # use an inner loop to build up our row.
    # to make the math easier, add 1
    for column_count in range(1, max_width + 1):

        # if the column number is less than the number of
        # blanks to the left, add a space
        if column_count <= number_of_blanks:
            row = row + " "
        # if the column number is greater than the number of
        # blanks to the right, add a space
        elif column_count > (max_width - number_of_blanks):
            row = row + " "

        # otherwise, let's add part of the triangle
        else:
            # FOR DEBUGGING: this line will print the column number
            # row = row + str(column_count)

            # For real, add the asterisk
            row = row + "*"

    # with each row, we have a 1 fewer blanks on either side
    number_of_blanks = number_of_blanks - 1

    # add the row that just got calculated
    triangle = triangle + row + "\n"


# -----------------------------------------------------------------
# result
print(triangle)