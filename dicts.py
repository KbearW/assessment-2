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
    counts = {}
    phrase = phrase.split()
    for word in phrase:
        counts[word] = counts.get(word, 0) + 1
    
    return counts

# if __name__ == "__main__":
#     phrase1 = "each word appears once"
#     print(f"Should return:['appears': 1, 'each': 1, 'once': 1, 'word': 1:] --> {count_words(phrase1)}")
#     phrase2 = "rose is a rose is a rose"
#     print(f"Should return:['a': 2, 'is': 2, 'rose': 3] --> {(count_words(phrase2))}")
#     phrase3 = "Porcupine see, porcupine do."
#     print(f"Should return:['Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1] --> {(count_words(phrase3))}")

def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """
    melon_dict = {1: 'Honeydew', 2: 'Cantaloupe', 3: 'Watermelon', 4: 'Musk', 5: 'Crenshaw', 6: 'Christmas'}
    price_dict = {1: 2.50, 2: 2.50, 3: 2.95, 4: 3.25, 5: 3.25, 6: 14.25}

    result = []
    for k, v in price_dict.items():
        if v == price:
            result.append(melon_dict[k])
    
    result.sort()
    for i in result:
        print(i)

    
    if result == []:
        print("None found")
    
    # test cases, will return "None" since the prompt asks for print!
# if __name__ == "__main__":
#     print(f"The result should print: Cantaloupe & Honeydew: \n{print_melon_at_price(2.50)}")
#     print("")
#     print(f"The result should be Watermelon: \n{print_melon_at_price(2.95)}")
#     print("")
#     print(f"The result should be None found: \n{print_melon_at_price(5.50)}")



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
    # create dict: maybe 1 or 2 - depends on setup
    # iterate over the dict for phrase
        # translate the words to the new lanuage, if not found, repeat original words

    result =[]
    translation = {'sir': 'matey', 'hotel': 'fleabag', 'student': 'swabbie', 'man': 'matey', 
                    'professor':'foul blaggart', 'restaurant':'galley','your':'yer','excuse':'arr',
                    'students':'swabbies','are':'be','restroom':'head','my':'me','is':'be'}
    # english = {1: 'sir', 2: 'hotel'}
    # pirate = {1: 'matey', 2:'fleabag'}

    """Nope, still not working!"""
    phrase = phrase.split()
    # print(f'input phrase is: {phrase}')
    # print("#############")
    # print(f'dict is: {translation}')
    # print("#############")
    
    for word in phrase:
        # print(word)
        if word in translation.keys():
            result.append(translation[word])
        else:
            # print('None')
            result.append(word)

    str1 = " "
    
    print(str1.join(result))

    return str1.join(result)

# if __name__ == "__main__":
#     translate_to_pirate_talk("my student is not a man")
#     translate_to_pirate_talk("my student is not a man!")




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
    print(names)
    result = []
    name = set(name)
    return []
