# ----------------------------- #
# Title: except_excercise.py
# Desc: An exercise in playing with Exceptions
# Change Log: (Who, When, What)
# KCreek, 2/5/2019, Altered Script
# ----------------------------- #
#!/usr/bin/python

from except_test import fun, more_fun, last_fun

try:
    first_try = ['spam', 'cheese', 'mr death']

    joke = fun(first_try[0])

# Figure out what the exception is, catch it
except NameError:
    # while still in that catch block, try again with the second item in the list
    joke = fun(first_try[1])

# Here is a try/except block.
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
# Add an else that prints not_joke
else:
    not_joke = fun(first_try[2])
    print(not_joke)

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)


langs = ['java', 'c', 'python']

try:
    more_joke = more_fun(langs[0])
# Figure out what the exception is, catch it and in that same block
except IndexError:
    # try calling the more_fun function with the 2nd language in the list,
    # again assigning it to more_joke.
    more_joke = more_fun(langs[1])
# If there are no exceptions, call the more_fun function with the last
# language in the list
else:
    more_joke = more_fun(langs[2])
# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)
finally:
    last_fun()
