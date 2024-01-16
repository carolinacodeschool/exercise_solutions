
# Change maker
# Write a function that calculates how many bills and coins someone would receive as change.

# Write a function `make_change` that accepts two arguments:
# * `total_charge` - the amount of money owed
# * `payment` - the amount of money payed

# Return a 2-dimensional tuple whose values represent the bills and coins.

# Example tuple
# ```py
# # Example change tuple
# (
#   (3, 0, 1, 1, 0, 1),
#   (4, 1, 0, 2)
# )
# ```

# The first item represents the bills:
# 3 singles, 0 fives, 1 ten, 1 twenty, 0 fifties, 1 hundred

# The second item represents the coins
# 4 pennies, 1 nickel, 0 dimes, 2 quarters

# Your function `make_change()` will return a tuple that resembles the above example based on
# the values the user gives for `payment` and `total_change`.
# Consider writing a small function to help produce the "bills" tuple and another function to help produce the "coins" tuple.

def generate_bills(bills):
    # Convert string input to integer, because maths
    bills = int(bills)
    # Calculate the number of each denomination
    # Order matters here!
    # Starting with singles will spit out a stack of $1 bills!
    hundreds = bills // 100 # divide the bills by hundreds
    bills %= 100            # update the bills to no longer count the hundreds
    fifties = bills // 50   # divide by fifties
    bills %= 50             # update the bills to no longer count the fifties
    twenties = bills // 20  # divide by twenties
    bills %= 20             # update the bills to no longer count the twenties
    tens = bills // 10      # divide by tens
    bills %= 10             # update the bills to no longer count the tens
    fives = bills // 5      # divide by fives
    bills %= 5              # update the bills to no longer count the fives
    singles = bills // 1    # finish up with the singles
    return (singles, fives, tens, twenties, fifties, hundreds)

def generate_coins(coins):
    coins = int(coins)
    quarters = coins // 25
    coins %= 25
    dimes = coins // 10
    coins %= 10
    nickels = coins // 5
    coins %= 5
    pennies = coins // 1
    return (pennies, nickels, dimes, quarters)

def make_change(total, payment):
    difference = round(payment - total, 2)
    difference_string = str(difference)
    parts = difference_string.split('.')
    bills_part = parts[0]
    coins_part = parts[1]

    bills_tuple = generate_bills(bills_part)
    coins_tuple = generate_coins(coins_part)
    return (bills_tuple, coins_tuple)


change_as_tuple = make_change(201.61, 300)

print("Change as tuple is: {}".format(change_as_tuple))

# Calculate the change value
# Write a `value_of_change` function that accepts a 2-dimensional tuple
# like the one returned by the `make_change` function.
# This function should calculate the monetary value specified by the tuple.

# For example, if the following tuple were passed to `value_of_change`
# ```py
# (
#   (3, 0, 1, 1, 0, 1),
#   (4, 1, 0, 2)
# )
# ```
# It would return `133.59`


def generate_bills(bills):
    # Calculate the number of each denomination
    hundreds = bills[5] * 100
    fifties = bills[4] * 50
    twenties = bills[3] * 20
    tens = bills[2] * 10
    fives = bills[1] * 5
    singles = bills[0] * 1
    total = hundreds + fifties + twenties + tens + fives + singles
    return total


def generate_coins(coins):
    quarters = coins[3] * 25
    dimes = coins[2] * 10
    nickels = coins[1] * 5
    pennies = coins[0] * 1
    total = quarters + dimes + nickels + pennies
    return total


def value_of_change(tuple):
    bills_total = generate_bills(tuple[0])
    coins_total = generate_coins(tuple[1])
    total_change = '$' + str(bills_total) + '.' + str(coins_total)
    return total_change


cash_value = value_of_change(change_as_tuple)

print("The cash value is: {}".format(cash_value))
