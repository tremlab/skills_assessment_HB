"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def is_hometown(town):
    """Checks if town is equal to Renee's hometown ;)
    >>> is_hometown("Chicago")
    False

    >>> is_hometown("Columbus")
    True
    """

    return town == "Columbus"


def make_full_name(first, last):
    """concatenates first and last name strings into one, with space between.

    >>> make_full_name("Will", "Smith")
    'Will Smith'
    """
    return first + " " + last


def greet_local(hometown, first_name, last_name):
    """Greets by full name, according to local or not.

    >>> greet_local("Chicago", "Will", "Smith")
    Hi, Will Smith, where are you from?
    """
    full_name = make_full_name(first_name, last_name)

    if is_hometown(hometown):
        local_msg = "we're from the same place!"
    else:
        local_msg = "where are you from?"
    #instrucitons asked for print, rather than return
    print "Hi, %s, %s" % (full_name, local_msg)



###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    return fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry"

# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.


def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit):
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([1,2,3], 4)
    [1, 2, 3, 4]
    """

    lst.append(num)
    return lst


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(price, state, tax=.05):
    """    Calculates total price based on item price, state, and tax.
    """
    state_fee = 0.00
    price_with_tax = price + (price * tax)

    if state == "CA":
        state_fee = price_with_tax * .03
    elif state == "PA":
        state_fee = 2.00
    elif state == "MA":
        if price_with_tax < 100:
            state_fee = 1.00
        else:
            state_fee = 3.00

    total_price = price_with_tax + state_fee
    #why does the test show cost amounts in 1 decimal place?
    return float("%.1f" % (total_price))


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


#1


def extend_list(a_list, *args):
    """accepts a list and any number of additional items,
    appends each itemto list.

    >>> extend_list([1,2,3], 6, 10, 4, 5)
    [1, 2, 3, 6, 10, 4, 5]
    """

    for arg in args:
        a_list.append(arg)

    return a_list

#2


def triple_string(word):
    """multiplIes given string by 3, returns original and treble string as tuple.

    >>> triple_string("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')
    """
    def treble(str_word):
        return str_word * 3

    string_3 = tuple([word, treble(word)])

    return string_3

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
