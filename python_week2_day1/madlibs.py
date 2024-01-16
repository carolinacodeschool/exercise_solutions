# Madlib function
# Write a function that accepts two arguments: a name and a subject.
# The function should return a String with the name and subject interpolated in.

def madlib(name, subject):
    the_madlib = "Your name is %s and your favorite subject is %s" % (
        name, subject)
    return the_madlib

my_story = madlib("Sean", "English")
print(my_story)
