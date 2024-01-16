# 1. Change a List
#     * Use the following list: `numbers = [1, 2, 3, 4, 5, 99, 2600, 300]`
#     * There is a Python method that will [reverse a list](https://realpython.com/python-reverse-list/).
#     * Create a new variable called `reversed_list` and assign it the reversed value of `numbers`.
#     * Print the values of each list.

numbers = [1, 2, 3, 4, 5, 99, 2600, 300]

print(numbers)
numbers.reverse()
print(numbers)

# 2. String to List
#     * Make a string with at least 6 characters.
#     * Make an empty list (hint: create a variable with no value between the brackets)
#     * Loop through each letter in your string and for each letter in the string, append it to the empty list.
#     * Revese the list.
#     * Create a new variable that is an empty string.
#     * Loop through the list, for each letter in the list, add it to the new string your created.
#     * Print out the new string. It should be the reversed version of the string you created. i.e. "sean" -> "neas".

test_stuff = "Do rad stuff."

string_list = []
for letter in test_stuff:
    string_list.append(letter)
print(string_list)
string_list.reverse()
print(string_list)

new_string = ""
for letter in string_list:
    new_string += letter
print(new_string)

# 3. List + Conditional
#     * Make a new list containing members of your favorite band/sports team/television show.
#     * Write a conditional statement to check if a specific person is in that list.
#     * If they are in the list, remove them.
#     * If they're not in the list, add them.
#     Can you write a condition that does _both_ of these checks?
#     * Think like this: "If the person exists, then remove them. Otherwise, if they don't, add them.
#     * Print the updated list.

power_rangers = [
    "Jason",
    "Trini",
    "Zack",
    "Kim",
    "Billy",
    "Tommy"
]

print(power_rangers)
if "Tommy" in power_rangers:
    power_rangers.remove("Tommy")
    print(power_rangers)
else:
    print("IT'S MORPHIN TIME!")
