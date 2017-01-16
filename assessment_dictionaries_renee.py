"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    word_count = {}
    words = phrase.split()

    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    price_per_melon = {

    "Watermelon":  2.95,
    "Cantaloupe": 2.50,
    "Musk": 3.25,
    "Christmas": 14.25,

    }

    if melon_name in price_per_melon:
        return price_per_melon[melon_name]
    else:
        return 'No price found'

    return 0


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    words_by_length = {}
    words_alphabetized = []

    # loop through word list, assign words of same length into value list
    # at key of word length as int, sort each value list.

    for word in words:
        wlength = len(word)
        if wlength in words_by_length.keys():
            words_by_length[wlength].append(word)
            # if the given lists were very long, I'd sort them outside the loop
            # but this seemed like the most elegant solution here.
            words_by_length[wlength].sort()
        else:
            words_by_length[wlength] = [word]

    # assign each word length int, and the list of words that have that length,
    # as a tuple pair into a containing list

    for wlength, word_collection in words_by_length.items():
        words_alphabetized.append((wlength, word_collection))

    # sort the containing list on word length int
    words_alphabetized.sort()

    return words_alphabetized


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    words = phrase.split()
    pirate_phrase = []

    for word in words:
        if word in english_to_pirate:
            pirate_phrase.append(english_to_pirate[word])
        else:
            pirate_phrase.append(word)

    return " ".join(pirate_phrase)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # remove first name from given list, add it as first name in new list
    name_sequence = [names.pop(0)]
    first_letter_for_words = {}

    # group all words in input list into dictionary by key of their first letter,
    # in order of appearance in the input list

    for name in names:
        first_letter = name[0].lower()

        if first_letter in first_letter_for_words:
            first_letter_for_words[first_letter].append(name)
        else:
            first_letter_for_words[first_letter] = [name]

    # return last letter of last word of the list passed in.
    # # internal function to clean up code that was getting too murky.
    # # will use below to search for the next word in sequence.

    def last_letter(word_list):
        return word_list[-1][-1].lower()

    # keep grabbing the next available word from the list value in dict,
    # where key = last letter of last word in the sequence so far,
    # until there are no more words left in that list,
    # or that letter isn't even in the dictionary at all.

    while True:
        letter = last_letter(name_sequence)
        if letter in first_letter_for_words:
            if len(first_letter_for_words[letter]) > 0:
                pull_word = first_letter_for_words[letter].pop(0)
                name_sequence.append(pull_word)
            else:
                break
        else:
            break

    return name_sequence

#####################################################################
# You can ignore everything below this.


def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
